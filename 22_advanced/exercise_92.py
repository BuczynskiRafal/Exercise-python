class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if Stack.is_empty(self) is True:
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return True if len(self._data) == 0 else False



