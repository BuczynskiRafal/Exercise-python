"""This module contain simple class allow you convert string matrix to list with int value."""


class Matrix:
    """Matrix class - convert string matrix to list with int value."""

    def __init__(self, string):
        """
        Create attribute matrix  - convert string matrix to list with int value."
        :type string: take string and convert to matrix List[[int]].
        """
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join(
            [' '.join(str(element)
                      for element in row)
                      for row in self.matrix])

    def row(self, index):
        return self.matrix[index]


m = Matrix('1 3\n5 6')
print(m.__repr__())
