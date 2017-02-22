from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MenuScreen( Screen ):
    def __init__( self, **kwargs ):
        super( MenuScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        start_exercising_button = Button( text = 'Start exercising' )
        start_exercising_button.on_press = self.goto_start_exercising
        v_layout.add_widget( start_exercising_button )
        compose_training_plan_button = Button( text = 'Compose training plan' )
        compose_training_plan_button.on_press = self.goto_compose_training_plan
        v_layout.add_widget( compose_training_plan_button )
        view_progress_button = Button( text = 'View progress' )
        view_progress_button.on_press = self.goto_view_progress
        v_layout.add_widget( view_progress_button )
        quit_button = Button( text = 'Quit' )
        quit_button.on_press = self.save_journal_and_quit
        v_layout.add_widget( quit_button )
        self.add_widget( v_layout )

    def goto_start_exercising( self ):
        self.parent.current = 'start_exercising'

    def goto_compose_training_plan( self ):
        self.parent.current = 'compose_training_plan'

    def goto_view_progress( self ):
        self.parent.current = 'view_progress'

    def save_journal_and_quit( self ):
        app = App.get_running_app()
        #app.write_config()
        app.journal.save_journal( app.journal_file )
        app.stop()
        
