class Exercise( object ):
    """Exercise description"""    
    def __init__( self, **description ):
        self.description = description
        self.essential_fields = None

    def __repr__( self ):
        return repr( self.description )

    def __str__( self ):
        return str( self.description )

    def update( self, **description ):
        self.description.update( description )

    def repr_for_json_dump( self ):
        return( self.description )

    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise
