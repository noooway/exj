import os.path
import configparser

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

from list_of_simple_programs import list_of_simple_programs

# The App 
class ExjApp(App):
    def __init__( self ):
        App.__init__( self )
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.journal_file = config.get( 'Journal', 'journal_file' )
        self.simple_program_key_in_list = config.get('Training program', 'simple_program_key_in_list' )
        self.simple_program_last_training = config.getint(
            'Training program', 'simple_program_last_training' )
        if os.path.isfile( self.journal_file ):            
            self.journal = Journal.load_journal( self.journal_file )
        else:
            self.journal = Journal()
        self.simple_program = list_of_simple_programs.get(
            self.simple_program_key_in_list )        

    def build( self ):
        sm = ScreenManager()
        sm.add_widget( MenuScreen( name='menu' ) )
        sm.add_widget( StartExercisingScreen( name='start_exercising') )
        sm.add_widget( ComposeTrainingPlanScreen( name='compose_training_plan') )
        sm.add_widget( SimpleProgramsScreen( name='simple_program_selection') )
        sm.add_widget( ViewProgressScreen( name='view_progress') )
        sm.add_widget( TrainingScreen( name='training') )
        sm.add_widget( SelectExerciseScreen( name='select_exercise') )
        sm.add_widget( JournalOverviewScreen( name='journal_overview') )
        return sm

    def write_config( self ):
        config = configparser.ConfigParser()
        config.add_section( 'Journal' )
        config.set('Journal', 'journal_file', str(self.journal_file) )
        config.add_section( 'Training program' )
        config.set('Training program', 'simple_program_key_in_list',
                   str(self.simple_program_key_in_list) )
        config.set('Training program', 'simple_program_last_training',
                   str(self.simple_program_last_training) )
        with open('config.ini', 'w') as configfile:
            config.write( configfile )

    @staticmethod
    def strip_quotes( quoted_string ):
        return( quoted_string[1:-1] )

if __name__ == '__main__':
    exj = ExjApp()
    exj.run()
