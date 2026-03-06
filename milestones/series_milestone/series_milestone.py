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


if __name__ == "__main__":
    print("--- Pandas Series milestone examples ---\n")
    series_from_list()
    series_from_numpy()
    labeled_index_examples()
    compare_with_numpy()
    alignment_example()
    print("--- End ---")
