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
        
### Bars
class PullUps( Exercise ):
    """Pull-up exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( PullUps, self ).__init__( name = "pull-ups",
                                         sets = sets,
                                         reps = reps,
                                         weights = weights,
                                         **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]

class Dips( Exercise ):
    """Dips exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( Dips, self ).__init__( name = "dips",
                                      sets = sets,
                                      reps = reps,
                                      weights = weights,
                                      **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]
        

class PushUps( Exercise ):
    """Push-up exercise"""
    
    def __init__( self, sets, reps, **description ):
        super( PushUps, self ).__init__( name = "push-ups",
                                         sets = sets,
                                         reps = reps,
                                         **description )
        self.essential_fields = ['name', 'sets', 'reps' ]


### Running
        
class DistanceRunning( Exercise ):
    """Fixed distance running"""
    
    def __init__( self, distance, time, **description ):
        super( DistanceRunning, self ).__init__( name = "distance running",
                                                 distance = distance,
                                                 time = time,
                                                 **description )
        self.essential_fields = ['name', 'distance', 'time' ]


class IntervalRunning( Exercise ):
    """Interval running"""
    
    def __init__( self, reps, run_time, rest_time, **description ):
        super( IntervalRunning, self ).__init__( name = "interval running",
                                                 reps = reps,
                                                 run_time = run_time,
                                                 rest_time = rest_time,
                                                 **description )
        self.essential_fields = ['name', 'reps', 'run_time', 'rest_time' ]


### Iron

class LegPress( Exercise ):
    """Leg Press exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( LegPress, self ).__init__( name = "leg-press",
                                          sets = sets,
                                          reps = reps,
                                          weights = weights,
                                          **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]


class HackSquat( Exercise ):
    """Hack Squat exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( HackSquat, self ).__init__( name = "hack-squat",
                                           sets = sets,
                                           reps = reps,
                                           weights = weights,
                                           **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]


class CalfRaise( Exercise ):
    """Calf Raise exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( CalfRaise, self ).__init__( name = "calf-raise",
                                           sets = sets,
                                           reps = reps,
                                           weights = weights,
                                           **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]



class Deadlift( Exercise ):
    """Deadlift exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( Deadlift, self ).__init__( name = "deadlift",
                                          sets = sets,
                                          reps = reps,
                                          weights = weights,
                                          **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]


class RomanianDeadlift( Exercise ):
    """Romanian Deadlift exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( RomanianDeadlift, self ).__init__( name = "romanian_deadlift",
                                                  sets = sets,
                                                  reps = reps,
                                                  weights = weights,
                                                  **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]


class BarbellSquat( Exercise ):
    """Barbell Squat exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( BarbellSquat, self ).__init__( name = "barbell_squat",
                                              sets = sets,
                                              reps = reps,
                                              weights = weights,
                                              **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]



class LyingLegCurl( Exercise ):
    """Lying Leg Curl exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( LyingLegCurl, self ).__init__( name = "lying_leg_curl",
                                              sets = sets,
                                              reps = reps,
                                              weights = weights,
                                              **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]


class LegExtension( Exercise ):
    """Leg Extension exercise"""
    
    def __init__( self, sets, reps, weights = 0, **description ):
        super( LegExtension, self ).__init__( name = "leg_extension",
                                              sets = sets,
                                              reps = reps,
                                              weights = weights,
                                              **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]
