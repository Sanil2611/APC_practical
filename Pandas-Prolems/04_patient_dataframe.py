# Problem Statement:
# Create a dictionary containing Patient ID, Patient Name, Age, Disease,
# and Medical Charges. Convert the dictionary into a DataFrame and:
# 1. Display patients above 60 years.
# 2. Find the average medical charge.
# 3. Find the maximum medical charge.
# 4. Display patients whose medical charges are greater than 50,000.

import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Patient_Name": ["Rahul", "Amit", "Sneha", "Priya", "Rohan"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Cold", "Cancer"],
    "Medical_Charges": [60000, 15000, 90000, 10000, 75000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])
