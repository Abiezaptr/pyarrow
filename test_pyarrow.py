import pyarrow.csv as pv
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd

# 1. Baca CSV ke dalam PyArrow Table
table = pv.read_csv("data.csv")
print("Data dalam PyArrow Table:")
print(table)

# 2. Simpan ke format Parquet
pq.write_table(table, "data.parquet")
print("\nData telah disimpan dalam format Parquet.")

# 3. Baca kembali file Parquet
table_baru = pq.read_table("data.parquet")

# 4. Konversi ke Pandas DataFrame untuk ditampilkan
df = table_baru.to_pandas()
print("\nData dalam Pandas DataFrame:")
print(df)
