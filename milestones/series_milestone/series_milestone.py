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

    print("--- End ---")
    
