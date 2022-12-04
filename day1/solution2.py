"""
Day 1 puzzle 2
"""


def main(path: str) -> int:
    """
    Solution to day 1 puzzle 2
    """
    calories = []
    cal = 0
    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            print(line)
            if line == "":
                calories.append(cal)
                cal = 0
                continue
            cal += int(line)

    calories = sorted(calories, reverse=True)
    res = sum(calories[:3])
    return res


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
