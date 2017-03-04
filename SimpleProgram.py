import random

class SimpleProgram( object ):
    """Simple program doesn't have a specific goal."""

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
