# Part one
elves = []
calories = 0
with open('cal.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line == '':
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)
            
print(max(elves))

# Part two
sorted_cals = sorted(elves, reverse=True)
print(sum(sorted_cals[:3]))

    