# Pandas CSV Writing - to_csv and variations
import pandas as pd

dic = {"a": [1, 2, 3, 4, 5], "b": [11, 12, 13, 14, 15]}
df = pd.DataFrame(dic)

print("Original DataFrame:")
print(df)
print("")

# Write with index
df.to_csv("../../data/raw/output_with_index.csv")
print("Saved output_with_index.csv (includes row numbers)")

# Write without index
df.to_csv("../../data/raw/output_no_index.csv", index=False)
print("Saved output_no_index.csv (no row numbers)")

# Write with custom headers
df.to_csv("../../data/raw/output_custom_header.csv", index=False, header=["col_a", "col_b"])
print("Saved output_custom_header.csv (custom column names)")
