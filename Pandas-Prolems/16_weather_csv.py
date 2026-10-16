# Problem Statement:
# Dataset: weather.csv
# Columns:
# Date, City, Temperature, Humidity, Rainfall
# Read the CSV file and:
# 1. Find the maximum temperature.
# 2. Find the minimum temperature.
# 3. Calculate the average temperature.
# 4. Display records where temperature is above 35°C.
# 5. Calculate city-wise average temperature.

import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print("Average Temperature:", df["Temperature"].mean())

print("\nRecords where temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
