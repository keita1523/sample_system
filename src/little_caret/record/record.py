

class Record:
    def __init__(
        self,
        data: dict[str, list[int]],
    ) -> None:
        self._data = data

    def append(
        self,
        data: dict[str, list[int]],
    ):
        raise NotImplementedError()

    @property
    def data(self):
        return self._data