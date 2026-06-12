# Pandas Insert and Delete Columns
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [11, 22, 33, 44, 55]})
print("Original DataFrame:")
print(df)
print("")

# Insert column at specific position
df.insert(1, "C", [2, 4, 65, 7, 5])
print("After insert column C at position 1:")
print(df)
print("")

# Add column using assignment
df2 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [11, 22, 33, 44, 55]})
df2.insert(2, "D", df2["A"])
print("Insert column D as copy of A:")
print(df2)
print("")

# Delete column using pop
df3 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [11, 22, 33, 44, 55], "C": [21, 22, 23, 24, 25]})
print("Before pop:")
print(df3)
df3.pop("B")
print("After pop('B'):")
print(df3)
print("")

# Delete column using drop
df4 = pd.DataFrame({"A": [1, 2, 3], "B": [11, 22, 33], "C": [21, 22, 23]})
print("drop column using drop():")
print(df4.drop(columns=["B"]))
