import os.path

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
import config

# The App 
class ExjApp(App):
    def __init__(self):
        App.__init__( self )
        self.journal_file = config.journal_file
        self.simple_program_key_in_list = config.simple_program_key_in_list
        self.simple_program_last_training = config.simple_program_last_training
        if os.path.isfile( self.journal_file ):            
            self.journal = Journal.load_journal( self.journal_file )
        else:
            self.journal = Journal()
        self.simple_program = list_of_simple_programs.get(
            self.simple_program_key_in_list )        

    def build(self):
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
        with open( 'config.py', 'w' ) as outfile:
            outfile.write( 'journal_file = "{0}"\n'.format( self.journal_file ) )
            outfile.write( 'simple_program_key_in_list = "{0}"\n'.format(
                self.simple_program_key_in_list ) )
            outfile.write( 'simple_program_last_training = {0}\n'.format(
                self.simple_program_last_training ) )
            

if __name__ == '__main__':
    exj = ExjApp()
    exj.run()
