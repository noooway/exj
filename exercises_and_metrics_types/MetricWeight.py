from Metric import *

class MetricWeight( Metric ):
    def __init__( self, name, weight, **description ):
        super( MetricWeight, self ).__init__( type = type(self).__name__,
                                              name = name,
                                              weight = weight,
                                              **description )
        self.essential_fields = ['name', 'weight' ]

    @classmethod
    def init_from_json( cls, dict_from_json ):
        metric = cls( **dict_from_json )
        return metric
