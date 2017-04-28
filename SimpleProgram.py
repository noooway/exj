import json
from Training import *

class SimpleProgram( object ):
    """A simple program is a collection of trainings.
       In that sense, it is similar to Journal. 
       Simple programs do not have any specific goals, 
       so they store only a sequence of trainings.
       There is no way to advise on the numbers for the next training."""

    def __init__( self, name, *trainings, **program_description ):
        self.program_type = 'simple_program'
        self.description = {}
        self.description["name"] = name
        self.trainings = list( trainings )
        self.description.update( program_description )
                
    def add_training( self, training ):
        """Add single training. Only one is expected."""
        self.trainings.append( training )

    def add_description( self, **description ):
        self.description.update( description )

    def get_name( self ):
        return self.description["name"]

    def __repr__( self ):
        return "Simple program: " + "\n" + \
            "\t" + repr( self.description ) + "\n" + \
            "\t" + repr( self.trainings )

    def __str__( self ):
        return "Simple program: " + "\n" + \
            "\t" + str( self.description ) + "\n" + \
            "\t" + str( self.trainings )

    def repr_for_json_dump( self ):
        for_json = {}        
        trainings_for_json_dump = \
            [ x.repr_for_json_dump() for x in self.trainings ]
        for_json.update( self.description )
        for_json.update( { 'trainings': trainings_for_json_dump } )
        return for_json
    
    def save_simple_program( self, filename ):
        with open( filename, 'wt' ) as outfile:
            json.dump( self.repr_for_json_dump(), outfile, indent = 2 )

    @classmethod
    def load_simple_program( cls, filename ):
        with open( filename, 'rt' ) as infile:
            dict_from_json = json.load( infile )
            name = dict_from_json.pop('name', "Missing name")
            program = cls( name )
            trainings = dict_from_json.pop('trainings')
            for x in trainings:
                program.add_training( Training.init_from_json( x ) )
            program.add_description( **dict_from_json )
            return program


    # def advise_current_training( self, journal ):
    #     # inspects the last training.
    #     # if an overlap with any of the training days is big enough
    #     # then suggests the next day in the program.
    #     # if overlap is not found, suggest the first day.
    #     # not necessary for now.
    #     return random.choice( self.trainings )
