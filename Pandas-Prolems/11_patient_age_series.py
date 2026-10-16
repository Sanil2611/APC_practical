# Problem Statement:
# Create a Pandas Series using a dictionary where patient IDs are the index
# and patient ages are the values.
# Perform:
# Find the average age.
# Find the oldest patient.
# Find the youngest patient.
# Display patients above 60 years.

import pandas as pd

data = {
    101: 65,
    102: 45,
    103: 72,
    104: 30,
    105: 68
}

series = pd.Series(data)

print("Series:")
print(series)

print("\nAverage Age:", series.mean())
print("Oldest Patient:", series.idxmax(), series.max())
print("Youngest Patient:", series.idxmin(), series.min())

print("\nPatients above 60 years:")
print(series[series > 60])
