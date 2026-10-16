# Problem Statement:
# Create a dictionary containing Order_ID, Customer, Product, Quantity,
# Price, and Discount.
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount.
# Then display:
# All orders
# Orders above 5,000
# Highest-value order
# Average order value

import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Rahul", "Amit", "Sneha", "Priya", "Rohan"],
    "Product": ["Laptop", "Phone", "Monitor", "Tablet", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [60000, 30000, 12000, 20000, 15000],
    "Discount": [5000, 2000, 1000, 1500, 500]
}

df = pd.DataFrame(data)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:", df["Final_Amount"].mean())
