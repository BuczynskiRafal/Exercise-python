"""This module contain function
allow you calculate hamming vector distance."""


def equal_length(vector_1: str, vector_2: str) -> bool:
    """
    The method checks if two vectors are of equal length.
    :rtype: True or raise ValueError
    """
    if len(vector_1) == len(vector_2):
        return True
    raise ValueError("Both vectors must be the same length.")


def hamming_distance(vector_1: str, vector_2: str) -> int:
    """
    Method allow calculate the hamming distance between two vectors.
    :type vector_1: str
    :type vector_2: str

    :return length: int
    """
    if equal_length(vector_1, vector_2):
        iterate = len(vector_1)
        length = 0
        for index in range(iterate):
            if not vector_1[index] == vector_2[index]:
                length += 1
            else:
                continue
        return length


print(hamming_distance('110', '101'))
