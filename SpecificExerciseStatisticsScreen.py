import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

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
        self.drawing_layout = RelativeLayout()
        v_layout.add_widget( self.drawing_layout )
        #
        back_button = Button( text = 'Back', size_hint_y = 0.2 )
        back_button.on_press = self.goto_view_progress
        v_layout.add_widget( back_button )
        self.add_widget( v_layout )

    def goto_view_progress( self ):
        self.parent.current = 'view_progress'

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
        if ex_type:
            ex_statistics_widget = ex_type + "StatisticsWidget"
            ExStatWidgetClass = globals().get( ex_statistics_widget )
            if ExStatWidgetClass:
                journal = App.get_running_app().journal
                self.drawing_layout.clear_widgets()
                self.drawing_layout.add_widget(
                    ExStatWidgetClass( ex_name, journal ) )
