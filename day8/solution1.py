"""
Day 8 puzzle 1
"""

from typing import List


def is_visible(tree: int, tree_set: List[int]):
    """
    A function to test if a given tree is vibile through all the trees in a 
    given direction
    """
    return all(map(lambda x: x < tree, tree_set))


def main(path: str) -> int:
    """
    Solution to day 8 puzzle 1
    """

    with open(path, encoding="utf-8") as fin:
        grid = [[int(x) for x in line.strip()] for line in fin]

    nrow = len(grid)
    ncol = len(grid[0])

    visible_trees = 2 * (ncol + nrow) - 4
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            tree = grid[i][j]

            left_trees = grid[i][:j]
            right_trees = grid[i][j + 1 :]
            top_trees = list(map(lambda x: x[j], grid[:i]))
            bottom_trees = list(map(lambda x: x[j], grid[i + 1 :]))

            for trees_set in [left_trees, right_trees, top_trees, bottom_trees]:
                visible = is_visible(tree, trees_set)
                if visible:
                    visible_trees += 1
                    break

    print(visible_trees)
    return visible_trees


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
