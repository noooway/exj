from Training import *
from Exercise import *
from Journal import *
import random

class SimpleProgram( object ):
    """Simple program doesn't have aim."""

    def __init__( self, name, trainings ):
        self.program_type = 'simple_program'
        self.name = name
        self.trainings = list( trainings )
                
    def advise_current_training( self, journal ):
        # inspects the last training.
        # if an overlap with any of the training days is big enough
        # then suggests the next day in the program.
        # if overlap is not found, suggest the first day.
        # not necessary for now.
        return random.choice( self.trainings )

    def __repr__( self ):
        return "Simple program: " +  repr( self.name ) + "\n" + \
            "\t" + repr( self.trainings ) + "\n" 

    def __str__( self ):
        return "Simple program: " + str( self.name) + "\n" + \
            "\t" + str( self.trainings ) + "\n"

    

novice_simple_program = SimpleProgram(
    'novice',
    [ Training( ExerciseSetsRepsWeights( 'Pull Ups',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Push Ups',
                                         sets = 3, reps = 25, weights = 0 ) ) ] )

twoday_simple_program = SimpleProgram(
    'two-day-split',
    [ Training( ExerciseSetsRepsWeights( 'Leg Press',
                                         sets = 3, reps = 5, weights = 25 ),
                ExerciseSetsRepsWeights( 'Hack Squat',
                                         sets = 3, reps = 10, weights = 10 ) ),
      Training( ExerciseSetsRepsWeights( 'Barbell Bench Press',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Pull Ups',
                                         sets = 3, reps = 25, weights = 0 ) ) ] )
