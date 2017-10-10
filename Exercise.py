class Exercise( object ):
    """Exercise description"""    
    def __init__( self, description_dict ):
        self.description = description_dict
        self.essential_fields = None

    def __repr__( self ):
        return repr( self.description )

    def __str__( self ):
        return str( self.description )

    def update( self, description_dict ):
        self.description.update( description_dict )

    def repr_for_json_dump( self ):
        return( self.description )

    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return str( self.description )
