# Problem Statement:
# Create a Pandas Series using a dictionary containing employee names and their salaries.
# Perform:
# Display the Series.
# Find the highest salary.
# Find the lowest salary.
# Calculate average salary.
# Display employees earning more than 50,000.

import pandas as pd

data = {
    "Rahul": 60000,
    "Amit": 45000,
    "Sneha": 55000,
    "Priya": 70000,
    "Rohan": 48000
}

series = pd.Series(data)

print("Series:")
print(series)

print("\nHighest Salary:", series.max())
print("Lowest Salary:", series.min())
print("Average Salary:", series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])
