import os
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

class SelectExerciseScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SelectExerciseScreen, self ).__init__( **kwargs )
        list_of_exercises = self.read_exercises()
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        label = Label( text = 'Select an exercise:', size_hint_y = 0.2 )
        v_layout.add_widget( label )
        exc_grid = GridLayout( cols = 3,
                               spacing = 5,
                               row_default_height = 70,
                               row_force_default = True,
                               size_hint_y = None )
        for x in list_of_exercises:
            btn =  Button( text = x['name'],
                           on_press = self.exercise_button_pressed )
            btn.exercise_widget_type = x['exercise_type'] + "Widget"
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
        self.parent.get_screen('training').add_exercise(
            exercise_name,
            exercise_widget_type )
        self.parent.get_screen('training').back_from_exc_selection = True
        self.parent.current = 'training'
        
    def goto_training( self ):
        self.parent.current = 'training'

    def read_exercises( self ):
        list_of_exercises = []
        exercise_folder = "exercises"
        for root, dirs, files in os.walk( exercise_folder ):
            for filename in files:
                if filename.endswith( ".json" ):
                    fullpath = os.path.join( root, filename )
                    with open( fullpath, 'rt' ) as infile:
                        dict_from_json = json.load( infile )
                        list_of_exercises.extend( dict_from_json )
        print( list_of_exercises )
        return( list_of_exercises )

