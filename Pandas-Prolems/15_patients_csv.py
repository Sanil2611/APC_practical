# Problem Statement:
# Dataset: patients.csv
# Columns:
# Patient_ID, Name, Age, Gender, Disease, Medical_Expense
# Read the CSV file and:
# 1. Display patients above 60 years.
# 2. Calculate average medical expense.
# 3. Find the patient with the highest medical expense.
# 4. Count patients for each disease.
# 5. Display patients whose medical expense exceeds 50,000.

import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense:", df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

print("\nPatient count for each disease:")
print(df["Disease"].value_counts())

print("\nPatients with medical expense above 50000:")
print(df[df["Medical_Expense"] > 50000])
