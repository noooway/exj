from datetime import datetime

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from ExerciseSetsRepsWeightsWidget import *

from Training import *

class TrainingScreen( Screen ):    
    def __init__( self, **kwargs ):
        super( TrainingScreen, self ).__init__( **kwargs )
        self.excercise_widgets = []
        self.training = Training()
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 5 )
        label = Label( text = 'List of exercises',
                       size_hint = (1.0, 0.3) )
        v_layout.add_widget( label )
        self.exercises_layout = GridLayout(
            cols = 1,
            spacing = 5,
            size_hint_y = None )
        self.exercises_layout.bind( minimum_height =
                                    self.exercises_layout.setter('height') )
        self.scroll_for_exercises = ScrollView()                
        self.scroll_for_exercises.add_widget( self.exercises_layout )
        v_layout.add_widget( self.scroll_for_exercises )
        add_exc_button = Button( text = 'Add exercise', size_hint_y = 0.2 )
        add_exc_button.on_press = self.goto_select_exercise
        v_layout.add_widget( add_exc_button )
        self.training_comment = TextInput( hint_text = 'Comment Training',
                                           size_hint_y = 0.1 )
        self.training_comment.bind( text = self.update_training_from_user_input )
        v_layout.add_widget( self.training_comment )
        back_layout = BoxLayout( orientation = 'horizontal',
                                 spacing = 30,
                                 size_hint = ( 1.0, 0.2 ) )
        discard_button = Button(
            text = 'Discard' )
        discard_button.on_press = self.goto_start_exercising
        save_and_exit_button = Button(
            text = 'Save and go back' )
        save_and_exit_button.on_press = self.save_training_and_goto_start_exercising
        back_layout.add_widget( discard_button )
        back_layout.add_widget( save_and_exit_button )
        v_layout.add_widget( back_layout )
        self.add_widget( v_layout )
        self.following_plan = False        

    def add_exercise( self, exercise_name, exercise_widget_type ):
        if exercise_widget_type == 'ExerciseSetsRepsWeightsWidget': 
            self.exercises_layout.add_widget(
                ExerciseSetsRepsWeightsWidget( self, text = exercise_name ) )
        else:
            print( 'Unknown excercise type:', exercise_widget_type )
        
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

    def save_training_and_goto_start_exercising( self ):
        self.add_time_information_to_training()
        self.add_info_on_used_program()
        journal = App.get_running_app().journal
        journal.add_training( self.training )
        journal.save_journal( App.get_running_app().journal_file )
        App.get_running_app().simple_program_last_training = self.last_training_index
        App.get_running_app().write_config()
        self.training = Training()
        self.exercises_layout.clear_widgets()
        self.training_comment.text = ''
        self.parent.current = 'start_exercising'

    def on_pre_enter( self ):
        self.last_training_index = App.get_running_app().simple_program_last_training
        if self.following_plan:
            current_program = App.get_running_app().simple_program
            self.last_training_index = \
                ( self.last_training_index + 1 ) % len( current_program.trainings )
            training = current_program.trainings[ self.last_training_index ]
            for ex in training.exercises:
                self.add_exercise( ex.description['name'],
                                   ex.description['type'] + 'Widget' )
        
    def on_enter( self ):
        self.start_time = datetime.now()

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
            used_training_program_name = App.get_running_app().simple_program.name
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
