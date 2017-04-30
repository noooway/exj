from Exercise import *

class ExerciseRunning( Exercise ):
    def __init__( self, name, intervals, distances, times, **description ):
        super( ExerciseRunning, self ).__init__( type = type(self).__name__,
                                                 name = name,
                                                 intervals = intervals,
                                                 distances = distances,
                                                 times = times,
                                                 **description )
        self.essential_fields = ['name', 'intervals', 'distances', 'times' ]
        
    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} intervals with distances {}".format(
            self.description['name'],
            self.description['intervals'],
            self.description['distances'] )
