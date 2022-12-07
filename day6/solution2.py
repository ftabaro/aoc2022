"""
Day 6 puzzle 2
"""

from typing import List


def main(path: str) -> List:
    """
    Solution to day 6 puzzle 2
    """
    with open(path, encoding="utf-8") as fin:
        signals = [line.strip() for line in fin.readlines()]

    res = []
    packet_size = 14
    for signal in signals:
        siglen = len(signal)
        for i in range(siglen-packet_size):
            msg = signal[i:i+packet_size]
            letters = set(list(msg))
            if len(letters) == packet_size:
                res.append(i+packet_size)
                break
    print(res)
    return res


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
