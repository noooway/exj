import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.graphics import *

#from Journal import *

class SpecificExerciseStatisticsScreen( Screen ):
    def __init__( self, **kwargs ):
        super(SpecificExerciseStatisticsScreen, self).__init__(**kwargs)
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        spinner_layout = BoxLayout( orientation = 'horizontal',
                                    spacing = 30 )
        exercise_spinner_label = Label( text = 'Exercise:' )
        exercise_spinner = Spinner(
            text='Home',
            values=('Home', 'Work', 'Other', 'Custom') )
        spinner_layout.add_widget( exercise_spinner_label )
        spinner_layout.add_widget( exercise_spinner )
        v_layout.add_widget( spinner_layout )
        #
        drawing_layout = RelativeLayout()
        drawing_widget = Widget()
        drawing_layout.add_widget( drawing_widget )
        drawing_widget.canvas.add( Color( 1, 0, 0) )
        print( drawing_layout.size )
        drawing_widget.canvas.add( Rectangle(pos=drawing_widget.pos,
                                             size=drawing_widget.size ) )
        v_layout.add_widget( drawing_layout )
        #
        back_button = Button( text = 'Back' )
        back_button.on_press = self.goto_view_progress
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )

    def goto_view_progress( self ):
        self.parent.current = 'view_progress'
