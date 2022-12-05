"""
Day 5 puzzle 1
"""

import re
import math
from typing import List


def parse_stack_config(stack_config: List[str]) -> List[List[str]]:
    """
    A function to read the initial stack configuration and parse it into
    a StackConfig object.

    Each key of the output dict should represent a stack. The values represent
    the content of the stack
    """
    # find number of stacks
    number_of_stacks = stack_config.pop(len(stack_config) - 1)
    number_of_chars = len(number_of_stacks)
    number_of_stacks = map(
        int, filter(lambda x: len(x) > 0, number_of_stacks.split(" "))
    )
    number_of_stacks = max(number_of_stacks)

    # initialize output
    ret = [[] for i in range(number_of_stacks)]

    # populate stacks
    pat = re.compile(r"\[(\w)\]")
    for row in stack_config:
        for match in re.finditer(pat, row):
            position_in_row = match.start(1)
            stack = math.ceil(
                position_in_row / number_of_chars * number_of_stacks
            )
            ret[stack - 1].append(match.group(1))
    return ret


def move_stacks(
    stack_config: List[List[str]], moves: List[str]
) -> List[List[str]]:
    """
    A function to compute the stack configuration after all the moves requested
    """
    pat = re.compile(r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)$")
    for move in moves:
        match = re.match(pat, move)
        if match is not None:
            nitems = int(match.group(1))
            from_stack = int(match.group(2))
            to_stack = int(match.group(3))

            for i in range(nitems):
                item = stack_config[from_stack - 1].pop(0)
                stack_config[to_stack - 1].insert(0, item)

    return stack_config


def main(path: str) -> str:
    """
    Solution to day 5 puzzle 1
    """
    stack_config = []
    moves = []
    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.rstrip("\n")
            if line.startswith("move"):
                moves.append(line)
            elif line != "":
                stack_config.append(line)

    stack_config = parse_stack_config(stack_config)
    stack_config = move_stacks(stack_config, moves)
    ret = "".join([x[0] for x in stack_config])
    print(ret)
    return ret


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
