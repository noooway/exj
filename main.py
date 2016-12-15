import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel

from Journal import *
from Training import *
from Exercise import *
from SimpleProgram import *
import list_of_exercises

# Declare screens
class MenuScreen( Screen ):
    def __init__( self, **kwargs ):
        super( MenuScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        start_exercising_button = Button( text = 'Start exercising' )
        start_exercising_button.on_press = self.goto_start_exercising
        v_layout.add_widget( start_exercising_button )
        compose_training_plan_button = Button( text = 'Compose training plan' )
        compose_training_plan_button.on_press = self.goto_compose_training_plan
        v_layout.add_widget( compose_training_plan_button )
        view_progress_button = Button( text = 'View progress' )
        view_progress_button.on_press = self.goto_view_progress
        v_layout.add_widget( view_progress_button )
        quit_button = Button( text = 'Quit' )
        quit_button.on_press = self.save_journal_and_quit
        v_layout.add_widget( quit_button )
        self.add_widget( v_layout )

    def goto_start_exercising( self ):
        self.parent.current = 'start_exercising'

    def goto_compose_training_plan( self ):
        self.parent.current = 'compose_training_plan'

    def goto_view_progress( self ):
        self.parent.current = 'view_progress'

    def save_journal_and_quit( self ):
        app = App.get_running_app()
        app.journal.save_journal("default_journal.json")
        app.stop()

class StartExercisingScreen( Screen ):
    def __init__( self, **kwargs ):
        super( StartExercisingScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        follow_plan_button = Button( text = 'Follow the plan' )
        follow_plan_button.on_press = self.generate_and_goto_training
        v_layout.add_widget( follow_plan_button )
        unplanned_training_button = Button( text = 'Unplanned training' )
        unplanned_training_button.on_press = self.goto_training
        v_layout.add_widget( unplanned_training_button )
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def generate_and_goto_training( self ):
        journal = App.get_running_app().journal
        current_program = App.get_running_app().simple_program
        training = current_program.advise_current_training( journal )
        for ex in training.exercises:
            self.parent.get_screen('training').add_exercise(
                ex.description['name'],
                ex.description['type'] + 'Widget' )
        self.parent.current = 'training'

    def goto_training( self ):
        self.parent.current = 'training'

    def goto_menu( self ):
        self.parent.current = 'menu'

            

class ComposeTrainingPlanScreen( Screen ):
    def __init__( self, **kwargs ):
        super( ComposeTrainingPlanScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        simple_programs_button = Button( text = 'Simple programs' )
        simple_programs_button.on_press = self.goto_simple_program_selection
        v_layout.add_widget( simple_programs_button )
        specific_goal_programs_button = Button(
            text = 'Programs for specific goal (not implemented)' )
        v_layout.add_widget( specific_goal_programs_button )
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def goto_menu( self ):
        self.parent.current = 'menu'

    def goto_simple_program_selection( self ):
        self.parent.current = 'simple_program_selection'

class ViewProgressScreen( Screen ):
    def __init__( self, **kwargs ):
        super( ViewProgressScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        progress_label = Label( text = 'Program progress (not implemented)' )
        v_layout.add_widget( progress_label )
        metrics_label = Label( text = 'Metrics (not implemented)' )
        v_layout.add_widget( metrics_label )
        journal_overview_button = Button( text = 'Journal overview' )
        journal_overview_button.on_press = self.goto_journal_overview
        v_layout.add_widget( journal_overview_button )        
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def goto_journal_overview( self ):
        self.parent.current = 'journal_overview'
        
    def goto_menu( self ):
        self.parent.current = 'menu'
        
class TrainingScreen( Screen ):    
    def __init__( self, **kwargs ):
        super( TrainingScreen, self ).__init__( **kwargs )
        self.excercise_widgets = []
        self.training = Training()
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        label = Label( text = 'List of exercises',
                       size_hint = (1.0, 0.3) )
        v_layout.add_widget( label )
        self.exercises_layout = GridLayout(
            cols = 1,
            spacing = 5,
            row_default_height = 200,
            row_force_default = True,
            size_hint_y = None )
        self.exercises_layout.bind( minimum_height =
                                    self.exercises_layout.setter('height') )
        self.scroll_for_exercises = ScrollView()                
        self.scroll_for_exercises.add_widget( self.exercises_layout )
        v_layout.add_widget( self.scroll_for_exercises )
        add_exc_layout = BoxLayout( orientation = 'horizontal',
                                    spacing = 30,
                                    size_hint = ( 1.0, 0.2 ) )
        add_exc_button = Button( text = 'Add exercise' )
        add_exc_button.on_press = self.goto_select_exercise
        add_exc_layout.add_widget( add_exc_button )
        v_layout.add_widget( add_exc_layout )
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
        self.training = Training( *exercises )
        
    def goto_select_exercise( self ):
        self.parent.current = 'select_exercise'
        
    def goto_start_exercising( self ):
        self.training = Training()
        self.exercises_layout.clear_widgets()
        self.parent.current = 'start_exercising'

    def save_training_and_goto_start_exercising( self ):
        journal = App.get_running_app().journal
        journal.add_training( self.training )
        self.training = Training()
        self.exercises_layout.clear_widgets()
        self.parent.current = 'start_exercising'

        
class SelectExerciseScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SelectExerciseScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        label = Label( text = 'Select an exercise:', size_hint_y = 0.2 )
        v_layout.add_widget( label )
        exc_grid = GridLayout( cols = 2,
                               spacing = 5,
                               row_default_height = 70,
                               row_force_default = True,
                               size_hint_y = None )
        for x in list_of_exercises.list_of_exercises:
            btn =  Button( text = x.name,
                           on_press = self.exercise_button_pressed )
            btn.exercise_widget_type = x.exercise_widget_type
            exc_grid.add_widget( btn )
            
        exc_grid.bind( minimum_height = exc_grid.setter('height') )
        scroll_for_exercises = ScrollView()
        scroll_for_exercises.add_widget( exc_grid )
        v_layout.add_widget( scroll_for_exercises )
        back_button = Button( text = 'Back', size_hint_y = 0.2 )
        back_button.on_press = self.goto_training
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )

    def exercise_button_pressed( self, button ):
        exercise_name = button.text
        exercise_widget_type = button.exercise_widget_type 
        self.parent.get_screen('training').add_exercise( exercise_name,
                                                         exercise_widget_type )
        self.parent.current = 'training'
        
    def goto_training( self ):
        self.parent.current = 'training'

        
class ExerciseWidget( BoxLayout ):
    def __init__( self, **kwargs ):
        super( ExerciseWidget, self ).__init__( **kwargs )
        self.orientation = 'vertical'
        self.spacing = 1
        excercise_label = Label( text = kwargs['text'] )
        self.add_widget( excercise_label )
        results = TextInput( text = 'Enter Results' )
        self.add_widget( results )
        comment = TextInput( text = 'Enter Comment' )
        self.add_widget( comment )    

        
class ExerciseSetsRepsWeightsWidget( GridLayout ):
    def __init__( self, current_training_screen, **kwargs ):
        super( ExerciseSetsRepsWeightsWidget, self ).__init__( **kwargs )
        self.cols = 1
        self.spacing = 1
        self.exercise_name = kwargs['text']
        title_layout = BoxLayout( orientation = 'horizontal',
                                  spacing = 30 )
        excercise_label = Label( text = self.exercise_name )
        title_layout.add_widget( excercise_label )
        title_layout.add_widget( Label( text = "Reps" ) )
        title_layout.add_widget( Label( text = "Weights" ) )
        self.add_widget( title_layout )
        self.add_reps_weights_set( current_training_screen )
        self.add_reps_weights_set( current_training_screen )
        self.add_reps_weights_set( current_training_screen )
        add_set_layout = BoxLayout( orientation = 'horizontal',
                                    spacing = 30 )
        add_set_layout.add_widget( Label(
            text='',
            size_hint = (0.30, 1.0) ) )
        add_set_layout.add_widget( Button(
            text = 'Add set',
            size_hint = (0.66, 1.0),
            on_press = lambda x: self.add_reps_weights_set(
                current_training_screen, index_in_layout = 2 ) ) )
        self.add_widget( add_set_layout ) 
        self.comment = TextInput( hint_text = 'Comment Exercise' )
        self.comment.bind( text =
                           current_training_screen.update_training_from_user_input )
        self.add_widget( self.comment )

    def add_reps_weights_set( self,
                              current_training_screen,
                              index_in_layout = 0 ):
        set_layout = GridLayout( rows = 1,
                                 spacing = 30 )
        pos_shift = Label( text='' )
        set_layout.add_widget( pos_shift )
        reps = TextInput( hint_text = '10' )
        set_layout.add_widget( reps )
        weights = TextInput( hint_text = '50' )
        set_layout.add_widget( weights )
        reps.bind( text =
                   current_training_screen.update_training_from_user_input )
        weights.bind( text =
                      current_training_screen.update_training_from_user_input )        
        self.add_widget( set_layout, index = index_in_layout )

    def exercise_from_user_input( self ):
        sets = len( self.children[2:-1] )
        reps = []
        weights = []
        for reps_weights_set in self.children[2:-1]:
            reps_input = reps_weights_set.children[1].text            
            weights_input = reps_weights_set.children[0].text
            if reps_input is not None:
                reps.insert( 0, reps_input )
            if weights_input is not None:
                weights.insert( 0, weights_input )
        comment = self.comment.text
        exc = ExerciseSetsRepsWeights( name = self.exercise_name,
                                       sets = sets,
                                       reps = reps,
                                       weights = weights,
                                       comment = comment )
        return( exc )
        

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
        self.populate_tree_view()
        scroll = ScrollView( pos = (0, 0) )
        scroll.add_widget( self.tree_view )    
        v_layout.add_widget( scroll )
        back_to_progress_button = Button( text = 'Back',
                                          size_hint_y = 0.2 )
        back_to_progress_button.on_press = self.goto_progress
        v_layout.add_widget( back_to_progress_button )
        self.add_widget( v_layout )

    def populate_tree_view( self ):
        journal = App.get_running_app().journal
        journal_node = self.tree_view.add_node(
            TreeViewLabel( text = 'Journal', is_open = True ) )
        for training in journal.trainings:
            training_node = self.tree_view.add_node(
                TreeViewLabel( text = 'Training' ), journal_node )
            for exercise in training.exercises:
                exc_node = self.tree_view.add_node(
                    TreeViewLabel(text='Exercise: ' + exercise.description['name']),
                    training_node )
                for essential_field in exercise.essential_fields:
                    label_str = essential_field + \
                                ': ' + str( exercise.description[essential_field] )
                    self.tree_view.add_node(
                        TreeViewLabel( text = label_str ), exc_node )
        
    def goto_progress( self ):
        self.parent.current = 'view_progress'


class SimpleProgramsScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SimpleProgramsScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        beginners_program = Button( text = 'Beginners',
                                    on_press = self.goto_program_content )
        v_layout.add_widget( beginners_program )
        two_day_split_program = Button( text = '2 day split',
                                        on_press = self.goto_program_content )
        v_layout.add_widget( two_day_split_program )
        create_custom_program = Button( text = 'Create custom program (not implemented)' )
        v_layout.add_widget( create_custom_program )
        back_button = Button( text = 'Back' )
        back_button.on_press = self.goto_programs_screen
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )

    def goto_programs_screen( self ):
        self.parent.current = 'compose_training_plan'

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
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        program_content_header = Label( text = 'Days and Exercises:' )
        v_layout.add_widget( program_content_header )
        self.program_content = Label( text = str( self.selected_simple_program ) )
        v_layout.add_widget( self.program_content )
        back_layout = BoxLayout( orientation = 'horizontal',
                                 spacing = 30,
                                 size_hint = ( 1.0, 0.2 ) )
        set_as_current_program_button = Button( text = 'Set as current program' )
        set_as_current_program_button.on_press = self.set_and_go_to_menu
        back_layout.add_widget( set_as_current_program_button )
        discard_button = Button( text = 'Discard' )
        discard_button.on_press = self.go_back
        back_layout.add_widget( discard_button )
        v_layout.add_widget( back_layout )
        self.add_widget( v_layout )

    def update_selected_program( self, simple_program ):
        self.selected_simple_program = simple_program
        self.program_content.text = str( self.selected_simple_program )

    def set_and_go_to_menu( self ):
        App.get_running_app().simple_program = self.selected_simple_program
        self.parent.current = 'menu'
        
    def go_back( self ):
        self.parent.current = 'simple_program_selection'

        
        
# Create the screen manager
class TestApp(App):
    def __init__(self):
        App.__init__( self )
        default_journal_file = "default_journal.json"
        default_simple_program = twoday_simple_program
        if os.path.isfile( default_journal_file ):            
            self.journal = Journal.load_journal( default_journal_file )            
        else:
            self.journal = Journal()
        self.simple_program = default_simple_program
            
            
    def build(self):
        sm = ScreenManager()
        sm.add_widget( MenuScreen( name='menu' ) )
        sm.add_widget( StartExercisingScreen( name='start_exercising') )
        sm.add_widget( ComposeTrainingPlanScreen( name='compose_training_plan') )
        sm.add_widget( SimpleProgramsScreen( name='simple_program_selection') )
        sm.add_widget( SimpleProgramContentScreen( name='simple_program_content') )
        sm.add_widget( ViewProgressScreen( name='view_progress') )
        sm.add_widget( TrainingScreen( name='training') )
        sm.add_widget( SelectExerciseScreen( name='select_exercise') )
        sm.add_widget( JournalOverviewScreen( name='journal_overview') )
        return sm

if __name__ == '__main__':
    ta = TestApp()
    ta.run()
