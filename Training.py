from Exercise import *

class Training( object ):
    """Single training consists of a number of exercises and
    some arbitrary data, such as duration, start time, end time, 
    comments etc."""
    
    def __init__( self, *exercises, **training_description ):
        self.exercises = list( exercises )
        self.description = training_description

    def add_exercise( self, exercise ):
        """Add single exercise. Only one is expected."""
        self.exercises.append( exercise )

    def add_description( self, **description ):
        self.description.update( description )

    def repr_for_json_dump( self ):
        for_json = {}        
        exercises_for_json_dump = [ x.repr_for_json_dump() for x in self.exercises ]
        for_json.update( self.description )
        for_json.update( { 'exercises': exercises_for_json_dump } )
        return for_json

    def __repr__( self ):
        return "Training: \n" + \
            "\t" + repr( self.description ) + "\n" + \
            "\t" + repr( self.exercises ) + "\n" 

    def __str__( self ):
        return "Training: \n" + \
            "\t" + str( self.description ) + "\n" + \
            "\t" + str( self.exercises ) + "\n"    

    @classmethod
    def init_from_json( cls, dict_from_json ):
        training = cls()
        exercises = dict_from_json.pop('exercises')
        for x in exercises:
            exc_class_name = x.pop("type", "Exercise")
            exc_class = globals()[exc_class_name]
            training.add_exercise( exc_class.init_from_json( x ) )
        training.add_description( **dict_from_json )
        return training
