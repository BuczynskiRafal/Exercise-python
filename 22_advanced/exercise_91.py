class EmptyStackError(Exception):
    pass

class Stack:
    """A simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()


techs = Stack()
techs.push('python')
techs.push('sql')
print(len(techs))
