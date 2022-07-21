class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"items: {self._data}"

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]


def transfer(stack_1: Stack, stack_2: Stack):
    while not stack_1.is_empty():
        stack_2.push(stack_1.pop())
    return stack_2


s1 = Stack()
s1.push('python')
s1.push('java')
s1.push('c++')
print(s1.__repr__())

s2 = Stack()
s2.push('sql')
print(s2.__repr__())

s2 = transfer(s1, s2)

print(s2.__repr__())
