from little_caret.visualize_lib.bokeh import Bokeh
from little_caret.record.record import Record
class Interface:
    def __init__(
            self,
            data: dict[str, list[int]]
        ) -> None:
        self._record = Record(data)
        self._bokeh = Bokeh()

    def data_append(
        self,
        data: dict[str, list[int]],
    ):
        self._record.append(data)



    def line_plot(self):
        self._bokeh.line_graph(self._record)

    def bar_plot(self):
        self._bokeh.bar_graph(self._record)


    @property # ()無しで参照できる
    def data(self):
        return self._record.data
