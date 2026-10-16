# Problem Statement:
# Create a Pandas Series using a dictionary containing product names and prices.
# Perform:
# Display all products and prices.
# Increase every price by 10%.
# Find the most expensive product.
# Find products costing more than 1,000.

import pandas as pd

data = {
    "Laptop": 60000,
    "Phone": 30000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

series = pd.Series(data)

print("Products and Prices:")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)

print("\nMost expensive product:")
print(series.idxmax(), series.max())

print("\nProducts costing more than 1000:")
print(series[series > 1000])
