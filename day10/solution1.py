"""
Day 10 puzzle 1
"""


from typing import List


def test_cycle(
    X: int, cycle: int, emit_cycle: int, emit_values: List[int]
) -> tuple[int, List[int]]:
    """
    Test if the given cycle needs to emit a value. Updates next emit cycle and
    return updated emit values list.
    """
    if cycle == emit_cycle:
        emit_values.append(X * emit_cycle)
        emit_cycle += 40
    return emit_cycle, emit_values


def main(path: str) -> int:
    """
    Solution to day 10 puzzle 1
    """

    X = 1
    cycle = 0
    emit_cycle = 20
    emit_values = []
    with open(path, encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if line == "noop":
                cycle += 1
                emit_cycle, emit_values = test_cycle(
                    X, cycle, emit_cycle, emit_values
                )
            elif line.startswith("addx"):
                i = 0
                while i < 2:
                    cycle += 1
                    emit_cycle, emit_values = test_cycle(
                        X, cycle, emit_cycle, emit_values
                    )
                    i += 1
                line = line.split(" ")
                X += int(line[1])
            else:
                raise ValueError(f"Unrecognized value: {line}.")

    ret = sum(emit_values)
    print(ret)
    return ret


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
