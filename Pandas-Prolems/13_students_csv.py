# Problem Statement:
# Dataset: students.csv
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
# Read students.csv using Pandas and perform:
# 1. Display the first 5 records.
# 2. Display the last 5 records.
# 3. Find the total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find the student with the highest average.
# 6. Find the average marks for each subject.

import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

subjects = ["Python", "DBMS", "Maths"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

print("\nStudent Total and Average:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage Marks for Each Subject:")
print(df[subjects].mean())
