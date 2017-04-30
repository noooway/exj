from Exercise import *

class ExerciseSetsRepsWeights( Exercise ):
    def __init__( self, name, sets, reps, weights, **description ):
        super( ExerciseSetsRepsWeights, self ).__init__( type = type(self).__name__,
                                                         name = name,
                                                         sets = sets,
                                                         reps = reps,
                                                         weights = weights,
                                                         **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]

    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} sets, {} reps".format(
            self.description['name'],
            self.description['sets'],
            self.description['reps'] )
