from app.datasets.paths import GENERAL_DATASET
import pandas as pd
import sqlite3
import os

 
db_folder = "app/databases"
os.makedirs(db_folder, exist_ok=True)  
db_path = os.path.join(db_folder, "general_dataset.db")

chunk_size = 10000 
chunks = pd.read_csv(GENERAL_DATASET, chunksize=chunk_size, dtype=str, low_memory=False)

conn = sqlite3.connect(db_path)

for chunk in chunks:
    chunk.to_sql("physicians", conn, if_exists="append", index=False)

conn.execute("CREATE INDEX idx_full_name ON physicians (covered_recipient_first_name, covered_recipient_last_name);")
conn.commit()
conn.close()

print(f"Database created at {db_path} and indexed on first_name and last_name.")
