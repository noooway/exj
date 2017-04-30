from Exercise import *

class Metric( Exercise ):
    """Metric is just another sort of exercise"""
    def __init__( self, **description ):
        super( Metric, self ).__init__( **description )

    @classmethod
    def init_from_json( cls, dict_from_json ):
        metric = cls( **dict_from_json )
        return metric
