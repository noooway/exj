class Exercise( object ):
    """Exercise description"""    
    def __init__( self, **description ):
        self.description = description
        self.essential_fields = None

    def __repr__( self ):
        return repr( self.description )

    def __str__( self ):
        return str( self.description )

    def update( self, **description ):
        self.description.update( description )

    def repr_for_json_dump( self ):
        return( self.description )

    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise

    
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
