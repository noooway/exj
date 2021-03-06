import os
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label

from exercises_and_metrics_types import *

class SelectExerciseScreen( Screen ):
    def __init__( self, **kwargs ):
        super( SelectExerciseScreen, self ).__init__( **kwargs )
        dict_of_exercises = self.read_exercises()
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        label = Label( text = 'Select an exercise:', size_hint_y = 0.15 )
        v_layout.add_widget( label )
        exc_grid = GridLayout( cols = 1,
                               spacing = 15,
                               size_hint_y = None )
        for category in sorted( dict_of_exercises.keys() ):
            cat_grid = GridLayout( cols = 1, 
                                   spacing = 15,
                                   row_default_height = 20,
                                   size_hint_y = None )
            cat_grid.bind( minimum_height = cat_grid.setter('height'))
            cat_label = Label( text = category, font_size='25sp', )
            cat_grid.add_widget( cat_label )
            cat_btn_grid = GridLayout( cols = 2,
                                       spacing = 5,
                                       row_default_height = 50,
                                       row_force_default = True,
                                       size_hint_y = None )
            cat_btn_grid.bind(
                minimum_height = cat_btn_grid.setter('height'))
            for x in dict_of_exercises[ category ]:
                btn =  Button( text = x['name'],
                               on_press = self.exercise_button_pressed )
                btn.exercise_type = x['exercise_type']
                cat_btn_grid.add_widget( btn )                
            cat_grid.add_widget( cat_btn_grid )
            exc_grid.add_widget( cat_grid )
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
        exercise_type = button.exercise_type
        ExerciseClass = globals().get( exercise_type )
        if ExerciseClass:
            exc = ExerciseClass.construct_from_name( exercise_name )
            self.parent.get_screen('training').add_exercise( exc )
        else:
            print( 'Unknown excercise type:', exercise_type )            
        self.parent.get_screen('training').back_from_exc_selection = True
        self.parent.current = 'training'
        
    def goto_training( self ):
        self.parent.current = 'training'

    def read_exercises( self ):
        dict_of_exercises = {}
        exercise_folder = "exercises_and_metrics_library"
        for root, dirs, files in os.walk( exercise_folder ):
            for filename in files:
                if filename.endswith( ".json" ):
                    fullpath = os.path.join( root, filename )
                    with open( fullpath, 'rt' ) as infile:
                        dict_from_json = json.load( infile )
                        category = dict_from_json.get('category',
                                                      'Unknown')
                        exercises = dict_from_json.get('exercises', [])
                        #print( category )
                        #print( exercises  )
                        dict_of_exercises.setdefault(
                            category, [] ).extend( exercises )        
        return( dict_of_exercises )

