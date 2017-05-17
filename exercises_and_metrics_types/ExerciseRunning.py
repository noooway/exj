from Exercise import *

from kivy.graphics import *
from kivy.core.text import Label as CoreLabel
#https://groups.google.com/forum/#!topic/kivy-users/zRCjfhBcX4c

class ExerciseRunning( Exercise ):
    def __init__( self, name, intervals, distances, times, **description ):
        super( ExerciseRunning, self ).__init__(
            type = type(self).__name__,
            name = name,
            intervals = intervals,
            distances = distances,
            times = times,
            **description )
        self.essential_fields = ['name', 'intervals',
                                 'distances', 'times' ]
        

    @classmethod
    def construct_from_name( cls, exercise_name ):
        intervals = 1
        distances = ['1.0']
        times = ['4:00']
        exercise = cls( exercise_name, intervals,
                        distances, times )
        return exercise

    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} intervals with distances {}".format(
            self.description['name'],
            self.description['intervals'],
            self.description['distances'] )


    @classmethod
    def gen_drawing_instructions( cls, ex_name, journal, rect_size ):
        plot = InstructionGroup()
        plot.add( Color( 1, 0, 1) )
        plot.add( Rectangle( pos = (0, 0), size = rect_size ) )
        text_label = CoreLabel( text="go to hell",
                                font_size=25, color=(0, 0, 0, 1))
        text_label.refresh()
        texture = text_label.texture
        texture_size = list( texture.size )
        plot.add( Rectangle(texture=texture, size=texture_size, pos=(0,0)))
        return plot
