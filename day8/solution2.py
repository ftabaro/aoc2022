"""
Day 8 puzzle 2
"""

from __future__ import annotations
from typing import Optional


class Tree:
    """
    A class to represent a tree and its neigbours
    """

    def __init__(self, tree: int, position: tuple[int, int]):

        self.tree = tree
        self.position = position
        self.neighbours = {"top": None, "bottom": None, "left": None, "right": None}
        self.visibility_score = 1

    def __repr__(self) -> str:
        repr = f"Tree({self.tree=}, {self.position=}"
        return repr

    def set_neighbours(
        self,
        top: Optional[Tree],
        bottom: Optional[Tree],
        left: Optional[Tree],
        right: Optional[Tree],
    ):
        self.neighbours = {"top": top, "bottom": bottom, "left": left, "right": right}

    def calc_visibility_score(self):
        for direction in self.neighbours:
            neighbour = self.neighbours[direction]
            score = 0
            while neighbour is not None:
                score += 1
                if neighbour.tree >= self.tree:
                    break
                neighbour = neighbour.neighbours[direction]
            if score > 0:
                self.visibility_score *= score


def main(
    path: str, input_i: Optional[int] = None, input_j: Optional[int] = None
) -> int:
    """
    Solution to day 8 puzzle 2
    """

    with open(path, encoding="utf-8") as fin:
        grid = [[int(x) for x in line.strip()] for line in fin]

    nrow = len(grid)
    ncol = len(grid[0])
    forest = {
        (i, j): Tree(grid[i][j], (i, j)) for j in range(ncol) for i in range(nrow)
    }

    for position, tree in forest.items():
        i, j = position
        top = None
        if i - 1 >= 0:
            top = forest[(i - 1, j)]

        bottom = None
        if i + 1 < nrow:
            bottom = forest[(i + 1, j)]

        left = None
        if j - 1 >= 0:
            left = forest[(i, j - 1)]

        right = None
        if j + 1 < ncol:
            right = forest[(i, j + 1)]

        tree.set_neighbours(top, bottom, left, right)

    # handle tests from assignments...
    if input_i is not None and input_j is not None:
        print(f"{input_i=}, {input_j=}")
        tree = forest[(input_i, input_j)]
        tree.calc_visibility_score()
        score = tree.visibility_score

    # or do the whole thing
    else:
        for tree in forest.values():
            tree.calc_visibility_score()
        score = max(map(lambda tree: tree.visibility_score, forest.values()))

    print(score)
    return score


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
