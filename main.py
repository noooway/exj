import os.path
import ConfigParser

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from MenuScreen import *
from StartExercisingScreen import *
from ComposeTrainingPlanScreen import *
from SimpleProgramsScreen import *
from ViewProgressScreen import *
from TrainingScreen import *
from SelectExerciseScreen import *
from JournalOverviewScreen import *

from Journal import *
from SimpleProgram import *

# The App 
class ExjApp(App):
    def __init__( self ):
        App.__init__( self )
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        self.journal_file = config.get( 'Journal', 'journal_file' )
        self.simple_program_name = config.get('Training program',
                                              'simple_program_name' )
        self.simple_program_last_training = config.getint(
            'Training program', 'simple_program_last_training' )
        if os.path.isfile( self.journal_file ):            
            self.journal = Journal.load_journal( self.journal_file )
        else:
            self.journal = Journal()
        self.dict_of_simple_programs = self.read_simple_programs()
        self.simple_program = self.dict_of_simple_programs.get(
            self.simple_program_name )        

    def build( self ):
        sm = ScreenManager()
        sm.add_widget( MenuScreen( name='menu' ) )
        sm.add_widget( StartExercisingScreen( name='start_exercising') )
        sm.add_widget( ComposeTrainingPlanScreen(
            name='compose_training_plan') )
        sm.add_widget( SimpleProgramsScreen(
            name='simple_program_selection') )
        sm.add_widget( ViewProgressScreen( name='view_progress') )
        sm.add_widget( TrainingScreen( name='training') )
        sm.add_widget( SelectExerciseScreen( name='select_exercise') )
        sm.add_widget( JournalOverviewScreen( name='journal_overview') )
        return sm

    def write_config( self ):
        config = ConfigParser.ConfigParser()
        config.add_section( 'Journal' )
        config.set('Journal', 'journal_file', str(self.journal_file) )
        config.add_section( 'Training program' )
        config.set('Training program', 'simple_program_name',
                   str(self.simple_program_name) )
        config.set('Training program', 'simple_program_last_training',
                   str(self.simple_program_last_training) )
        with open('config.ini', 'w') as configfile:
            config.write( configfile )

    def read_simple_programs( self ):
        dict_of_simple_programs = {}
        simple_programs_folder = "simple_programs_library"
        for root, dirs, files in os.walk( simple_programs_folder ):
            for filename in files:
                if filename.endswith( ".json" ):
                    fullpath = os.path.join( root, filename )
                    simple_program = \
                        SimpleProgram.load_simple_program( fullpath )
                    dict_of_simple_programs.setdefault(
                        simple_program.description["name"], simple_program)
        return( dict_of_simple_programs )

    @staticmethod
    def strip_quotes( quoted_string ):
        return( quoted_string[1:-1] )

if __name__ == '__main__':
    exj = ExjApp()
    exj.run()
