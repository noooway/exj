from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ViewProgressScreen( Screen ):
    def __init__( self, **kwargs ):
        super( ViewProgressScreen, self ).__init__( **kwargs )
        v_layout = BoxLayout( orientation = 'vertical',
                              spacing = 30 )
        progress_label = Label(
            text = 'Program progress (not implemented)' )
        v_layout.add_widget( progress_label )
        exercise_statistics_button = Button(
            text = 'Statistics for Specific Exercise' )
        exercise_statistics_button.on_press = \
            self.goto_exercise_statistics
        v_layout.add_widget( exercise_statistics_button )
        journal_overview_button = Button( text = 'Journal overview' )
        journal_overview_button.on_press = self.goto_journal_overview
        v_layout.add_widget( journal_overview_button )        
        back_to_menu_button = Button( text = 'Back to menu' )
        back_to_menu_button.on_press = self.goto_menu
        v_layout.add_widget( back_to_menu_button )
        self.add_widget( v_layout )

    def goto_journal_overview( self ):
        self.parent.current = 'journal_overview'

    def goto_exercise_statistics( self ):
        self.parent.current = 'exercise_statistics'
        
    def goto_menu( self ):
        self.parent.current = 'menu'
