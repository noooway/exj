import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel

from Journal import *
from Training import *
from SimpleProgram import *
import list_of_exercises

# Declare screens
class MenuScreen( Screen ):
    def save_journal_and_quit( self ):
        app = App.get_running_app()
        app.journal.save_journal("default_journal.json")
        app.stop()

class StartExercisingScreen( Screen ):
    def generate_and_goto_training( self ):
        journal = App.get_running_app().journal
        current_program = App.get_running_app().simple_program
        training = current_program.advise_current_training( journal )
        for ex in training.exercises:
            self.parent.get_screen('training').add_exercise(
                ex.description['name'],
                ex.description['type'] )
        self.parent.current = 'training'

        
class ComposeTrainingPlanScreen( Screen ):
    pass

class SimpleProgramSelectionScreen( Screen ):
    def goto_program_content( self, button ):
        program_name = button.text
        if program_name == 'Beginners':
            selected_program = novice_simple_program
        elif program_name == '2 day split':
            selected_program = twoday_simple_program
            
        self.parent.get_screen('simple_program_content').update_selected_program(
            selected_program )
        self.parent.current = 'simple_program_content'

class SimpleProgramContentScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SimpleProgramContentScreen, self ).__init__( **kwargs )
        self.selected_simple_program = App.get_running_app().simple_program
    
    def update_selected_program( self, simple_program ):
        self.selected_simple_program = simple_program
        self.ids['program_content'].text = str( self.selected_simple_program )

    def set_and_go_to_menu( self ):
        App.get_running_app().simple_program = self.selected_simple_program
        self.parent.current = 'menu'

class ViewProgressScreen( Screen ):
    pass

class SpecificGoalProgramsScreen( Screen ):
    pass

class TrainingScreen( Screen ):
    def __init__( self, **kwargs ):
        super( TrainingScreen, self ).__init__( **kwargs )
        self.training = Training()
    
    def post_kv_build( self ):
        grid_layout = self.ids['exercises_list']
        grid_layout.bind( minimum_height = grid_layout.setter('height') )

    def add_exercise( self, exercise_name, exercise_type ):
        if exercise_type == 'ExerciseSetsRepsWeights':
            ex_widget = ExerciseSetsRepsWeightsWidget( self, text = exercise_name )
            self.ids['exercises_list'].add_widget( ex_widget )
        else:
            print( 'Unknown excercise type:', exercise_type )

    def update_training_from_user_input( self, *unused_rest ):
        exercises = []
        for exercise_widget in self.ids['exercises_list'].children:
            exc = exercise_widget.exercise_from_user_input()
            exercises.insert( 0, exc )
        self.training = Training( *exercises )

    def discard_training_and_goto_start_exercising( self ):
        self.training = Training()
        self.ids['exercises_list'].clear_widgets()
        self.parent.current = 'start_exercising'
        
    def save_training_and_goto_start_exercising( self ):
        journal = App.get_running_app().journal
        journal.add_training( self.training )
        self.training = Training()
        self.ids['exercises_list'].clear_widgets()
        self.parent.current = 'start_exercising'


class ExerciseSetsRepsWeightsWidget( GridLayout ):
    def __init__( self, current_training_screen, **kwargs ):
        super( ExerciseSetsRepsWeightsWidget, self ).__init__( **kwargs )
        self.current_training_screen = current_training_screen
        self.exercise_name = kwargs['text']
        self.ids['exercise_name_label'].text = self.exercise_name
        self.add_set_with_reps_weights()
        self.add_set_with_reps_weights()
        self.add_set_with_reps_weights()

    def add_set_with_reps_weights( self ):
        set_layout = GridLayout( rows = 1, spacing = 30 )
        pos_shift = Label( text='' )
        set_layout.add_widget( pos_shift )
        reps = TextInput( hint_text = '10' )
        set_layout.add_widget( reps )
        weights = TextInput( hint_text = '50' )
        set_layout.add_widget( weights )
        reps.bind( text =
                   self.current_training_screen.update_training_from_user_input )
        weights.bind( text =
                      self.current_training_screen.update_training_from_user_input )
        self.ids['sets_reps_weights'].add_widget( set_layout )
        

    def exercise_from_user_input( self ):        
        sets = len( self.ids['sets_reps_weights'].children )
        reps = []
        weights = []
        for reps_weights_set in self.ids['sets_reps_weights'].children:
            reps_input = reps_weights_set.children[1].text            
            weights_input = reps_weights_set.children[0].text
            if reps_input is not None:
                reps.insert( 0, reps_input )
            if weights_input is not None:
                weights.insert( 0, weights_input )
        comment = self.ids['exercise_comment'].text
        exc = ExerciseSetsRepsWeights( name = self.exercise_name,
                                       sets = sets,
                                       reps = reps,
                                       weights = weights,
                                       comment = comment )
        print( exc )
        return( exc )

            
class SelectExerciseScreen( Screen ):
    def post_kv_build( self ):
        for x in list_of_exercises.list_of_exercises:
            btn =  Button(
                text = x.name,
                on_press = self.exercise_button_pressed )
            btn.exercise_type = x.exercise_type
            self.ids.possible_exercises.add_widget( btn )        

        grid_layout = self.ids['possible_exercises']
        grid_layout.bind( minimum_height = grid_layout.setter('height') )

    def exercise_button_pressed( self, button ):
        exercise_name = button.text
        exercise_type = button.exercise_type 
        self.parent.get_screen('training').add_exercise( exercise_name,
                                                         exercise_type )
        self.parent.current = 'training'            



class JournalOverviewScreen( Screen ):
    def post_kv_build( self ):
        tree = self.ids['tree']
        tree.bind( minimum_height = tree.setter('height') )
        self.populate_tree_view()

    def populate_tree_view( self ):
        journal = App.get_running_app().journal
        journal_node = self.ids['tree'].add_node(
            TreeViewLabel( text = 'Journal', is_open = True ) )
        for training in journal.trainings:
            training_node = self.ids['tree'].add_node(
                TreeViewLabel( text = 'Training' ), journal_node )
            for exercise in training.exercises:
                exc_node = self.ids['tree'].add_node(
                    TreeViewLabel(text='Exercise: ' + exercise.description['name']),
                    training_node )
                for essential_field in exercise.essential_fields:
                    label_str = essential_field + \
                                ': ' + str( exercise.description[essential_field] )
                    self.ids['tree'].add_node(
                        TreeViewLabel( text = label_str ), exc_node )

        
# App 
class AppScreenManager( ScreenManager ):    
    pass
        
class ExjApp( App ):
    def __init__( self ):
        App.__init__( self )
        default_journal_file = "default_journal.json"
        if os.path.isfile( default_journal_file ):            
            self.journal = Journal.load_journal( default_journal_file )            
        else:
            self.journal = Journal()
        default_simple_program = twoday_simple_program
        self.simple_program = default_simple_program
    
    def build( self ):
        app_screen_manager = AppScreenManager()
        app_screen_manager.ids['select_exercise'].post_kv_build()
        app_screen_manager.ids['training'].post_kv_build()
        app_screen_manager.ids['journal_overview'].post_kv_build()
        return app_screen_manager


if __name__ == '__main__':
    ExjApp().run()
