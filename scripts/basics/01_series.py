# Pandas Series - Creation and Operations
import pandas as pd

# Create Series from list
x = [1, 2, 3, 4]
x2 = pd.Series(x, index=['a', 'b', 'c', 'd'], dtype='float', name='python series')
print("Series from list:")
print(x2)
print(type(x2))
print("")

# Create Series from dictionary
dic = {"name": ['python', 'java'], "rank": [1, 2], "learn": [1, 0]}
x3 = pd.Series(dic)
print("Series from dictionary:")
print(x3)
print("")

# Addition of two Series (NaN for missing indexes)
x = pd.Series([1, 2, 3, 4])
x2 = pd.Series([1, 2, 3, 4, 5, 6, 7])
print("Addition of two Series with different lengths:")
print(x + x2)
