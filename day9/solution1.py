"""
Day 9 puzzle 1
"""

import math


class Tile:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        rep = f"Tile({self.x=}, {self.y=})"
        return rep


class Head:
    def __init__(self, tile: Tile) -> None:
        self.tile = tile

    def __repr__(self) -> str:
        rep = f"Head({self.tile=})"
        return rep

    def update_tile(self, direction: Tile) -> None:
        # print(f'Head - from {self.tile} to {tile}')

        x = self.tile.x
        y = self.tile.y

        if direction == "R":
            newx = x + 1
            newy = y

        elif direction == "L":
            newx = x - 1
            newy = y

        elif direction == "U":
            newx = x
            newy = y + 1

        elif direction == "D":
            newx = x
            newy = y - 1

        else:
            raise Exception(f"Unknown direction: {direction}.")

        self.tile = Tile(newx, newy)


class Tail:
    def __init__(self, tile: Tile) -> None:
        self.tile = tile
        self.history = set([])
        self._update_history(tile)

    def __repr__(self) -> str:
        rep = f"Tail({self.tile=}, {self.history=})"
        return rep

    def _update_history(self, tile: Tile) -> None:
        self.history.add((tile.x, tile.y))

    def update_tile(self, head: Head) -> None:
        dx = head.tile.x - self.tile.x
        dy = head.tile.y - self.tile.y

        if abs(dx) == 2 and dy == 0:
            newx = self.tile.x + math.copysign(1, dx)
            newy = self.tile.y

        elif abs(dy) == 2 and dx == 0:
            newx = self.tile.x
            newy = self.tile.y + math.copysign(1, dy)

        elif (abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2):
            newx = self.tile.x + math.copysign(1, dx)
            newy = self.tile.y + math.copysign(1, dy)

        else:
            newx = self.tile.x
            newy = self.tile.y

        tile = Tile(newx, newy)
        # print(f'Tail - from {self.tile} to {tile}')
        self.tile = tile
        self._update_history(tile)


def main(path: str) -> int:
    """
    Solution to day 9 puzzle 1
    """

    start = Tile(0, 0)
    H = Head(start)
    T = Tail(start)

    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            direction, steps = line.split(" ")
            steps = int(steps)

            while steps > 0:
                H.update_tile(direction)
                T.update_tile(H)
                steps -= 1

    # print(T.history)
    ret = len(T.history)
    print(ret)
    return ret


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
