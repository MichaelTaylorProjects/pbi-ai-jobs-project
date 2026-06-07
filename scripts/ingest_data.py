import pandas as pd
from pathlib import Path

# Define the path to the data directory
BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / 'data' / 'AI_Impact_on_Jobs_2030.csv'
output_file = BASE_DIR / 'data' / 'job_raw.csv'

# Read the input CSV file
df = pd.read_csv(input_file)

# Save as Parquet format
df.to_parquet(output_file, index=False)

print("Data has been ingested and saved as Parquet format at:", output_file)
print(df.head())
