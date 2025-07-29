import pandas as pd

# 1. Create a DataFrame (like a table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Chennai']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Access columns
print("\nNames:", df['Name'])

# 3. Filter rows
adults = df[df['Age'] > 28]
print("\nPeople older than 28:\n", adults)

# 4. Add a new column
df['Salary'] = [50000, 60000, 70000]
print("\nWith Salary column:\n", df)

# 5. Basic stats
print("\nAverage Age:", df['Age'].mean())
print("Maximum Salary:", df['Salary'].max())

# 6. Read CSV file (example)
# df_from_csv = pd.read_csv("yourfile.csv")
# print("\nCSV Data:\n", df_from_csv)
