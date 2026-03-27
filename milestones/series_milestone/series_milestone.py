"""Series milestone examples.
Run: python milestones/series_milestone/series_milestone.py
"""
import pandas as pd
import numpy as np


def series_from_list():
    data = [10, 20, 30, 40]
    s = pd.Series(data, name="numbers")
    print("Series from list:")
    print(s)
    print("Index:", s.index)
    print("Values:", s.values)
    print("Dtype:", s.dtype)
    print("Access by position (iloc):", s.iloc[1])
    print("Access by label (loc) with default index:", s.loc[1])
    print()


def series_from_numpy():
    arr = np.array([1.5, 2.5, 3.5])
    s = pd.Series(arr, name="floats")
    print("Series from NumPy array:")
    print(s)
    print("Index:", s.index)
    print("Values:", s.values)
    print("Dtype preserved from NumPy:", s.dtype)
    print()


def labeled_index_examples():
    s = pd.Series([100, 200, 300], index=["a", "b", "c"], name="labels")
    print("Series with custom labels:")
    print(s)
    print("Access by label (loc):", s.loc["b"])  # label-based
    print("Access by position (iloc):", s.iloc[1])   # positional
    print()


def compare_with_numpy():
    arr = np.array([1, 2, 3])
    s = pd.Series(arr, index=[0, 1, 2], name="nums")
    print("NumPy array + 1:", arr + 1)
    print("Series + 1:\n", s + 1)
    print()


def alignment_example():
    s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    s2 = pd.Series([10, 20], index=["b", "a"])  # different order / subset
    print("s1:\n", s1)
    print("s2:\n", s2)
    print("s1 + s2 (label-aligned):\n", s1 + s2)
    print()


def dataframe_inspection_example(csv_path=None):
    """Load a CSV and demonstrate head(), info(), and describe().

    If csv_path is None, try the project's `data/transactions.csv`,
    otherwise fall back to the first sample file available.
    """
    import os

    if csv_path is None:
        default = os.path.join(os.path.dirname(__file__), "..", "..", "data", "transactions.csv")
        default = os.path.normpath(default)
        if os.path.exists(default):
            csv_path = default
        else:
            # fallback to a sample in the data folder (relative to repo root)
            sample = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample_01_standard.csv")
            csv_path = os.path.normpath(sample)

    print("\n--- DataFrame inspection example ---")
    print(f"Loading: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print("Failed to load CSV:", e)
        return

    print("\n.head() preview:")
    print(df.head())

    print("\n.info() summary:")
    # info() writes to stdout directly
    df.info()

    print("\n.describe() statistics:")
    print(df.describe(include='number'))


def dataframe_missing_values_example(csv_path=None):
    """Demonstrate detecting and summarizing missing values in a DataFrame.

    Loads the same CSV fallback as the inspection example and prints:
    - boolean mask snippets, per-column counts, proportions
    - rows that contain any missing values (sample)
    """
    import os

    if csv_path is None:
        default = os.path.join(os.path.dirname(__file__), "..", "..", "data", "transactions.csv")
        default = os.path.normpath(default)
        if os.path.exists(default):
            csv_path = default
        else:
            sample = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample_01_standard.csv")
            csv_path = os.path.normpath(sample)

    print("\n--- Missing-values detection example ---")
    print(f"Loading: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print("Failed to load CSV:", e)
        return

    print("\nShow boolean mask for first 5 rows (isnull):")
    print(df.head().isnull())

    print("\nCount of missing values per column:")
    missing_counts = df.isnull().sum()
    print(missing_counts)

    print("\nProportion of missing values per column:")
    missing_prop = df.isnull().mean()
    print(missing_prop)

    print("\nTotal missing values in DataFrame:")
    print(int(missing_counts.sum()))

    print("\nRows that contain any missing values (sample 5):")
    rows_with_missing = df[df.isnull().any(axis=1)]
    if len(rows_with_missing) == 0:
        print("No rows with missing values found.")
    else:
        print(rows_with_missing.head())




# ---------------------------------------------------------------------------
# Standardization milestone
# ---------------------------------------------------------------------------

def standardize_column_names():
    """Clean and normalize column headers to consistent snake_case."""
    import re

    raw_columns = ["Date", "Narration", "Amount", "Dr/Cr", "  Balance  ", "Ref# No", "ValueDATE"]
    data = [["01/01/2023", "Amazon Purchase", 4254.62, "Dr", 15000.00, "REF001", "01/01/2023"]]
    df = pd.DataFrame(data, columns=raw_columns)

    print("\n--- Standardize Column Names ---")
    print("BEFORE — raw column names:")
    print(list(df.columns))

    # Step 1: strip leading/trailing whitespace
    df.columns = df.columns.str.strip()
    # Step 2: convert to lowercase
    df.columns = df.columns.str.lower()
    # Step 3: replace any run of non-alphanumeric characters with underscore
    df.columns = df.columns.str.replace(r"[^a-z0-9]+", "_", regex=True)
    # Step 4: strip trailing/leading underscores that may remain
    df.columns = df.columns.str.strip("_")

    print("AFTER  — cleaned snake_case column names:")
    print(list(df.columns))
    print()
    return df


def naming_conventions_demo():
    """Show how to convert mixed-style names (camelCase, abbreviations) to snake_case."""
    import re

    messy = {
        "TransactionDate": "2023-01-01",
        "TXN AMT": 1500.00,
        "Ref No.": "REF001",
        "Debit/Credit": "Dr",
        "AcctBal": 10000.00,
    }
    df = pd.DataFrame([messy])

    print("\n--- Naming Conventions Demo (snake_case) ---")
    print("BEFORE:")
    print(list(df.columns))

    def to_snake_case(name: str) -> str:
        """Convert any column name to snake_case."""
        name = name.strip()
        # Insert underscore before uppercase letters that follow lowercase (CamelCase)
        name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)
        name = name.lower()
        # Replace any non-alphanumeric sequence with a single underscore
        name = re.sub(r"[^a-z0-9]+", "_", name)
        return name.strip("_")

    df.columns = [to_snake_case(c) for c in df.columns]

    print("AFTER  (snake_case — descriptive, no abbreviations):")
    print(list(df.columns))
    print(df.to_string(index=False))
    print()


def standardize_text_data():
    """Normalize string values: case, whitespace, and category consistency."""
    raw = {
        "Category": ["  shopping ", "FOOD", "Transport", "food", "SHOPPING", "transport"],
        "Description": ["Amazon Purchase", "  swiggy order  ", "Uber Ride", "Zomato ", " BookMyShow", "Ola Cab"],
        "Status": ["DEBIT", "debit", "Debit", "credit", "CREDIT", "Credit"],
    }
    df = pd.DataFrame(raw)

    print("\n--- Standardize Text Data ---")
    print("BEFORE:")
    print(df.to_string(index=False))

    # Strip whitespace then lowercase for categorical columns
    df["category"] = df["Category"].str.strip().str.lower()
    # Strip whitespace then title-case for descriptive text
    df["description"] = df["Description"].str.strip().str.title()
    # Strip whitespace then lowercase for status values
    df["status"] = df["Status"].str.strip().str.lower()

    df = df.drop(columns=["Category", "Description", "Status"])

    print("\nAFTER:")
    print(df.to_string(index=False))
    print("\nUnique categories:", df["category"].unique().tolist())
    print("Unique statuses  :", df["status"].unique().tolist())
    print()


def standardize_numeric_date_formats():
    """Ensure numeric columns hold proper floats and dates follow ISO 8601."""
    raw = {
        "date":    ["01/01/2023", "2023-02-15", "March 5, 2023", "04-01-2023"],
        "amount":  ["1,500.00",   "2500",        " 300.50 ",      "4,000"],
        "balance": ["10,000.50",  "8500",        "12,300.75",     "6,000"],
    }
    df = pd.DataFrame(raw)

    print("\n--- Standardize Numeric and Date Formats ---")
    print("BEFORE:")
    print(df.to_string(index=False))
    print("Dtypes before:")
    print(df.dtypes)

    # Remove thousand-separator commas and strip whitespace, then cast to float
    for col in ["amount", "balance"]:
        df[col] = (
            df[col]
            .str.replace(",", "", regex=False)
            .str.strip()
            .pipe(pd.to_numeric, errors="coerce")
        )

    # Parse dates — format="mixed" lets pandas handle each entry individually (pandas >= 2.0)
    df["date"] = pd.to_datetime(df["date"], format="mixed", errors="coerce").dt.strftime("%Y-%m-%d")

    print("\nAFTER:")
    print(df.to_string(index=False))
    print("Dtypes after:")
    print(df.dtypes)
    print()


def full_standardization_pipeline(csv_path=None):
    """End-to-end standardization demo using one of the project sample CSVs."""
    import os

    if csv_path is None:
        candidates = [
            os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample_02_bank_export.csv"),
            os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample_01_standard.csv"),
            os.path.join(os.path.dirname(__file__), "..", "..", "data", "transactions.csv"),
        ]
        csv_path = next(
            (os.path.normpath(p) for p in candidates if os.path.exists(os.path.normpath(p))),
            None,
        )
        if csv_path is None:
            print("No sample CSV found — skipping pipeline demo.")
            return

    print("\n--- Full Standardization Pipeline ---")
    print(f"Loading: {csv_path}")
    df = pd.read_csv(csv_path)

    print("\nBEFORE standardization:")
    print("Column names:", list(df.columns))
    print(df.head(3).to_string(index=False))

    # ── 1. Normalize column names ──────────────────────────────────────────
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    # ── 2. Parse and reformat date columns ────────────────────────────────
    date_cols = [c for c in df.columns if "date" in c]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")

    # ── 3. Strip whitespace from all remaining string columns ──────────────
    # include both 'object' (pandas < 3) and 'str' / 'string' (pandas >= 3)
    obj_cols = set(df.select_dtypes(include="object").columns)
    try:
        obj_cols |= set(df.select_dtypes(include="str").columns)
    except Exception:
        pass
    for col in obj_cols:
        if col not in date_cols:
            df[col] = df[col].str.strip()

    # ── 4. Coerce amount/balance-like columns to numeric ──────────────────
    numeric_hints = ["amount", "balance", "debit", "credit"]
    for col in df.columns:
        if any(h in col for h in numeric_hints):
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "", regex=False).str.strip(),
                errors="coerce",
            )

    print("\nAFTER standardization:")
    print("Column names:", list(df.columns))
    print(df.head(3).to_string(index=False))
    print("Dtypes:")
    print(df.dtypes)
    print()


if __name__ == "__main__":
    print("--- Pandas Series milestone examples ---\n")
    series_from_list()
    series_from_numpy()
    labeled_index_examples()
    compare_with_numpy()
    alignment_example()
    # Run the DataFrame inspection example too (helpful for this milestone)
    dataframe_inspection_example()
    # Run missing-values demo
    dataframe_missing_values_example()

    print("\n--- Standardization milestone examples ---\n")
    standardize_column_names()
    naming_conventions_demo()
    standardize_text_data()
    standardize_numeric_date_formats()
    full_standardization_pipeline()

    print("--- End ---")
    
