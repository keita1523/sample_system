from little_caret.record.record import Record
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

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
        for column in data:
            fig.line(x='x_values', y=column, source=source)
        show(fig)
