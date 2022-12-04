import string

PRIORITY = string.ascii_lowercase + string.ascii_uppercase
PRIORITY = list(PRIORITY)

def get_group_score(group):
    intersection = group[0] & group[1] & group[2]
    intersection = list(intersection)
    intersection = intersection[0]
    group_score = PRIORITY.index(intersection) + 1
    print(intersection, group_score)
    return group_score

def main(path: str) -> int:
    score = 0
    group = []


    with open(path) as fin:
        for i, line in enumerate(fin):
            if i % 3 == 0 and i > 0:
                group_score = get_group_score(group)
                score += group_score
                group = []

            rucksack = line.strip()
            group.append(set(rucksack))
            
    score += get_group_score(group)
    print(score)
    return score


if __name__ == "__main__":
    import sys
    main(sys.argv[1])