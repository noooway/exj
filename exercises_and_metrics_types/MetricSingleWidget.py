from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from MetricSingle import *

class MetricSingleWidget( GridLayout ):
    def __init__( self, current_training_screen, **kwargs ):
        super( MetricSingleWidget, self ).__init__( **kwargs )
        self.cols = 1
        self.spacing = 1
        self.row_default_height = 40
        self.row_force_default = True
        self.size_hint_y = None
        self.bind( minimum_height = self.setter('height') )
        self.metric_name = kwargs['text']
        input_layout = BoxLayout( orientation = 'horizontal',
                                  spacing = 30 )
        metric_label = Label( text = self.metric_name )
        input_layout.add_widget( metric_label )
        self.value_input = TextInput( hint_text = "" )
        self.value_input.bind(
            text = current_training_screen.update_training_from_user_input )
        input_layout.add_widget( self.value_input )
        del_metric_btn = Button( text = "Del Metr", size_hint_x = 0.3 )
        del_metric_btn.on_press = \
            lambda: current_training_screen.remove_exercise( self )
        input_layout.add_widget( del_metric_btn )
        self.add_widget( input_layout )
        self.comment = TextInput( hint_text = 'Comment Metric' )
        self.comment.bind(
            text = current_training_screen.update_training_from_user_input )
        self.add_widget( self.comment )

    def exercise_from_user_input( self ):
        value_input = self.value_input.text
        comment = self.comment.text
        metric = MetricSingle( name = self.metric_name,
                               value = value_input,
                               comment = comment )
        return( metric )
