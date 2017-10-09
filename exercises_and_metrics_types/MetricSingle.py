from Metric import *

class MetricSingle( Metric ):
    def __init__( self, name, value, description_dict ):
        super( MetricSingle, self ).__init__( description_dict )
        self.update( {
            'type': type(self).__name__, # type: str
            'name': name, # type: str
            'value': value, # type: float
        } )        
        self.essential_fields = ['name', 'value' ]

    @classmethod
    def construct_from_name( cls, metric_name ):
        value = ' '
        metric = cls( metric_name, value, {} )
        return metric
        
    @classmethod
    def init_from_json( cls, dict_from_json ):
        name = dict_from_json.pop( 'name' )
        value = dict_from_json.pop( 'value' )
        metric = cls( name, value, dict_from_json )
        return metric

    def rep_for_simple_program_selection( self ):
        return "Measure {}".format( self.description['name'] )
