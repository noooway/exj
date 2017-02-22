from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ComposeTrainingPlanScreen( Screen ):
    def __init__( self, **kwargs ):
        super( ComposeTrainingPlanScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        simple_programs_button = Button( text = 'Simple programs' )
        simple_programs_button.on_press = self.goto_simple_program_selection
        v_layout.add_widget( simple_programs_button )
        specific_goal_programs_button = Button(
            text = 'Programs for specific goal (not implemented)' )
        v_layout.add_widget( specific_goal_programs_button )
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def goto_menu( self ):
        self.parent.current = 'menu'

    def goto_simple_program_selection( self ):
        self.parent.current = 'simple_program_selection'
