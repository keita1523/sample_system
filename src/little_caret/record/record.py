

class Record:
    def __init__(
        self,
        data: dict[str, int | list[int]],
    ) -> None:
        self._data = {key: [value] if isinstance(value, int) else value for key, value in data.items()}
        if not all(isinstance(v, int) for lst in self._data.values() for v in lst):
            raise TypeError("All values in the dictionary must be either an integer or a list of integers.")
        self._same_size()

    def append(
        self,
        data: dict[str, list[int]],
    ):
        self._data.update(data)

    def _same_size(
        self,
    ):
        max_length = max([len(v) for v in self._data.values()])
        self._data =  {k: v + [0]*(max_length - len(v)) for k, v in self._data.items()}

    @property
    def data(self):
        return self._data