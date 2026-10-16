# Problem Statement:
# Create a dictionary containing Product ID, Product Name, Category, Price,
# and Quantity. Convert it into a DataFrame.
# Calculate Total Amount = Price × Quantity.
# Then find the product having the highest total sales.

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Phone", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [60000, 30000, 800, 1500, 12000],
    "Quantity": [2, 5, 20, 15, 4]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])
