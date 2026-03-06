# Loading CSV Data into Pandas DataFrames Milestone

## Overview

This milestone focuses on loading CSV data into Pandas DataFrames correctly.
CSV is one of the most common tabular formats in data workflows, and correct loading is the first checkpoint before analysis.

## Learning Objectives

By completing this milestone, you will be able to:

- Understand what CSV files represent
- Load CSV files into Pandas DataFrames
- Interpret headers, rows, and columns correctly
- Inspect loaded data for correctness
- Recognize common CSV loading issues

## Why This Matters

Most downstream analysis issues start at data loading.
Common beginner mistakes include:

- Incorrect column names after loading
- Data shifted into wrong columns
- Assuming the data is correct without inspection
- Analysis errors caused by bad loading steps

This milestone ensures:

- Data is loaded as expected
- Dataset structure is clearly understood
- Problems are caught early
- Further analysis is more reliable

## Scope

This is a Pandas fundamentals milestone, not a data analysis task.

Included:

- Loading a CSV into a DataFrame
- Inspecting structure and columns
- Verifying row and column counts
- Identifying basic loading issues

Not included:

- Data cleaning
- Data transformation
- Feature creation

## File Structure

```
scripts/
  - loading_csv_data_milestone.py

data/
  raw/
    - sample_transactions.csv
```

## How to Run

From the project root:

```bash
python scripts/loading_csv_data_milestone.py
```

## What the Script Demonstrates

### 1. Understanding CSV Files

- Header row vs data rows
- Comma delimiter concept
- CSV as table-like structure

### 2. Loading CSV Files into Pandas

- Uses `pd.read_csv()`
- Verifies file path before loading
- Creates DataFrame successfully

### 3. Inspecting Loaded Data

- `df.head()` for preview
- `df.columns.tolist()` for column names
- `df.shape` for row and column counts
- `df.info()` for quick structure summary

### 4. Recognizing Common Loading Issues

- Mismatched column names
- Missing or extra columns
- Zero-row loads
- Why immediate inspection matters

## Expected CSV Schema

The script checks against this expected column order:

- `Date`
- `Category`
- `Amount`
- `Type`
- `Payment_Method`

## Submission Checklist

- [ ] Script runs without errors
- [ ] CSV file loads into a DataFrame
- [ ] First rows are previewed correctly
- [ ] Column names are printed and verified
- [ ] Row and column counts are printed
- [ ] Common loading checks are performed

## Key Reminder

Loading a CSV is like opening a dataset.
Always inspect what you opened before moving forward.
