# Problem Statement:
# Dataset: employees.csv
# Columns:
# Employee_ID, Name, Department, Experience, Salary
# Read the CSV file and:
# 1. Display employees from the CSE department.
# 2. Find the average salary.
# 3. Find the highest and lowest salary.
# 4. Display employees having salary greater than 50,000.
# 5. Calculate department-wise average salary.

import pandas as pd

df = pd.read_csv("employees.csv", sep=",", encoding="utf-8")

print(df.columns.tolist())

print("Employees from CSE department:")
print(df[df["Department"] == "CSE"])

print("Average salary:")
print(df["Salary"].mean())

print("Highest salary:")
print(df["Salary"].max())

print("Lowest salary:")
print(df["Salary"].min())

print("Employees having salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("Department-wise average salary:")
print(df.groupby("Department")["Salary"].mean())