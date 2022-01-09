class Queue:
    """A simplest queue."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, other):
        return self._data.append(other)

    def dequeue(self):
        if len(self) != 0:
            return self._data.pop()
        else:
            raise IndexError('The queue is empty.')


