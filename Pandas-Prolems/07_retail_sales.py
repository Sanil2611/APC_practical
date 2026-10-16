# Problem Statement:
# A retail shop maintains sales information in a Python dictionary containing
# Product_ID, Product_Name, Category, Price, and Quantity.
# Write a Python program to:
# 1. Convert the dictionary into a Pandas DataFrame.
# 2. Add a new column Total_Sales.
# 3. Calculate total sales using Price × Quantity.
# 4. Display products with sales greater than 10,000.
# 5. Find the product with maximum sales.
# 6. Calculate the average sales.

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Mouse", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [60000, 30000, 800, 12000, 15000],
    "Quantity": [2, 5, 20, 3, 2]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:", df["Total_Sales"].mean())
