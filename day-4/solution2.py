
def get_interval(start: int, end: int) -> set:
    return set(range(start, end + 1))

def main(path: str) -> int:
    counter = 0
    with open(path) as fin:
        for line in fin:
            line = line.strip().split(",")

            elve1 = get_interval(*map(int, line[0].split("-")))
            elve2 = get_interval(*map(int, line[1].split("-")))

            shared = elve1.intersection(elve2)

            if len(shared) > 0:
                counter += 1
                print(line)
            
    print(counter)
    return counter

if __name__ == "__main__":
    import sys
    main(sys.argv[1])