from Exercise import *

class ExerciseSetsRepsWeights( Exercise ):
    def __init__( self, name, sets, reps, weights, description_dict ):
        super( ExerciseSetsRepsWeights, self ).__init__( description_dict )
        self.update( {
            'type': type(self).__name__, # type: str
            'name': name, # type: str
            'sets': sets, # type: int
            'reps': reps, # type: List[ int ]
            'weights': weights # type: List[ float ]
        } )                    
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]

    @classmethod
    def construct_from_name( cls, exercise_name ):
        sets = 3
        reps = [ '10', '10', '10' ]
        weights = [ '30', '50', '50' ]
        exercise = cls( exercise_name, sets, reps, weights, {} )
        return exercise
        
    @classmethod
    def init_from_json( cls, dict_from_json ):
        name = dict_from_json.pop( 'name' )
        sets = dict_from_json.pop( 'sets' )
        reps = dict_from_json.pop( 'reps' )
        weights = dict_from_json.pop( 'weights' )
        exercise = cls( name, sets, reps, weights, dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} sets, {} reps".format(
            self.description['name'],
            self.description['sets'],
            self.description['reps'] )
