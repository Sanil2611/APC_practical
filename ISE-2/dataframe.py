import pandas as pd

data = {
    'Name': ['Amit', 'Priya', None, 'Rahul'],
    'Age': [20, None, 21, 22],
    'Marks': [80, 90, None, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df['Name'] = df['Name'].fillna('Sanil')
df['Age'] = df['Age'].fillna(21)
df['Marks'] = df['Marks'].fillna(80)

print("\nAfter replacing missing values:")
print(df)
