import pandas as pd

# Baca file Parquet
df = pd.read_parquet("data.parquet")

# Tampilkan data
print(df)
