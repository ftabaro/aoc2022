def main(path: str) -> int:
    with open(path) as fin:
        calories = []
        cal = 0
        for line in fin:
            line = line.strip()
            if line == "":
                calories.append(cal)
                cal = 0
                continue
            cal += int(line)
        
        res = max(calories)
        print(res)
        return res

if __name__ == "__main__":
    import sys
    main(sys.argv[1])