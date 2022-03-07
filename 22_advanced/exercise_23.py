"""This module contain simple class
allow you to create scrabble game."""

import collections

Plate = collections.namedtuple("Plate", ["symbol", "points"])


class Scrabble:
    """Scrabble class allow you to create scrabble game."""

    elements = (
        [(" ", 0) for element in range(2)]
        + [(letter, 1) for letter in "EAIONRTLSU"]
        + [(letter, 2) for letter in "DG"]
        + [(letter, 3) for letter in "BCMP"]
        + [(letter, 4) for letter in "FHVWY"]
        + [(letter, 5) for letter in "K"]
        + [(letter, 8) for letter in "JX"]
        + [(letter, 10) for letter in "QZ"]
    )

    def __init__(self):
        self._plate = [Plate(symbol, points) for symbol, points in self.elements]

    def __len__(self):
        return len(self._plate)

    def get_letter(self, letter: str) -> object:
        """
        This function allows you to search for object contains typed letter.
        :return: object that is instance Scrabble class.
        """
        for element in self._plate:
            return element if element.symbol == letter else 'Not found'

    def score(self, word: str) -> int:
        """
        This function allows you to calculate the sum of points from the entered word.
        :return: score (int) - sum of points
        """
        score = 0
        for letter in word:
            score += self.get_letter(letter).points
        return score


plate = Scrabble()
