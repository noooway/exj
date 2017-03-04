from SimpleProgram import *
from Training import *
from Exercise import *
from Metric import *

list_of_simple_programs = {}
list_of_simple_programs['novice'] = SimpleProgram(
    'Novice',
    [ Training( ExerciseSetsRepsWeights( 'Pull Ups',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Dips',
                                         sets = 3, reps = 25, weights = 0 ) ),
      Training( ExerciseSetsRepsWeights( 'Squat',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Hyperextenstion',
                                         sets = 3, reps = 25, weights = 0 ) ) ] )

list_of_simple_programs['two_day_split'] = SimpleProgram(
    'Two-day split',
    [ Training( ExerciseSetsRepsWeights( 'Barbell Bench Press',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Standing Military Press',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Push Ups',
                                         sets = 3, reps = 25, weights = 0 ) ),
      Training( ExerciseSetsRepsWeights( 'Leg Press',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Hack Squat',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Deadlift',
                                         sets = 3, reps = 25, weights = 0 ) ) ] )


list_of_simple_programs['current_two_day_split'] = SimpleProgram(
    'Current Two-day split',
    [ Training( ExerciseRunning( 'Warm-up Running',
                                 intervals = 1,
                                 distances = 1.0, times = '4:00' ),
                ExerciseSetsRepsWeights( 'Pull Ups',
                                         sets = 3, reps = 8, weights = 0 ),
                ExerciseSetsRepsWeights( 'Dips',
                                         sets = 3, reps = 8, weights = 0 ),
                ExerciseSetsRepsWeights( 'Leverage Iso Row',
                                         sets = 3, reps = 8, weights = 0 ),
                ExerciseSetsRepsWeights( 'Barbell Bench Press',
                                         sets = 3, reps = 8, weights = 50 ),
                ExerciseSetsRepsWeights( 'T-Bar Row',
                                         sets = 3, reps = 8, weights = 50 ),
                ExerciseSetsRepsWeights( 'Triceps Pushdown',
                                         sets = 3, reps = 8, weights = 50 ),
                ExerciseSetsRepsWeights( 'Hammer Curl',
                                         sets = 3, reps = 8, weights = 50 ),
            ),
      Training( ExerciseRunning( 'Warm-up Running',
                                 intervals = 1,
                                 distances = 1.0, times = '4:00' ),
                ExerciseSetsRepsWeights( 'Leg Press',
                                         sets = 3, reps = 5, weights = 16 ),
                ExerciseSetsRepsWeights( 'Hack Squat',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Calf Raise',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Hyperextenstion',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Romanian Deadlift',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Deadlift',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Decline Crunch',
                                         sets = 3, reps = 25, weights = 0 ),
                ExerciseSetsRepsWeights( 'Hanging Leg Raise',
                                         sets = 3, reps = 25, weights = 0 ) ) ] )
