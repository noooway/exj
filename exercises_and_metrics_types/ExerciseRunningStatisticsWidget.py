from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from ExerciseRunning import *

from kivy.graphics import *
from kivy.core.text import Label as CoreLabel
#https://groups.google.com/forum/#!topic/kivy-users/zRCjfhBcX4c

class ExerciseRunningStatisticsWidget( GridLayout ):
    def __init__( self, exercise_sets_reps_weights_name,
                  journal, **kwargs ):
        super( ExerciseRunningStatisticsWidget,
               self ).__init__( **kwargs )
        self.cols = 1
        self.spacing = 1
        self.exercise_name = exercise_sets_reps_weights_name
        excercise_label = Label(
            text = "(ExerciseRunning, default plot type)",
            size_hint_y = 0.1 )
        self.add_widget( excercise_label )
        self.drawing_widget = Widget()
        self.add_widget( self.drawing_widget )
        self.drawing_widget.bind( size = self.update_drawing )
        
    def update_drawing(self, *args):
        self.drawing_widget.canvas.clear()
        self.drawing_widget.canvas.add( Color( 1, 1, 1) )
        self.drawing_widget.bg_rect = Rectangle(
            pos = (0, 0),
            size = ( self.drawing_widget.width,
                     self.drawing_widget.height ) )
        self.drawing_widget.canvas.add( self.drawing_widget.bg_rect )
        journal = App.get_running_app().journal
        drawing_instructions = \
        ExerciseRunningStatisticsWidget.gen_drawing_instructions(
            self.exercise_name, journal,
            self.drawing_widget.bg_rect.size )
        self.drawing_widget.canvas.add( drawing_instructions )
        
    @classmethod
    def gen_drawing_instructions( cls, ex_name, journal, rect_size ):
        plot = InstructionGroup()
        # test
        plot.add( Color( 1, 1, 0) )
        plot.add( Rectangle( pos = (0, 0), size = ( 100, 100 ) ) )
        #
        axes_offsets, axes_sizes, axes_instr = \
            cls.axes_instructions( rect_size )
        plot.add( axes_instr )
        dates_exces = cls.get_dates_exercises_pairs( ex_name, journal )
        ticks_instr = cls.ticks_instructions( axes_offsets,
                                              axes_sizes,
                                              dates_exces )
        plot.add( ticks_instr )
        plot.add( cls.plot_dists_times( dates_exces,
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
    def plot_dists_times( cls, dates_exces, axes_offset, axes_size ):
        dists_times_instr = InstructionGroup()
        if len( dates_exces ) != 0:
            distance_between_centers = axes_size[0] / len( dates_exces )
        else:
            distance_between_centers = 0
        max_total = 0
        for d, ex in dates_exces:
            # move to sep function
            ex_total = 0
            dists = ex.description.get("distances")
            for dist in dists:
                try:
                    ex_total = ex_total + float(dist)
                except ValueError:
                    ex_total = ex_total + 0
                if ex_total > max_total:
                    max_total = ex_total
        if max_total != 0:
            y_distance = axes_size[1] / ( max_total + 1 )
        else:
            y_distance = 0
        for i, (d, ex) in enumerate( dates_exces ):
            distances = ex.description.get("distances")
            times = ex.description.get("times")
            float_dists = []
            for dist in distances:
                try:
                    float_dists.append( float(dist) )
                except ValueError:
                    float_dists.append( 0 )
            for f_d, d in enumerate( float_dists ):
                y_pos_top = axes_offset[1] + \
                            sum( float_dists[0:f_d+1] ) * y_distance
                y_pos_bottom = axes_offset[1] + \
                               sum( float_dists[0:f_d] ) * y_distance
                x_center_pos = \
                    axes_offset[0] + distance_between_centers * (i + 1)
                x_size = 10
                y_size = y_pos_top - y_pos_bottom
                dists_times_instr.add(
                    Line( points = [ x_center_pos - 5, y_pos_top,
                                     x_center_pos + 5, y_pos_top ],
                          width = 3 ) )
                text_label = CoreLabel( text = str(d), font_size = 15 )
                text_label.refresh()
                texture = text_label.texture
                texture_size = list( texture.size )
                dists_times_instr.add( Rectangle(
                    texture = texture,
                    size = texture_size,
                    pos = (
                        x_center_pos - 10,
                        y_pos_bottom + (y_pos_top - y_pos_bottom) / 2 )))
        return dists_times_instr
