"""This module contain simple class allow you convert string matrix to list with int value."""

class Matrix:
    """Matrix class - convert string matrix to list with int value."""

    def __init__(self, matrix):
        """
        Create attribute matrix  - convert string matrix to list with int value."
        :type matrix: take string and convert to matrix List[[int]].
        """
        self.matrix = [[int(n) for n in numbers.split()] for numbers in matrix.split('\n')]


m = Matrix('1')
print(m.matrix)
