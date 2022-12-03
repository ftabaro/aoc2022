import string

priority = string.ascii_lowercase + string.ascii_uppercase
priority = list(priority)
score = 0
with open("input.txt") as fin:
    for line in fin:
        rucksack = line.strip()
        nitems = len(rucksack)
        
        first_compartment = rucksack[:int(nitems / 2)]
        first_compartment = set(first_compartment)

        second_compartment = rucksack[int(nitems / 2):]
        second_compartment = set(second_compartment)

        intersection = list(first_compartment.intersection(second_compartment))
        intersection = str(intersection[0])
        score += priority.index(intersection) + 1
print(score)
