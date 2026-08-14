runs = (45, 78, 23, 56, 91, 34, 67, 12, 85, 50)

total = sum(runs)
highest = runs[0]
lowest = runs[0]

for run in runs:
    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total Runs =", total)
print("Highest Score =", highest)
print("Lowest Score =", lowest)
print("Average Score =", average)
