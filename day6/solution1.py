"""
Day 6 puzzle 1
"""

from typing import List


def main(path: str) -> List:
    """
    Solution to day 6 puzzle 1
    """
    with open(path, encoding="utf-8") as fin:
        signals = [line.strip() for line in fin.readlines()]

    res = []
    for signal in signals:
        siglen = len(signal)
        for i in range(siglen-4):
            msg = signal[i:i+4]
            letters = set(list(msg))            
            counts = [msg.count(letter) for letter in letters]
            if all(map(lambda x: x == 1, counts)):
                res.append(i+4)
                break
    print(res)
    return res


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
