class EmptyStackError(Exception):
    pass

class Stack:
    """A simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.insert(0, item)

    def pop(self):
        try:
            return self._data[0]
            del(self._data[0])
        except:
            raise EmptyStackError('The stack is empty.')


techs = Stack()
techs.push('python')
techs.push('sql')
print(len(techs))

techs.pop()