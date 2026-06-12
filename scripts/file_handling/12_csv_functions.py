# Pandas CSV Functions - Explore and Analyze Data
import pandas as pd

FILE = "../../data/raw/panda_practise.csv"
f = pd.read_csv(FILE)

print("Column names:")
print(f.columns)
print("")

print("Statistical summary (numerical columns only):")
print(f.describe())
print("")

print("First 3 rows (head):")
print(f.head(3))
print("")

print("Last 3 rows (tail):")
print(f.tail(3))
print("")

print("Rows 3 to 9 (slicing):")
print(f[3:9])
print("")

print("Convert to NumPy array:")
print(f.to_numpy())
print("")

print("Sort by index descending:")
print(f.sort_index(axis=0, ascending=False).head())
print("")

# Modify specific cell
f.loc[0, "first_name"] = "python"
print("After modifying row 0 first_name:")
print(f.head(3))
print("")

# Select specific rows and columns
w = f.loc[[2, 3], ["first_name"]]
print("Select rows 2,3 and specific columns:")
print(w)
