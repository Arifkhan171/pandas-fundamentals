# Pandas Merge and Concat
import pandas as pd

# --- MERGE ---
x1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})
x2 = pd.DataFrame({"A": [1, 2, 3, 4], "C": [22, 23, 242, 44]})

print("merge on column A (inner join by default):")
print(pd.merge(x1, x2, on="A"))
print("")

# Outer merge with indicator
x1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})
x2 = pd.DataFrame({"A": [1, 2, 3, 5], "C": [22, 23, 242, 44]})

print("outer merge - keeps all rows, NaN for missing:")
print(pd.merge(x1, x2, how="outer"))
print("")

print("outer merge with indicator column:")
print(pd.merge(x1, x2, how="outer", indicator=True))
print("")

# Merge on index
x1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})
x2 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [22, 23, 242, 44]})

print("merge on index (left_index + right_index):")
print(pd.merge(x1, x2, left_index=True, right_index=True))
print("")

# --- CONCAT ---
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([11, 31, 33, 43])

print("concat two Series:")
print(pd.concat([s1, s2]))
print("")

x1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})
x2 = pd.DataFrame({"A": [1, 2], "C": [22, 23]})

print("concat axis=1 (side by side):")
print(pd.concat([x1, x2], axis=1))
print("")

print("concat axis=1 with inner join:")
print(pd.concat([x1, x2], axis=1, join="inner"))
