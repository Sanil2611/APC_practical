# Problem Statement:
# Create a dictionary containing Student_ID, Name, Department, Total_Classes,
# and Classes_Attended. Create a DataFrame and calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100.
# Display students whose attendance is below 75%.

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Amit", "Sneha", "Priya", "Rohan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [85, 70, 92, 65, 78]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)
print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])
