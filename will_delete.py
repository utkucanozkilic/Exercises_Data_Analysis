import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"]})
result = df["name"].str.len()
print(result)