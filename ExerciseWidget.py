class ExerciseWidget( BoxLayout ):
    def __init__( self, **kwargs ):
        super( ExerciseWidget, self ).__init__( **kwargs )
        self.orientation = 'vertical'
        self.spacing = 1
        excercise_label = Label( text = kwargs.get('text') )
        self.add_widget( excercise_label )
        results = TextInput( text = 'Enter Results' )
        self.add_widget( results )
        comment = TextInput( text = 'Enter Comment' )
        self.add_widget( comment )    
