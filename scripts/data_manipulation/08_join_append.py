# Pandas Join and Append
import pandas as pd

# --- JOIN ---
d1 = pd.DataFrame({"arif": [2, 3, 4, 5], "gul": [11, 12, 13, 14]})
d2 = pd.DataFrame({"ajab": [21, 31], "sattar": [22, 22]})

print("join (default left join):")
print(d1.join(d2))
print("")

print("d2.join(d1) - smaller joins larger:")
print(d2.join(d1))
print("")

print("join with how='outer' (union):")
print(d2.join(d1, how="outer"))
print("")

# --- APPEND (using pd.concat as modern alternative) ---
d1 = pd.DataFrame({"arif": [2, 3, 4, 5], "gul": [11, 12, 13, 14]})
d2 = pd.DataFrame({"ajab": [21, 31], "gul": [22, 22]})

print("append DataFrames (pd.concat rows):")
print(pd.concat([d1, d2], ignore_index=True))
