class Data(dict):
    """Actually a superset class of python dictionaries, which also supports accessing of its keys using . syntax."""

    def __getattribute__(self, item):
        try:
            data = self[str(item)]
        except KeyError:
            raise AttributeError
        else:
            try:
                return int(data)
            except ValueError:
                return data
