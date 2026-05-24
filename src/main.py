import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# File paths
INPUT_FILE = "../data/raw_data.xlsx"
OUTPUT_FILE = "../output/cleaned_data.xlsx"

logging.info("Starting data cleaning process...")

# Check if input file exists
if not os.path.exists(INPUT_FILE):
    logging.error(f"File not found: {INPUT_FILE}")
    exit()

# Read file based on extension
if INPUT_FILE.endswith(".csv"):
    df = pd.read_csv(INPUT_FILE)
    logging.info("CSV file loaded successfully.")
else:
    df = pd.read_excel(INPUT_FILE)
    logging.info("Excel file loaded successfully.")

logging.info(f"Original rows: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

logging.info(f"Rows after removing duplicates: {len(df)}")

# Fill missing values
df = df.fillna("N/A")

logging.info("Missing values handled.")

# Standardize column names
df.columns = [
    col.strip().lower().replace(" ", "_")
    for col in df.columns
]

logging.info("Column names standardized.")

# Create output directory if not exists
os.makedirs("../output", exist_ok=True)

# Save cleaned file
df.to_excel(OUTPUT_FILE, index=False)

logging.info("Cleaned dataset exported successfully.")
logging.info(f"Output saved to: {OUTPUT_FILE}")