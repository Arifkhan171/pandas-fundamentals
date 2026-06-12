# Pandas Read CSV - All Important Parameters
import pandas as pd

FILE = "../../data/raw/panda_practise.csv"

# Basic read
print("Basic read_csv:")
f = pd.read_csv(FILE)
print(f.head())
print("")

# Read only specific number of rows
print("nrows=3 - read only 3 rows:")
print(pd.read_csv(FILE, nrows=3))
print("")

# Read specific columns by name
print("usecols by name:")
print(pd.read_csv(FILE, usecols=["id", "first_name"]))
print("")

# Read specific columns by index
print("usecols by index position:")
print(pd.read_csv(FILE, usecols=[0, 1, 3]))
print("")

# Skip specific rows
print("skiprows=[2,3]:")
print(pd.read_csv(FILE, skiprows=[2, 3]).head())
print("")

# Set index column
print("index_col='first_name':")
print(pd.read_csv(FILE, index_col=["first_name"]).head())
print("")

# Read without header
print("header=None - treat first row as data:")
print(pd.read_csv(FILE, header=None).head())
print("")

# Custom column names
cols = ["col1", "col2", "col3", "col4", "col5",
        "col6", "col7", "col8", "col9", "col10"]
print("Custom column names:")
print(pd.read_csv(FILE, names=cols).head())
