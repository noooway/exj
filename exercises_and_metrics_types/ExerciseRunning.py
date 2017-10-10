from Exercise import *

class ExerciseRunning( Exercise ):
    def __init__( self, name, intervals, distances, times, description_dict ):
        super( ExerciseRunning, self ).__init__( description_dict )
        self.update( {
            'type': type(self).__name__, # type: str
            'name': name, # type: str
            'intervals': intervals, # type: int
            'distances': distances, # type: List[float]
            'times': times # List[str] ; todo: change str to time type
        } )        
        self.essential_fields = ['name', 'intervals',
                                 'distances', 'times' ]
        

    @classmethod
    def construct_from_name( cls, exercise_name ):
        intervals = 1
        distances = ['1.0']
        times = ['4:00']
        exercise = cls( exercise_name, intervals,
                        distances, times, {} )
        return exercise

    @classmethod
    def init_from_json( cls, dict_from_json ):
        name = dict_from_json.pop('name')
        intervals = dict_from_json.pop('intervals')
        distances = dict_from_json.pop('distances')
        times = dict_from_json.pop('times')
        exercise = cls( name, intervals, distances, times, dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} intervals with distances {}".format(
            self.description['name'],
            self.description['intervals'],
            self.description['distances'] )
