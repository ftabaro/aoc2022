"""
Day 3 puzzle 2
"""

import string

PRIORITY = string.ascii_lowercase + string.ascii_uppercase
PRIORITY = list(PRIORITY)


def get_group_score(group):
    """
    A function to compute the score of a group of shared items
    """
    intersection = group[0] & group[1] & group[2]
    intersection = list(intersection)
    intersection = intersection[0]
    group_score = PRIORITY.index(intersection) + 1
    print(intersection, group_score)
    return group_score


def main(path: str) -> int:
    """
    Solution to day 3 puzzle 2
    """
    score = 0
    group = []

    with open(path, encoding="utf-8") as fin:
        for i, line in enumerate(fin):
            if i % 3 == 0 and i > 0:
                group_score = get_group_score(group)
                score += group_score
                group = []

            rucksack = line.strip()
            group.append(set(rucksack))

    score += get_group_score(group)
    print(score)
    return score


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
