with open("input.txt") as fin:
    calories = []
    cal = 0
    for line in fin:
        line = line.strip()
        if line == "":
            calories.append(cal)
            cal = 0
            continue
        cal += int(line)
    print(max(calories))
