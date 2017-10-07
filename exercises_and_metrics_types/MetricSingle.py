from Metric import *

class MetricSingle( Metric ):
    def __init__( self, name, value, **description ):
        super( MetricSingle, self ).__init__( type = type(self).__name__,
                                              name = name, # type: str
                                              value = value, # type: float
                                              **description )
        self.essential_fields = ['name', 'value' ]

    @classmethod
    def construct_from_name( cls, metric_name ):
        value = ' '
        metric = cls( metric_name, value )
        return metric
        
    @classmethod
    def init_from_json( cls, dict_from_json ):
        metric = cls( **dict_from_json )
        return metric

    def rep_for_simple_program_selection( self ):
        return "Measure {}".format( self.description['name'] )
