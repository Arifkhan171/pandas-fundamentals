# Pandas GroupBy - Grouping and Aggregation
import pandas as pd

df = pd.DataFrame({
    "name": ["arif", "faiz", "ajab", "faiz", "arif", "ajab", "arif", "faiz", "ajab"],
    "math": [11, 12, 23, 12, 15, 19, 21, 14, 19],
    "urdu": [11, 12, 12, 14, 16, 18, 21, 32, 43]
})

print("Original DataFrame:")
print(df)
print("")

# GroupBy - iterate groups
print("GroupBy name - iterate each group:")
grouped = df.groupby("name")
for name, group in grouped:
    print(f"Group: {name}")
    print(group)
    print("")

# Get specific group
print("get_group('arif'):")
print(grouped.get_group("arif"))
print("")

# Aggregation functions
print("min() per group:")
print(grouped.min())
print("")

print("max() per group:")
print(grouped.max())
print("")

print("sum() per group:")
print(grouped.sum())
print("")

print("mean() per group:")
print(grouped.mean())
