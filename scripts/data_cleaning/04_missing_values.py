# Pandas Missing Values - dropna and fillna
import pandas as pd

# Load dataset - update path if needed
csv = pd.read_csv("../../data/raw/panda_practise2.csv")
print("Original data:")
print(csv)
print("")

# Drop rows with any NaN
print("dropna() - remove rows with any NaN:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").dropna())
print("")

# Drop columns with NaN
print("dropna(axis=1) - remove columns with NaN:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").dropna(axis=1))
print("")

# Drop rows where ALL values are NaN
print("dropna(how='all') - remove rows where all values are NaN:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").dropna(how="all"))
print("")

# Drop rows where specific column has NaN
print("dropna(subset=['prices']) - remove rows where prices is NaN:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").dropna(subset=["prices"]))
print("")

# Fill NaN with a value
print("fillna('unknown') - fill all NaN with string:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").fillna("unknown"))
print("")

# Fill NaN column-specific values
print("fillna with column-specific values:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").fillna({"gender": "male", "prices": 0}))
print("")

# Forward fill
print("fillna(method='ffill') - forward fill:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").ffill())
print("")

# Fill with limit
print("fillna with limit=2:")
print(pd.read_csv("../../data/raw/panda_practise2.csv").fillna("unknown", limit=2))
