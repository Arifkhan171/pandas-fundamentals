# Pandas Pivot Table and Melt
import pandas as pd

df = pd.DataFrame({
    "days": [2, 3, 4, 5],
    "students": ["a", "b", "c", "d"],
    "math": [11, 12, 13, 14],
    "eng": [21, 31, 41, 15]
})

print("Original DataFrame:")
print(df)
print("")

# Pivot table
print("pivot(index='students', columns='days'):")
print(df.pivot(index="students", columns="days"))
print("")

# Melt - reshape wide to long format
print("melt(id_vars='days') - wide to long format:")
print(pd.melt(df, id_vars="days"))
print("")

print("melt with custom names:")
print(pd.melt(df, id_vars="days",
              value_vars=["math", "eng"],
              var_name="subject",
              value_name="score"))
