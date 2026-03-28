Pandas Series — Milestone Lesson

Goal
- Understand what a Pandas Series is and how to create one from Python lists and NumPy arrays.

What is a Series?
- A one-dimensional labeled array capable of holding any data type.
- Think of it as a NumPy array with an index (labels).

Tasks covered in the examples
1. Create a Series from a Python list (automatic integer index).
2. Create a Series from a NumPy array (dtype preserved).
3. Inspect `index` and `values`.
4. Access by position (`.iloc`) and by label (`.loc`).
5. Compare simple operations with NumPy arrays.
6. Show label-aware alignment when combining Series.

Files
- Example script: milestones/series_milestone/series_milestone.py
- Video script: milestones/series_milestone/video_script.md

How to run the examples

Open a terminal (activate your venv if needed) and run:

```bash
python milestones/series_milestone/series_milestone.py
```

What to observe when running
- Printed Series objects show both index and values.
- `s.index` returns the labels; `s.values` returns a NumPy array of the data.
- `.loc` is label-based, `.iloc` is position-based.
- Adding two Series aligns by labels (not by position), which is different from raw NumPy arrays.

Quick tips
- If you create a Series from a list, Pandas assigns a default integer index (0..n-1).
- Use custom indexes for more meaningful labels: e.g., dates, categories, or IDs.
- Use Series as building blocks for DataFrames later.

DataFrame inspection (head, info, describe)

- Purpose: quickly understand structure, types, and numeric summaries before cleaning.
- Use `head()` to preview the first rows and check column alignment and sample values.
- Use `info()` to view column names, data types, non-null counts, and memory usage.
- Use `describe()` to get count, mean, std, min/max and percentiles for numeric columns.

How to run the inspection example

1. Run the example script which loads a CSV and prints the outputs:

```bash
python milestones/series_milestone/series_milestone.py
```

2. Observe the terminal output:
- The `.head()` section shows sample rows and column headers.
- The `.info()` section lists dtypes and non-null counts — look for unexpected object types or missing values.
- The `.describe()` section provides numeric distributions; large differences between min/max/percentiles may indicate outliers.

Video guidance (~2 minutes)

- Demonstrate running the script and show each inspection step (`head()`, `info()`, `describe()`).
- Explain in one sentence what each method reveals and one example observation (e.g., a column with many nulls).
- Keep the screen capture clear and the terminal font large enough to read.

