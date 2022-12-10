"""
Day 9 puzzle 1
"""

from __future__ import annotations
import math


class Tile:
    """
    A simple class to represent a 2D tile
    """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        rep = f"Tile({self.x=}, {self.y=})"
        return rep


class Knot:
    """
    A class to represent a knot or a segment of a snake or of a worm :D
    """
    def __init__(self, tile: Tile) -> None:
        self.tile = tile

    def __repr__(self) -> str:
        rep = f"Knot({self.tile=})"
        return rep

    def update_tile(self, head: Knot) -> None:
        """
        A function to update the knot position depending on its preceding knot
        """
        dx = head.tile.x - self.tile.x
        dy = head.tile.y - self.tile.y

        if abs(dx) == 2 and dy == 0:
            newx = self.tile.x + math.copysign(1, dx)
            newy = self.tile.y

        elif abs(dy) == 2 and dx == 0:
            newx = self.tile.x
            newy = self.tile.y + math.copysign(1, dy)

        elif (abs(dx) == 2 and abs(dy) > 0) or (abs(dx) > 0 and abs(dy) == 2):
            newx = self.tile.x + math.copysign(1, dx)
            newy = self.tile.y + math.copysign(1, dy)

        else:
            newx = self.tile.x
            newy = self.tile.y

        newx = int(newx)
        newy = int(newy)
        tile = Tile(newx, newy)

        self.tile = tile


class Head(Knot):
    """
    A special knot that represent the head of the rope or the snake. It has no
    preceding knots.
    """
    def __repr__(self) -> str:
        rep = f"Head({self.tile=})"
        return rep

    def update_tile(self, direction: str) -> None:
        """
        A function to model the movement of the head of the rope or the snake.
        Since it has no preceding knots, it can freely move of one step in each 
        direction.
        """
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


class Tail(Knot):
    """
    A special knot that remembers the tiles has visited.
    """
    def __init__(self, tile: Tile) -> None:
        super().__init__(tile)
        self.history = set([])
        self._update_history(tile)

    def __repr__(self) -> str:
        rep = f"Tail({self.tile=}, {self.history=})"
        return rep

    def _update_history(self, tile: Tile) -> None:
        """
        A function that stores a tile into the Tail memory.
        """
        self.history.add((tile.x, tile.y))

    def update_tile(self, knot: Knot) -> None:
        """
        A function that moves the tail depending on its preceding knot and 
        implements position memory.
        """
        Knot.update_tile(self, knot)
        self._update_history(self.tile)


class Snake:
    """
    A class that models a Snake (or a Rope). It has a fixed length of knots. 
    The first one is always a head, the last one is always a tail. 
    """
    def __init__(self, tile: Tile, length: int = 10) -> None:
        self.length = length - 1
        self.snake = []

        self.head = Head(tile)
        i = 1
        while i < self.length:
            self.snake.append(Knot(tile))
            i += 1
        self.snake.append(Tail(tile))

    def __repr__(self) -> str:
        head = self.head.__repr__()
        knots = [x.__repr__() for x in self.snake]
        knots = [
            x.replace('Knot(', f'Knot{i+1}(')
            for i, x in enumerate(knots)
        ]
        rep = (
            "Snake<"
            + f'length={len(self.snake) + 1}, '
            + f"{head}, "
            + f'{", ".join(knots)}'
            + ">"
        )
        rep = rep.replace("self.", "")
        return rep

    def update_tile(self, direction: str) -> None:
        """
        A function to update the positions of all the knots that compose the 
        Snake (or the Rope).
        """
        self.head.update_tile(direction)
        self.snake[0].update_tile(self.head)
        for i in range(1, self.length):
            self.snake[i].update_tile(self.snake[i - 1])

    def get_visited_tiles(self):
        """
        A function to get how many tiles the tail has visited.
        """
        return len(self.snake[-1:][0].history)


def main(path: str) -> int:
    """
    Solution to day 9 puzzle 1
    """

    start = Tile(0, 0)
    snake = Snake(start)

    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            direction, steps = line.split(" ")
            steps = int(steps)

            while steps > 0:
                snake.update_tile(direction)
                steps -= 1

    ret = snake.get_visited_tiles()
    print(ret)
    return ret


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
