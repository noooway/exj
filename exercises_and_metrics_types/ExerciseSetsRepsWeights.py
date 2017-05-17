from Exercise import *

from kivy.graphics import *
from kivy.core.text import Label as CoreLabel
#https://groups.google.com/forum/#!topic/kivy-users/zRCjfhBcX4c


class ExerciseSetsRepsWeights( Exercise ):
    def __init__( self, name, sets, reps, weights, **description ):
        super( ExerciseSetsRepsWeights, self ).__init__(
            type = type(self).__name__,
            name = name,
            sets = sets,
            reps = reps,
            weights = weights,
            **description )
        self.essential_fields = ['name', 'sets', 'reps', 'weights' ]

    @classmethod
    def construct_from_name( cls, exercise_name ):
        sets = 3
        reps = [ '10', '10', '10' ]
        weights = [ '30', '50', '50' ]
        exercise = cls( exercise_name, sets, reps, weights )
        return exercise
        
    @classmethod
    def init_from_json( cls, dict_from_json ):
        exercise = cls( **dict_from_json )
        return exercise

    def rep_for_simple_program_selection( self ):
        return "{}: {} sets, {} reps".format(
            self.description['name'],
            self.description['sets'],
            self.description['reps'] )

    @classmethod
    def gen_drawing_instructions( cls, ex_name, journal, rect_size ):
        plot = InstructionGroup()
        #plot.add( Color( 1, 1, 0) )
        #plot.add( Rectangle( pos = (0, 0), size = ( 100, 100 ) ) )
        axes_offsets, axes_sizes, axes_instr = \
            cls.axes_instructions( rect_size )
        plot.add( axes_instr )
        dates_exces = cls.get_dates_exercises_pairs( ex_name, journal )
        ticks_instr = cls.ticks_instructions( axes_offsets,
                                              axes_sizes,
                                              dates_exces )
        plot.add( ticks_instr )
        plot.add( cls.plot_sets_reps( dates_exces,
                                      axes_offsets,
                                      axes_sizes ) )
        return plot

    @classmethod
    def axes_instructions( cls, rect_size ):
        axes = InstructionGroup()
        offset_x = 0.05 * rect_size[0]
        offset_y = 0.1 * rect_size[1]
        line_width = 2
        axes.add( Color( 0, 0, 0) )
        axes.add( Line(
            points = [ offset_x, offset_y,
                       offset_x, rect_size[1] - offset_y ],
            width = line_width ) )
        axes.add( Line(
            points = [ offset_x, offset_y,
                       rect_size[0] - offset_x, offset_y ],
            width = line_width ) )
        return ( ( offset_x, offset_y ),
                 ( rect_size[0] - 2 * offset_x,
                   rect_size[1] - 2 * offset_y ),
                 axes )

    @classmethod
    def ticks_instructions( cls, axes_offsets, axes_sizes, dates_exces ):
        x_ticks = InstructionGroup()
        ticks_len = 5
        if len( dates_exces ) != 0:
            x_ticks_distance = axes_sizes[0] / len( dates_exces )
        else:
            x_ticks_distance = 0
        yyyy_mm_dd = [ x.split(' ')[0] for (x, y) in dates_exces ]
        for i, d in enumerate( yyyy_mm_dd ):
            x_ticks.add(
                Line( points =
                      [ axes_offsets[0] + ( i + 1 ) * x_ticks_distance,
                        axes_offsets[1],
                        axes_offsets[0] + ( i + 1 ) * x_ticks_distance,
                        axes_offsets[1] - ticks_len ],
                      width = 3 ) )
            text_label = CoreLabel( text=d, font_size = 15 )
            text_label.refresh()
            texture = text_label.texture
            texture_size = list( texture.size )
            x_ticks.add( Rectangle(
                texture = texture,
                size = texture_size,
                pos = (
                    axes_offsets[0] + ( i + 1 ) * x_ticks_distance - 45,
                    axes_offsets[1] - ticks_len - 25 )))
        return x_ticks
    
            
    @classmethod
    def get_dates_exercises_pairs( cls, ex_name, journal ):
        dates_exces = []
        # move to Journal class?
        for tr in journal.trainings:
            for ex in tr.exercises:
                if ex_name == ex.description.get( 'name' ):
                    dates_exces.append( 
                        ( tr.description.get( "start_time" ), ex ) )
        return dates_exces
                                         

    @classmethod
    def plot_sets_reps( cls, dates_exces, axes_offset, axes_size ):
        sets_reps_instr = InstructionGroup()
        if len( dates_exces ) != 0:
            distance_between_centers = axes_size[0] / len( dates_exces )
        else:
            distance_between_centers = 0
        max_total = 0
        for d, ex in dates_exces:
            # move to sep function
            ex_total = 0
            reps = ex.description.get("reps")
            for r in reps:
                try:
                    ex_total = ex_total + int(r)
                except ValueError:
                    ex_total = ex_total + 0
                if ex_total > max_total:
                    max_total = ex_total
        if max_total != 0:
            y_distance = axes_size[1] / ( max_total + 1 )
        else:
            y_distance = 0
        for i, (d, ex) in enumerate( dates_exces ):
            sets = ex.description.get("sets")
            reps = ex.description.get("reps")
            weights = ex.description.get("weights")
            int_reps = []
            for r in reps:
                try:
                    int_reps.append( int(r) )
                except ValueError:
                    int_reps.append( 0 )
            for i_r,r in enumerate( int_reps ):
                y_pos_top = axes_offset[1] + \
                            sum( int_reps[0:i_r+1] ) * y_distance
                y_pos_bottom = axes_offset[1] + \
                               sum( int_reps[0:i_r] ) * y_distance
                x_center_pos = \
                    axes_offset[0] + distance_between_centers * (i + 1)
                x_size = 10
                y_size = y_pos_top - y_pos_bottom
                sets_reps_instr.add(
                    Line( points = [ x_center_pos - 5, y_pos_top,
                                     x_center_pos + 5, y_pos_top ],
                          width = 3 ) )
                text_label = CoreLabel( text = str(r), font_size = 15 )
                text_label.refresh()
                texture = text_label.texture
                texture_size = list( texture.size )
                sets_reps_instr.add( Rectangle(
                    texture = texture,
                    size = texture_size,
                    pos = (
                        x_center_pos - 10,
                        y_pos_bottom + (y_pos_top - y_pos_bottom) / 2 )))
        return sets_reps_instr
