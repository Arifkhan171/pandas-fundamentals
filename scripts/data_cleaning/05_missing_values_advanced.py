# Pandas Advanced Missing Values - replace and interpolate
import pandas as pd

csv = pd.read_csv("../../data/raw/panda_practise2.csv")

# Replace specific value
print("replace() - replace specific string value:")
r = csv.replace(to_replace="Genderfluid", value="male")
print(r)
print("")

# Replace using regex
print("replace with regex:")
print(csv.replace(["F"], ["f"], regex=True))
print("")

# Interpolate - fill NaN using linear interpolation
print("interpolate() - fill NaN linearly:")
r = csv.interpolate()
print(r)
print("")

# Interpolate with limit
print("interpolate(limit=2) - fill max 2 consecutive NaN:")
r = csv.interpolate(limit=2)
print(r)
print("")

# Interpolate forward only
print("interpolate(limit_direction='forward'):")
r = csv.interpolate(limit_direction="forward")
print(r)
