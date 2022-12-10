"""
Day 10 puzzle 2
"""


from typing import List
import math


def draw(
    sprite: List[int],
    cycle: int,
    crt_screen: List[List[str]]
) -> List[List[str]]:
    """
    A function to draw pixels
    """
    pixel = (cycle % 40) - 1
    pixel = pixel if pixel != -1 else 39
    row = math.ceil(cycle / 40) - 1
    if pixel in sprite:
        crt_screen[row][pixel] = '#'
    return crt_screen


def main(path: str) -> str:
    """
    Solution to day 10 puzzle 1
    """

    X = 1
    cycle = 0

    crt_screen = [["." for j in range(40)] for i in range(6)]

    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            sprite = [
                    X-1 if X-1 > 0 else 0,
                    X,
                    X+1 if X+1 < 39 else 39
            ]
            if line == "noop":
                cycle += 1
                crt_screen = draw(sprite, cycle, crt_screen)
            elif line.startswith("addx"):
                i = 0
                while i < 2:
                    cycle += 1
                    crt_screen = draw(sprite, cycle, crt_screen)
                    i += 1
                line = line.split(" ")
                X += int(line[1])

            else:
                raise ValueError(f"Unrecognized value: {line}.")

    crt_screen = [''.join(line) for line in crt_screen]
    crt_screen = '\n'.join(crt_screen)

    print(crt_screen)
    return crt_screen


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
