from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class StartExercisingScreen( Screen ):
    def __init__( self, **kwargs ):
        super( StartExercisingScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        self.follow_plan_button = Button( text = 'Follow the plan',
                                          halign='center' )
        self.follow_plan_button.on_press = self.generate_and_goto_training
        v_layout.add_widget( self.follow_plan_button )
        unplanned_training_button = Button( text = 'Unplanned training' )
        unplanned_training_button.on_press = self.goto_training
        v_layout.add_widget( unplanned_training_button )
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def generate_and_goto_training( self ):
        journal = App.get_running_app().journal
        current_program = App.get_running_app().simple_program
        if not current_program:
            self.goto_select_program()
            return
        self.parent.get_screen('training').following_plan = True
        self.parent.current = 'training'

    def goto_training( self ):
        self.parent.current = 'training'

    def goto_menu( self ):
        self.parent.current = 'menu'

    def goto_select_program( self ):
        self.parent.current = 'simple_program_selection'

    def on_pre_enter( self ):
        current_program_name = None
        if App.get_running_app().simple_program:
            current_program_name = \
                App.get_running_app().simple_program.get_name()
        self.follow_plan_button.text = 'Follow the plan.\n' + \
                '(Current program: {0})'.format( current_program_name )
