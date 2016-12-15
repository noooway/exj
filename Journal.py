import sys
import json
from Training import *

class Journal( object ):
    """Journal is a collection of trainings"""

    def __init__( self, *trainings, **journal_description ):
        self.trainings = list( trainings )
        self.description = journal_description

    def add_training( self, training ):
        """Add single training. Only one is expected."""
        self.trainings.append( training )

    def add_description( self, **description ):
        self.description.update( description )

    def __repr__( self ):
        return "Journal: \n" + \
            "\t" + repr( self.description ) + "\n" + \
            "\t" + repr( self.trainings )

    def __str__( self ):
        return "Journal: \n" + \
            "\t" + str( self.description ) + "\n" + \
            "\t" + str( self.trainings )

    def repr_for_json_dump( self ):
        for_json = {}        
        trainings_for_json_dump = [ x.repr_for_json_dump() for x in self.trainings ]
        for_json.update( self.description )
        for_json.update( { 'trainings': trainings_for_json_dump } )
        return for_json
    
    def save_journal( self, filename ):
        with open( filename, 'wt' ) as outfile:
            json.dump( self.repr_for_json_dump(), outfile, indent = 2 )

    @classmethod
    def load_journal( cls, filename ):
        journal = cls()
        with open( filename, 'rt' ) as infile:
            dict_from_json = json.load( infile )
            trainings = dict_from_json.pop('trainings')
            for x in trainings:
                journal.add_training( Training.init_from_json( x ) )
            journal.add_description( **dict_from_json )
        return journal
