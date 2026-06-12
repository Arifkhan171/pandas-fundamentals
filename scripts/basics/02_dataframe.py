# Pandas DataFrame - Creation and Access
import pandas as pd

# Create DataFrame from list
x = [1, 2, 3, 4]
x2 = pd.DataFrame(x)
print("DataFrame from list:")
print(x2)
print("")

# Create DataFrame from dictionary
dic = {"name": ['python', 'java'], "rank": [1, 2], "learn": [1, 0]}
x3 = pd.DataFrame(dic)
print("DataFrame from dictionary:")
print(x3)
print("")

# Select specific columns
x3 = pd.DataFrame(dic, columns=["name"])
print("Select specific column:")
print(x3)
print("")

# Access specific cell
print("Access specific cell [name][1]:")
print(x3["name"][1])
