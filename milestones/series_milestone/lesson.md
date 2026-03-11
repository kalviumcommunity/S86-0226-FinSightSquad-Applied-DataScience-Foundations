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

Missing-values detection (isnull, sum, mean)

- Purpose: locate and quantify missing data before cleaning.
- Use `df.isnull()` to obtain a boolean mask of missing entries.
- Use `df.isnull().sum()` to count missing values per column.
- Use `df.isnull().mean()` to view proportions of missing values per column.
- Use `df[df.isnull().any(axis=1)]` to inspect rows that contain any missing values.

How to demonstrate (in the video)

1. Run the example script so the missing-values section prints.
2. Point out the per-column counts and proportions; mention columns with non-zero counts.
3. Open a few rows returned by `df[df.isnull().any(axis=1)]` and explain why row-level context matters.

---

## Standardizing Column Names and Data Formats

### Why standardization matters

Real-world datasets arrive from many sources — bank exports, spreadsheets, forms — each with its own naming style.
Inconsistent column names cause errors when merging datasets, make code harder to read, and create subtle bugs in analysis pipelines.
Standardizing early costs very little but saves significant debugging time later.

Common problems:
- `"Transaction Date"`, `"TransactionDate"`, `"txn_date"` all mean the same thing but can't be merged automatically.
- `"Amount"` stored as a string `"1,500.00"` silently blocks arithmetic.
- Mixed case categories like `"Shopping"`, `"SHOPPING"`, `"shopping"` are treated as different groups.

---

### 1. Standardizing column names

Goal: every column name should be lowercase, words separated by underscores, no special characters.

```python
# Strip whitespace, lowercase, replace non-alphanumeric runs with underscore
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)
```

Before: `["Date", "Narration", "Dr/Cr", "  Balance  ", "Ref# No"]`
After : `["date", "narration", "dr_cr", "balance", "ref_no"]`

---

### 2. Choosing a naming convention — snake_case

Rules for consistent column names:

- Use **snake_case**: all lowercase, words joined with `_`.
- Spell out abbreviations where possible (`transaction_date` not `txn_dt`).
- Keep names short but self-explanatory (`amount`, `transaction_type`, `account_balance`).
- Avoid leading digits (`1st_amount` → `first_amount`).

```python
import re

def to_snake_case(name: str) -> str:
    name = name.strip()
    name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)  # CamelCase → camel_case
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")

df.columns = [to_snake_case(c) for c in df.columns]
```

---

### 3. Standardizing text data

Goal: consistent case, no extra whitespace, uniform category values.

```python
# Lowercase + strip for category-like columns
df["category"] = df["category"].str.strip().str.lower()

# Title case + strip for human-readable descriptions
df["description"] = df["description"].str.strip().str.title()

# Lowercase for status/flag columns
df["status"] = df["status"].str.strip().str.lower()
```

Before `category` column: `["  shopping ", "FOOD", "food", "SHOPPING"]`
After                    : `["shopping",   "food", "food", "shopping"]` — 2 unique values, not 4.

---

### 4. Standardizing numeric and date formats

**Numbers stored as strings** (commas, currency symbols, extra spaces):

```python
df["amount"] = (
    df["amount"]
    .str.replace(",", "", regex=False)   # remove thousand-separator commas
    .str.strip()                          # remove surrounding whitespace
    .pipe(pd.to_numeric, errors="coerce") # cast; NaN for unparseable values
)
```

**Dates from multiple formats → ISO 8601 (`YYYY-MM-DD`)**:

```python
df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")
```

`pd.to_datetime` recognises `"01/01/2023"`, `"2023-01-01"`, `"January 1 2023"` and more.
Use `errors="coerce"` so unparseable entries become `NaT` instead of raising an exception.

---

### 5. Full standardization pipeline

Apply all steps together near the top of any cleaning script:

```python
def standardize(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Column names
    df.columns = (
        df.columns.str.strip().str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True).str.strip("_")
    )
    # 2. Dates
    for col in [c for c in df.columns if "date" in c]:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")
    # 3. Strip text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
    # 4. Numeric columns
    for col in [c for c in df.columns if any(h in c for h in ["amount", "balance"])]:
        df[col] = pd.to_numeric(
            df[col].astype(str).str.replace(",", "", regex=False), errors="coerce"
        )
    return df
```

---

### Key takeaways

- Standardize **first** — before filtering, merging, or analysing.
- Use `str.strip()`, `str.lower()`, `str.replace()` (with regex where needed) for column names.
- `pd.to_numeric(..., errors="coerce")` and `pd.to_datetime(..., errors="coerce")` are safe, non-crashing converters.
- Consistent naming conventions (`snake_case`) make column references predictable across the entire project.

### How to run the standardization examples

```bash
python milestones/series_milestone/series_milestone.py
```

Observe the `--- Standardization milestone examples ---` section in the output.
Compare the BEFORE and AFTER blocks to see the effect of each transformation.


