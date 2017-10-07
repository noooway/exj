from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from ExerciseSetsRepsWeights import *

class ExerciseSetsRepsWeightsInputWidget( GridLayout ):
    def __init__( self, exercise_sets_reps_weights,
                  current_training_screen, **kwargs ):
        super( ExerciseSetsRepsWeightsInputWidget, self ).__init__( **kwargs )
        self.cols = 1
        self.spacing = 1
        self.row_default_height = 40
        self.row_force_default = True
        self.size_hint_y = None
        self.bind( minimum_height = self.setter('height') )
        self.exercise_name = \
            exercise_sets_reps_weights.description['name']
        title_layout = BoxLayout( orientation = 'horizontal',
                                  spacing = 30 )
        excercise_label = Label( text = self.exercise_name )
        title_layout.add_widget( excercise_label )
        title_layout.add_widget( Label( text = "Reps" ) )
        title_layout.add_widget( Label( text = "Weights" ) )
        del_excercise_btn = Button( text = "Del Exc", size_hint_x = 0.3 )
        del_excercise_btn.on_press = \
            lambda: current_training_screen.remove_exercise( self )
        title_layout.add_widget( del_excercise_btn )
        self.add_widget( title_layout )
        self.add_reps_weights_sets_from_exercise(
            exercise_sets_reps_weights, current_training_screen )
        add_set_layout = BoxLayout( orientation = 'horizontal',
                                    spacing = 30 )
        add_set_layout.add_widget( Label(
            text='',
            size_hint = (0.30, 1.0) ) )
        add_set_layout.add_widget( Button(
            text = 'Add set',
            size_hint = (0.775, 1.0),
            on_press = lambda x: self.add_reps_weights_set(
                current_training_screen, index_in_layout = 2 ) ) )
        self.add_widget( add_set_layout )
        comment_text = \
            exercise_sets_reps_weights.description.get(
                'comment',
                'Comment Exercise')
        self.comment = TextInput( hint_text = comment_text )
        self.comment.bind(
            text =
            current_training_screen.update_training_from_user_input )
        self.add_widget( self.comment )

    def add_reps_weights_sets_from_exercise( self, 
            exercise_sets_reps_weights, current_training_screen ):
        # print( '===', 'reps',
        #        exercise_sets_reps_weights.description['reps'],
        #        'weigh',
        #        exercise_sets_reps_weights.description['weights'] )
        for (reps, weights) in zip(
                exercise_sets_reps_weights.description['reps'],
                exercise_sets_reps_weights.description['weights'] ):
            self.add_reps_weights_set( current_training_screen,
                                       reps, weights )

    def add_reps_weights_set( self,
                              current_training_screen,
                              hint_reps = '10',
                              hint_weights = '50',
                              index_in_layout = 0 ):
        set_layout = GridLayout( rows = 1, spacing = 30 )
        set_layout.height = 30
        pos_shift = Label( text='' )
        set_layout.add_widget( pos_shift )
        reps = TextInput( hint_text = str( hint_reps ) )
        set_layout.add_widget( reps )
        weights = TextInput( hint_text = str( hint_weights ) )
        set_layout.add_widget( weights )        
        reps.bind(
            text =
            current_training_screen.update_training_from_user_input )
        weights.bind(
            text =
            current_training_screen.update_training_from_user_input )
        del_button = Button( text = "Del Set", size_hint_x = 0.3 )
        del_button.on_press = lambda: self.remove_set_widget(
            current_training_screen, set_layout )
        set_layout.add_widget( del_button )
        self.add_widget( set_layout, index = index_in_layout )

    def exercise_from_user_input( self ):
        # todo: add input check
        sets = len( self.children[2:-1] )
        reps = []
        weights = []
        for reps_weights_set in self.children[2:-1]:
            reps_input = reps_weights_set.children[2].text            
            weights_input = reps_weights_set.children[1].text
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

    def remove_set_widget( self, current_training_screen, set_layout ):
        self.remove_widget( set_layout )
        current_training_screen.update_training_from_user_input()
        print( 'deleting' )
