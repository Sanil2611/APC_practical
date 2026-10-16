# Problem Statement:
# Create a dictionary containing Employee ID, Employee Name, Department,
# Salary, and Experience.
# Convert it into a Pandas DataFrame and:
# 1. Display employees with salary greater than 50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Rahul", "Amit", "Sneha", "Priya", "Rohan"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [60000, 45000, 55000, 70000, 48000],
    "Experience": [5, 3, 7, 8, 4]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
