"""
Loading CSV Data into Pandas DataFrames Milestone
================================================
This script demonstrates the fundamentals of loading CSV data into Pandas,
then validating that the structure is interpreted correctly.

Scope:
- Load CSV files into DataFrames
- Inspect headers, rows, and columns
- Verify structure and basic correctness
- Recognize common loading issues

Out of scope:
- Data cleaning
- Data transformation
- Feature engineering
"""

import os
import pandas as pd


print("=" * 70)
print("LOADING CSV DATA INTO PANDAS DATAFRAMES")
print("=" * 70)

# Build a stable path from this script location to data/raw/sample_transactions.csv.
script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, ".."))
csv_path = os.path.join(project_root, "data", "raw", "sample_transactions.csv")

print("\n1. UNDERSTANDING CSV FILES")
print("-" * 70)
print(
    "A CSV (Comma-Separated Values) file stores table data as plain text:\n"
    "- Row 1 is usually the header (column names).\n"
    "- Each following row is one data record.\n"
    "- Commas separate fields into columns.\n"
)

print("2. LOADING CSV FILE INTO PANDAS")
print("-" * 70)
print(f"Expected CSV path: {csv_path}")

if not os.path.exists(csv_path):
    print("ERROR: CSV file was not found.")
    print("Check that data/raw/sample_transactions.csv exists.")
    raise SystemExit(1)

# Standard CSV loading method in Pandas.
df = pd.read_csv(csv_path)
print("CSV loaded successfully into DataFrame.")

print("\n3. INSPECTING LOADED DATA")
print("-" * 70)
print("Preview (first 5 rows):")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

row_count, column_count = df.shape
print("\nDataFrame shape:")
print(f"Rows: {row_count}")
print(f"Columns: {column_count}")

print("\nDataFrame info:")
df.info()

print("\n4. CHECKING FOR COMMON LOADING ISSUES")
print("-" * 70)
expected_columns = ["Date", "Category", "Amount", "Type", "Payment_Method"]

if df.columns.tolist() != expected_columns:
    print("Potential issue: column names differ from expected schema.")
    print(f"Expected: {expected_columns}")
    print(f"Actual:   {df.columns.tolist()}")
else:
    print("Column names match the expected schema.")

if column_count != len(expected_columns):
    print("Potential issue: unexpected number of columns detected.")

if row_count == 0:
    print("Potential issue: file loaded but has zero data rows.")
else:
    print(f"Row count check passed: {row_count} rows loaded.")

print(
    "\nNote: This milestone focuses on loading and structure validation only.\n"
    "No data cleaning or transformation is performed."
)

print("\n" + "=" * 70)
print("MILESTONE COMPLETE")
print("=" * 70)
