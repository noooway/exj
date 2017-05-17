import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.graphics import Rectangle, Color

from exercises_and_metrics_types import *


class SpecificExerciseStatisticsScreen( Screen ):
    def __init__( self, **kwargs ):
        super(SpecificExerciseStatisticsScreen, self).__init__(**kwargs)
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        spinner_layout = BoxLayout( orientation = 'horizontal',
                                    spacing = 30,
                                    size_hint_y = 0.2 )
        exercise_spinner_label = Label( text = 'Exercise:' )
        self.exercise_spinner = Spinner()
        self.exercise_spinner.bind( text = self.draw_exercise )
        self.exercise_spinner.ex_names_and_types = {}
        spinner_layout.add_widget( exercise_spinner_label )
        spinner_layout.add_widget( self.exercise_spinner )
        v_layout.add_widget( spinner_layout )
        #
        drawing_layout = RelativeLayout()
        #drawing_layout = ScatterLayout()
        self.drawing_widget = Widget()
        drawing_layout.add_widget( self.drawing_widget )
        self.drawing_widget.canvas.add( Color( 1, 1, 1) )
        self.drawing_widget.bg_rect = Rectangle(
            pos = (0, 0),
            size = ( self.drawing_widget.width,
                     self.drawing_widget.height ) )
        self.drawing_widget.canvas.add( self.drawing_widget.bg_rect )
        self.drawing_widget.bind( size = self.drawing_widget_update_rect )
        v_layout.add_widget( drawing_layout )
        #
        back_button = Button( text = 'Back', size_hint_y = 0.2 )
        back_button.on_press = self.goto_view_progress
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )

    def goto_view_progress( self ):
        self.parent.current = 'view_progress'

    def drawing_widget_update_rect(self, *args):
        #self.drawing_widget.bg_rect.pos = self.drawing_widget.pos
        self.drawing_widget.bg_rect.size = self.drawing_widget.size

    def on_pre_enter( self ):
        self.populate_spinner_with_exercises()

    def populate_spinner_with_exercises( self ):
        self.exercise_spinner.text = 'Select Exercise'
        journal = App.get_running_app().journal
        ex_names_and_types = \
            journal.get_dict_of_exercise_names_and_types()
        ex_names = [ k for (k,v) in ex_names_and_types.items() ]
        self.exercise_spinner.values = ex_names
        self.exercise_spinner.ex_names_and_types = ex_names_and_types
    
    def draw_exercise( self, *rest ):        
        ex_name = self.exercise_spinner.text
        ex_type = self.exercise_spinner.ex_names_and_types.get( ex_name )
        ExClass = globals().get( ex_type )
        if ExClass:
            journal = App.get_running_app().journal
            drawing_instructions = \
                    ExClass.gen_drawing_instructions(
                        ex_name, journal,
                        self.drawing_widget.bg_rect.size )
            self.drawing_widget.canvas.clear()
            self.drawing_widget.canvas.add( self.drawing_widget.bg_rect )
            self.drawing_widget.canvas.add( drawing_instructions ) 
