def get_interval(start: int, end: int) -> set:
    return set(range(start, end + 1))


def main(path):
    counter = 0
    with open(path) as fin:
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