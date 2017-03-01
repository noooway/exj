from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Exercise import *

class ExerciseRunningWidget( GridLayout ):
    def __init__( self, current_training_screen, **kwargs ):
        super( ExerciseRunningWidget, self ).__init__( **kwargs )
        self.cols = 1
        self.spacing = 1
        self.row_default_height = 40
        self.row_force_default = True
        self.size_hint_y = None
        self.bind( minimum_height = self.setter('height') )
        self.exercise_name = kwargs['text']
        title_layout = BoxLayout( orientation = 'horizontal',
                                  spacing = 30 )
        excercise_label = Label( text = self.exercise_name )
        title_layout.add_widget( excercise_label )
        title_layout.add_widget( Label( text = "Distance (km)" ) )
        title_layout.add_widget( Label( text = "Time" ) )
        del_excercise_btn = Button( text = "Del Exc", size_hint_x = 0.3 )
        del_excercise_btn.on_press = \
            lambda: current_training_screen.remove_exercise( self )
        title_layout.add_widget( del_excercise_btn )
        self.add_widget( title_layout )
        self.add_dist_time_interval( current_training_screen )
        add_interval_btn_layout = BoxLayout( orientation = 'horizontal',
                                             spacing = 30 )
        add_interval_btn_layout.add_widget( Label(
            text='',
            size_hint = (0.30, 1.0) ) )
        add_interval_btn_layout.add_widget( Button(
            text = 'Add interval',
            size_hint = (0.775, 1.0),
            on_press = lambda x: self.add_dist_time_interval(
                current_training_screen, index_in_layout = 2 ) ) )
        self.add_widget( add_interval_btn_layout ) 
        self.comment = TextInput( hint_text = 'Comment Exercise' )
        self.comment.bind( text =
                           current_training_screen.update_training_from_user_input )
        self.add_widget( self.comment )

    def add_dist_time_interval( self, current_training_screen, index_in_layout = 0 ):
        interval_layout = GridLayout( rows = 1, spacing = 30 )
        interval_layout.height = 30
        pos_shift = Label( text='' )
        interval_layout.add_widget( pos_shift )
        distance = TextInput( hint_text = '1.0' )
        interval_layout.add_widget( distance )
        time = TextInput( hint_text = '3:40' )
        interval_layout.add_widget( time )        
        distance.bind( text =
                       current_training_screen.update_training_from_user_input )
        time.bind( text =
                   current_training_screen.update_training_from_user_input )
        del_button = Button( text = "Del Int", size_hint_x = 0.3 )
        del_button.on_press = lambda: self.remove_interval_widget(
            current_training_screen, interval_layout )
        interval_layout.add_widget( del_button )
        self.add_widget( interval_layout, index = index_in_layout )

    def exercise_from_user_input( self ):
        intervals = len( self.children[2:-1] )
        distances = []
        times = []
        for dist_time_interval in self.children[2:-1]:
            dist_input = dist_time_interval.children[2].text            
            time_input = dist_time_interval.children[1].text
            if dist_input is not None:
                distances.insert( 0, dist_input )
            if time_input is not None:
                times.insert( 0, time_input )
        comment = self.comment.text
        exc = ExerciseRunning( name = self.exercise_name,
                               intervals = intervals, 
                               distances = distances,
                               times = times,
                               comment = comment )
        return( exc )

    def remove_interval_widget( self, current_training_screen, interval_layout ):
        self.remove_widget( interval_layout )
        current_training_screen.update_training_from_user_input()
        print( 'deleting' )
