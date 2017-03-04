import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.popup import Popup

from Journal import *

class JournalOverviewScreen( Screen ):
    def __init__( self, **kwargs ):
        super( JournalOverviewScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        self.tree_view = TreeView( root_options = dict( text = 'Tree One' ),
                                   hide_root = True,
                                   indent_level = 4 )
        self.tree_view.size_hint = ( 1, None )
        self.tree_view.bind( minimum_height = self.tree_view.setter( 'height' ) )
        scroll = ScrollView( pos = (0, 0) )
        scroll.add_widget( self.tree_view )    
        v_layout.add_widget( scroll )
        change_journal_layout = BoxLayout( orientation = 'horizontal',
                                           spacing = 5,
                                           size_hint_y = 0.1 )
        change_journal_layout.add_widget(
            Label( text = 'Journal file:' ) )
        self.journal_file_input = TextInput(
            text = App.get_running_app().journal_file )
        change_journal_layout.add_widget( self.journal_file_input )
        change_journal_layout.add_widget(
            Button( text = 'Set another',
                    on_press = self.set_another_journal ) )
        v_layout.add_widget( change_journal_layout )
        back_to_progress_button = Button( text = 'Back',
                                          size_hint_y = 0.2 )
        back_to_progress_button.on_press = self.goto_progress
        v_layout.add_widget( back_to_progress_button )
        self.add_widget( v_layout )

    def on_pre_enter( self ):
        self.populate_tree_view()

    def on_leave( self ):
        for node in self.tree_view.iterate_all_nodes():
            self.tree_view.remove_node( node )
        
    def populate_tree_view( self ):
        journal = App.get_running_app().journal
        journal_node = self.tree_view.add_node(
            TreeViewLabel( text = 'Journal', is_open = True ) )
        for training in journal.trainings:
            training_node = self.tree_view.add_node(
                TreeViewLabel( text = training.description['date'] + ': Training' ),
                journal_node )
            label_str = 'Start time: ' + \
                        str( training.description['start_time'] )
            #training.description['start_time'].strftime('%H:%M:%S')
            self.tree_view.add_node(
                TreeViewLabel( text = label_str ), training_node )
            label_str = 'End time: ' + \
                        str( training.description['end_time'] )
            self.tree_view.add_node(
                TreeViewLabel( text = label_str ), training_node )
            label_str = 'Duration: ' + \
                        str( training.description['duration'] )
            self.tree_view.add_node(
                TreeViewLabel( text = label_str ), training_node )
            label_str = 'Training program: ' + \
                        str( training.description['training_program'] )
            self.tree_view.add_node(
                TreeViewLabel( text = label_str ), training_node )
            label_str = 'Training index in program: ' + \
                        str( training.description['training_index_in_program'] )
            self.tree_view.add_node(
                TreeViewLabel( text = label_str ), training_node )
            for exercise in training.exercises:
                title_node_text = 'Exercise: ' + exercise.description['name']
                if 'Metric' in exercise.description.get( 'type' ):
                    title_node_text = 'Metric: ' + exercise.description['name']
                exc_node = self.tree_view.add_node(
                    TreeViewLabel( text = title_node_text ), training_node )
                for essential_field in exercise.essential_fields:
                    label_str = essential_field + \
                                ': ' + str( exercise.description[essential_field] )
                    self.tree_view.add_node(
                        TreeViewLabel( text = label_str ), exc_node )
                if exercise.description['comment']:
                    label_str = 'Comment: ' + \
                                str( exercise.description['comment'] )
                    self.tree_view.add_node(
                        TreeViewLabel( text = label_str ), exc_node )
            if training.description['comment']:
                label_str = 'Comment: ' + \
                            str( training.description['comment'] )
                self.tree_view.add_node(
                    TreeViewLabel( text = label_str ), training_node )


    def goto_progress( self ):
        self.parent.current = 'view_progress'


    def set_another_journal( self, *rest ):
        app = App.get_running_app()
        journal_file = self.journal_file_input.text
        filename, file_extension = os.path.splitext( journal_file )
        if file_extension != '.json':
            self.show_not_json_popup()
            return
        if journal_file != app.journal_file:
            app.journal_file = journal_file
            if os.path.isfile( app.journal_file ):
                app.journal = Journal.load_journal( app.journal_file )
            else:
                app.journal = Journal()
        app.write_config()
        for node in self.tree_view.iterate_all_nodes():
            self.tree_view.remove_node( node )
        self.populate_tree_view()

    def show_not_json_popup( self ):
        popup_content = BoxLayout( orientation = 'vertical' )
        popup_content.add_widget( Label(
            text = 'The journal file is expected ' + 
            'to have a ".json" extension.\n' + 'Please, specify ' +
            'another file.',                
            haling = 'center') )
        close_btn = Button( text = 'Ok', size_hint_y = 0.2 )
        popup_content.add_widget( close_btn )
        popup = Popup(title = 'Error: journal file is not JSON',
                      content = popup_content,
                      size_hint=( None, None ), size=(400, 400) )
        close_btn.bind( on_press = popup.dismiss )
        popup.open()
