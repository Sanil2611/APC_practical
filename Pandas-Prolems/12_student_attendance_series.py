import pandas as pd

data = {
    "Sanil": 85,
    "Shubham": 70,
    "Parshvanath": 92,
    "Pratik": 65,
    "Prathmesh": 95
}

series = pd.Series(data)

print("Average Attendance:", series.mean())

print("\nAttendance below 75%:")
print(series[series < 75])

print("\nAttendance above 90%:")
print(series[series > 90])

print("\nHighest Attendance:", series.max())
