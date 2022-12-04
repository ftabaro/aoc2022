
def main(path):
    counter = 0
    with open(path) as fin:
        for line in fin:
            line = line.strip().split(",")

            elve1_start, elve1_end = [int(x) for x in line[0].split("-")]
            elve2_start, elve2_end = [int(x) for x in line[1].split("-")]

            fully_contained = (
                (
                    elve2_start >= elve1_start and elve2_end <= elve1_end
                ) or (
                    elve1_start >= elve2_start and elve1_end <= elve2_end
                )
            )

            if fully_contained:
                counter += 1
                print(line)
            
    print(counter)
    return counter

if __name__ == "__main__":
    import sys
    main(sys.argv[1])