from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

import os
from SimpleProgram import *

class SimpleProgramsScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SimpleProgramsScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 20 )
        label = Label( text = 'Select a program:', size_hint_y = 0.1 )
        v_layout.add_widget( label )
        programs_grid = GridLayout( cols = 1,
                                    spacing = 5,
                                    size_hint_y = None )
        dict_of_simple_programs = \
            App.get_running_app().dict_of_simple_programs
        for k, v in dict_of_simple_programs.items():
            self.add_simple_program_widget( programs_grid, v )
        programs_grid.bind( minimum_height =
                            programs_grid.setter('height') )
        scroll_for_programs = ScrollView( size_hint_y = 0.6 )
        scroll_for_programs.add_widget( programs_grid )
        v_layout.add_widget( scroll_for_programs )                
        create_custom_program = Button(
            text = 'Create custom program (not implemented)',
            size_hint_y = 0.15 )
        v_layout.add_widget( create_custom_program )
        back_button = Button( text = 'Back',
                              size_hint_y = 0.15 )
        back_button.on_press = self.goto_programs_screen
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )
        
    def add_simple_program_widget( self, parent_layout, simple_program ):
        program_layout = GridLayout( cols = 1,
                                     row_default_height = 70,
                                     size_hint_y = None )
        program_layout.bind(
            minimum_height = program_layout.setter('height') )
        #print( simple_program )
        btn = Button( text = simple_program.description["name"],
                      on_press = self.select_program_and_goto_main_screen )
        btn.simple_program = simple_program
        program_layout.add_widget( btn )
        description_layout = GridLayout( cols = 1,
                                         row_default_height = 20,
                                         row_force_default = True,
                                         size_hint_y = None )
        description_layout.bind(
            minimum_height = description_layout.setter('height') )
        for i, tr in enumerate( simple_program.trainings ):
            training_label = Label( text = "Training {0}:".format( i+1 ) )
            description_layout.add_widget( training_label )
            for ex in tr.exercises:
                ex_label = Label( text = str( ex ) )
                description_layout.add_widget( ex_label )
        program_layout.add_widget( description_layout )
        parent_layout.add_widget( program_layout )

    def goto_programs_screen( self ):
        self.parent.current = 'compose_training_plan'

    def select_program_and_goto_main_screen( self, btn ):
        app = App.get_running_app()
        selected_program = btn.simple_program
        for k, v in app.dict_of_simple_programs.items():
            if v == selected_program:
                selected_program_name = k
        app.simple_program = selected_program
        app.simple_program_name = selected_program_name
        app.simple_program_last_training = -1
        app.write_config()
        self.parent.current = 'menu'
