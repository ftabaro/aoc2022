import string

priority = string.ascii_lowercase + string.ascii_uppercase
priority = list(priority)
score = 0
group = []

def get_group_score(group):
    intersection = group[0] & group[1] & group[2]
    intersection = list(intersection)
    intersection = intersection[0]
    group_score = priority.index(intersection) + 1
    print(intersection, group_score)
    return group_score

with open("input.txt") as fin:
    for i, line in enumerate(fin):
        if i % 3 == 0 and i > 0:
            group_score = get_group_score(group)
            score += group_score
            group = []

        rucksack = line.strip()
        group.append(set(rucksack))
        
score += get_group_score(group)
print(score)
