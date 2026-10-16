# Problem Statement:
# Create a Pandas Series using a dictionary where the student names are keys
# and their marks are values.
# Perform:
# Display the Series.
# Display marks of a particular student.
# Find maximum and minimum marks.
# Calculate the average marks.
# Display students who scored more than 75.

import pandas as pd

data = {
    "Rahul": 85,
    "Amit": 72,
    "Sneha": 90,
    "Priya": 68,
    "Rohan": 78
}

series = pd.Series(data)

print("Series:")
print(series)

print("\nMarks of Rahul:", series["Rahul"])
print("Maximum Marks:", series.max())
print("Minimum Marks:", series.min())
print("Average Marks:", series.mean())

print("\nStudents scoring more than 75:")
print(series[series > 75])
