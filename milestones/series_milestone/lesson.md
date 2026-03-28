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
