import pandas as pd
import os

# File paths
INPUT_FILE = "../data/raw_data.xlsx"
OUTPUT_FILE = "../output/cleaned_data.xlsx"

print("Loading dataset...")

# Read Excel file
df = pd.read_excel(INPUT_FILE)

print(f"Original rows: {len(df)}")

# Remove duplicate rows
df = df.drop_duplicates()

print(f"Rows after removing duplicates: {len(df)}")

# Fill missing values
df = df.fillna("N/A")

# Standardize column names
df.columns = [
    col.strip().lower().replace(" ", "_")
    for col in df.columns
]

# Create output directory if not exists
os.makedirs("../output", exist_ok=True)

# Save cleaned data
df.to_excel(OUTPUT_FILE, index=False)

print("Data cleaned successfully!")
print(f"Cleaned file saved to: {OUTPUT_FILE}")