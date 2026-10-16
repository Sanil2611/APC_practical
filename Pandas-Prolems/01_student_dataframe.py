# Problem Statement:
# Create a dictionary containing the following information for 5 students:
# Student ID, Student Name, Python Marks, DBMS Marks, Mathematics Marks.
# Convert the dictionary into a Pandas DataFrame and:
# 1. Display the DataFrame.
# 2. Calculate total marks for each student.
# 3. Calculate average marks.
# 4. Display students who scored more than 75% average.

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Rahul", "Amit", "Sneha", "Priya", "Rohan"],
    "Python": [85, 72, 90, 68, 78],
    "DBMS": [80, 75, 88, 70, 82],
    "Mathematics": [90, 70, 85, 65, 80]
}

df = pd.DataFrame(data)

df["Total"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Mathematics"]].mean(axis=1)

print(df)
print("\nStudents with average above 75:")
print(df[df["Average"] > 75])
