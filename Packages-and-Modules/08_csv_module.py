import csv

rows = [
    ["Name", "Marks"],
    ["Asha", 88],
    ["Ravi", 76],
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Created students.csv")
