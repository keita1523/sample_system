from little_caret.record.record import Record
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models import LinearColorMapper
from bokeh.palettes import Turbo256
from .color_selector import ColorSelectorFactory

class Bokeh:
    def __init__(self) -> None:
        pass

    def line_graph(
        self,
        record: Record,
    ):
        data: dict[str, list[int]] = record.data

        fig = figure(title='line plot', x_axis_label='x軸', y_axis_label='y軸')
        keys =list(data.keys())
        x_values = list(range(len(data[keys[0]])))

        source = ColumnDataSource(data=data)
        source.add(x_values, 'x_values')
        color_selector = ColorSelectorFactory.create_instance(coloring_rule='unique')

        for column in data:
            color = color_selector.get_color(column)
            fig.line(
                x='x_values', y=column, source=source,
                line_color=color,
            )
        show(fig)

    def bar_graph(
        self,
        record: Record
    ):
        data: dict[str, list[int]] = record.data
        fig = figure(title='bar plot', x_axis_label='x軸', y_axis_label='y軸')
        keys =list(data.keys())
        # x_values = keys
        x_values = list(range(len(data[keys[0]])))
        source = ColumnDataSource(data=data)
        source.add(x_values, 'x_values')
        color_selector = ColorSelectorFactory.create_instance(coloring_rule='unique')
        for column in data:
            color = color_selector.get_color(column)
            fig.vbar(x='x_values', top=column, width=0.5, source=source, color=color)
        show(fig)

