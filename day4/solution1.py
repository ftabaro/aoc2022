"""
Day 4 puzzle 1
"""


def get_interval(start: int, end: int) -> set:
    """
    A function to get all the interval values from beginning and end values.
    """
    return set(range(start, end + 1))


def main(path: str) -> int:
    """
    Solution to day 4 puzzle 1.
    """
    counter = 0
    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip().split(",")

            elve1 = get_interval(*map(int, line[0].split("-")))
            elve2 = get_interval(*map(int, line[1].split("-")))

            diff1 = elve1.difference(elve2)
            diff2 = elve2.difference(elve1)

            if not diff1 or not diff2:
                counter += 1
                print(line)

    print(counter)
    return counter


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
