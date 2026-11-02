import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "Neha"],
    "Marks": [88, 76, 92],
}
df = pd.DataFrame(data)
print(df)
print("Average marks:", df["Marks"].mean())
