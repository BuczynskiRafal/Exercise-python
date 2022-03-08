from typing import List
from itertools import cycle


def spiral_matrix(levels: int) -> List[list]:
    matrix = [[None] * levels for _ in range(levels)]
    x, y = 0, 0
    movements = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    dx, dy = next(movements)

    for number in range(levels ** 2):
        matrix[x][y] = number + 1
        xdx = x + dx
        ydy = y + dy
        if (
            not 0 <= xdx < levels
            or not 0 <= ydy < levels
            or matrix[xdx][ydy] is not None
        ):
            dx, dy = next(movements)
        x += dx
        y += dy
    return matrix


print(spiral_matrix(4))
