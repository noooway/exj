from datetime import datetime

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from exercises_and_metrics_types import *
from Training import *

class TrainingScreen( Screen ):    
    def __init__( self, **kwargs ):
        super( TrainingScreen, self ).__init__( **kwargs )
        self.excercise_widgets = []
        self.training = Training()
        self.main_layout = BoxLayout( orientation = 'vertical',
                              spacing = 5 )
        label = Label( text = 'List of exercises',
                       size_hint = (1.0, 0.3) )
        self.main_layout.add_widget( label )
        self.exercises_layout = GridLayout(
            cols = 1,
            spacing = 5,
            size_hint_y = None )
        self.exercises_layout.bind(
            minimum_height = self.exercises_layout.setter('height') )
        self.scroll_for_exercises = ScrollView()                
        self.scroll_for_exercises.add_widget( self.exercises_layout )
        self.main_layout.add_widget( self.scroll_for_exercises )
        self.main_layout.add_widget( Label(size_hint_y = 0.1) )
        add_exc_button = Button( text = 'Add exercise',
                                 size_hint_y = 0.2 )
        add_exc_button.on_press = self.goto_select_exercise
        self.main_layout.add_widget( add_exc_button )
        self.training_comment = TextInput( hint_text = 'Comment Training',
                                           size_hint_y = 0.1 )
        self.training_comment.bind( text =
                                    self.update_training_from_user_input )
        self.main_layout.add_widget( self.training_comment )
        back_layout = BoxLayout( orientation = 'horizontal',
                                 spacing = 30,
                                 size_hint = ( 1.0, 0.2 ) )
        discard_button = Button( text = 'Discard' )
        discard_button.on_press = self.goto_start_exercising
        save_and_exit_button = Button( text = 'Save and go back' )
        save_and_exit_button.on_press = \
            self.save_training_and_goto_start_exercising
        back_layout.add_widget( discard_button )
        back_layout.add_widget( save_and_exit_button )
        self.main_layout.add_widget( back_layout )
        self.add_widget( self.main_layout )
        self.following_plan = False
        self.changer_layout = None
        self.back_from_exc_selection = False

    def add_exercise( self, exercise ):
        exercise_type_name = exercise.__class__.__name__
        exercise_widget_name = exercise_type_name + 'Widget'
        WidgetClass = globals().get( exercise_widget_name )
        if WidgetClass:
            exc_widget = WidgetClass( exercise, self )
            self.exercises_layout.add_widget( exc_widget )
        else:
            print( exercise_type_name,
                   " doesn't have corresponding widget type" )
        
    def update_training_from_user_input( self, *rest ):
        exercises = []
        for exc_widget in self.exercises_layout.children:
            exc = exc_widget.exercise_from_user_input()
            exercises.insert( 0, exc )
        training_comment = self.training_comment.text
        self.training = Training( *exercises, comment=training_comment )
        
    def goto_select_exercise( self ):
        self.parent.current = 'select_exercise'
        
    def goto_start_exercising( self ):
        self.training = Training()
        self.exercises_layout.clear_widgets()
        self.training_comment.text = ''
        self.parent.current = 'start_exercising'
        if self.following_plan:
            self.following_plan = False
            self.main_layout.remove_widget( self.changer_layout )
            self.changer_layout = None

    def save_training_and_goto_start_exercising( self ):
        self.add_time_information_to_training()
        self.add_info_on_used_program()
        journal = App.get_running_app().journal
        journal.add_training( self.training )
        journal.save_journal( App.get_running_app().journal_file )
        App.get_running_app().simple_program_last_training = \
            self.last_training_index
        App.get_running_app().write_config()
        self.training = Training()
        self.exercises_layout.clear_widgets()
        self.training_comment.text = ''
        if self.following_plan:
            self.following_plan = False
            self.main_layout.remove_widget( self.changer_layout )
            self.changer_layout = None
        self.parent.current = 'start_exercising'

    def on_pre_enter( self ):
        self.last_training_index = \
          App.get_running_app().simple_program_last_training
        if self.following_plan and not self.back_from_exc_selection:
            self.add_training_changer()
            current_program = App.get_running_app().simple_program
            self.last_training_index = \
                ( self.last_training_index + 1 ) % \
                len( current_program.trainings )
            training = \
              current_program.trainings[ self.last_training_index ]
            for ex in training.exercises:
                self.add_exercise( ex )
        self.back_from_exc_selection = False
                
    def on_enter( self ):
        self.start_time = datetime.now()

    def add_training_changer( self ):
        if not self.changer_layout:
            self.changer_layout = BoxLayout( orientation = 'horizontal',
                                             spacing = 5,
                                             size_hint_y = 0.05 )
            label = Label(
                text = 'Select another training from the program:' )
            prev_btn = Button( text = 'Prev', size_hint_x = 0.2 )
            prev_btn.on_press = self.select_prev_training
            next_btn = Button( text = 'Next', size_hint_x = 0.2 )
            next_btn.on_press = self.select_next_training
            self.changer_layout.add_widget( label )
            self.changer_layout.add_widget( prev_btn )
            self.changer_layout.add_widget( next_btn )
            self.main_layout.add_widget(
                self.changer_layout,
                len( self.main_layout.children ) )

    def select_prev_training( self ):
        self.exercises_layout.clear_widgets()
        current_program = App.get_running_app().simple_program
        self.last_training_index = \
            ( self.last_training_index - 1 ) % \
            len( current_program.trainings )
        training = current_program.trainings[ self.last_training_index ]
        for ex in training.exercises:
            self.add_exercise( ex )
        

    def select_next_training( self ):
        self.exercises_layout.clear_widgets()
        current_program = App.get_running_app().simple_program
        self.last_training_index = \
            ( self.last_training_index + 1 ) % \
            len( current_program.trainings )
        training = current_program.trainings[ self.last_training_index ]
        for ex in training.exercises:
            self.add_exercise( ex )

        
    def add_time_information_to_training( self ):
        training_date = self.start_time.strftime('%d-%m-%Y')
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        self.training.add_description(
            date = training_date,
            start_time = str( self.start_time ),
            end_time = str( self.end_time ),
            duration = str( duration ) )

    def add_info_on_used_program( self ):
        if self.following_plan:
            used_training_program_name = \
                App.get_running_app().simple_program.get_name()
            training_index_in_program = self.last_training_index
        else:
            used_training_program_name = None
            training_index_in_program = None
        self.training.add_description(
            training_program = used_training_program_name,
            training_index_in_program = training_index_in_program )
        

    def remove_exercise( self, exercise_widget ):
        self.exercises_layout.remove_widget( exercise_widget )
        self.update_training_from_user_input()
        print( 'del' )
