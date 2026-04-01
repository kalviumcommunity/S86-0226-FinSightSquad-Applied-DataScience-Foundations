2-minute Video Script — Pandas Series Milestone

Total length: ~2:00

0:00–0:10 (Intro)
- "Hi — in two minutes I'll show how to create Pandas Series from lists and NumPy arrays."

0:10–0:40 (Series from list)
- Show editor with `series_milestone.py`.
- Run the `series_from_list()` example.
- Narration: "A Series is a labeled 1D array. When created from a list, Pandas assigns a default integer index. Here you can see the `index` and `values`."

0:40–1:00 (Series from NumPy)
- Run `series_from_numpy()`.
- Narration: "When you create a Series from a NumPy array, the data type is preserved and you get the benefits of labels."

1:00–1:25 (Index vs values / access)
- Run `labeled_index_examples()` and show `.loc` vs `.iloc` usage.
- Narration: "`.loc` uses labels, `.iloc` uses positions — this difference matters when indexes are not simple integers."

1:25–1:50 (Compare with NumPy & alignment)
- Run `compare_with_numpy()` and `alignment_example()`.
- Narration: "Arithmetic on Series preserves labels and aligns data by labels, unlike NumPy arrays which operate position-wise."

1:50–2:00 (Wrap-up)
- "Series are lightweight and essential — they're the building blocks for DataFrames. That's it!"

Recording checklist
- Screen-facing camera visible, audio clear.
- Show code editor and terminal output.
- Keep video close to 2 minutes.
- Include link to `milestones/series_milestone/series_milestone.py` in submission notes.

---

2-minute Video Script — Standardizing Column Names and Data Formats

Total length: ~2:00

0:00–0:10 (Intro)
- "In this walkthrough I'll show how to standardize column names and data formats in Pandas — a critical first step for clean, reliable analysis."

0:10–0:35 (Standardizing column names)
- Open `series_milestone.py`, scroll to `standardize_column_names()`.
- Run the script and point to the BEFORE / AFTER output.
- Narration: "Raw column names often have spaces, mixed casing, and special characters. We use `.str.strip()`, `.str.lower()`, and a regex replace to turn them into clean snake_case names — simple to reference in code."
- Example shown: `"  Balance  "` → `"balance"`, `"Dr/Cr"` → `"dr_cr"`.

0:35–1:00 (Naming conventions)
- Point to `naming_conventions_demo()` output.
- Narration: "We convert camelCase names like `TransactionDate` and abbreviated names like `AcctBal` using a small helper. The rule is: always snake_case, always descriptive — `transaction_date`, `account_balance`. Consistent naming means fewer bugs when merging datasets."

1:00–1:25 (Standardizing text data)
- Point to `standardize_text_data()` output.
- Narration: "Category columns had four variants of 'shopping' and 'food'. After `.str.strip().str.lower()` we have exactly two. Description gets title-case. Status gets lowercase. Text consistency prevents groupby and merge errors downstream."

1:25–1:50 (Numeric and date formats)
- Point to `standardize_numeric_date_formats()` output — show dtypes before and after.
- Narration: "Amounts like `'1,500.00'` were strings. We remove commas with `.str.replace()` and call `pd.to_numeric()`. Dates in three different formats become a uniform ISO 8601 string `YYYY-MM-DD` using `pd.to_datetime()`. The dtype changes from object to float64 and date strings become consistent — now arithmetic and sorting work correctly."

1:50–2:00 (Wrap-up)
- Point to `full_standardization_pipeline()` running against the real sample CSV.
- Narration: "Putting it all together, a four-step pipeline — normalize names, parse dates, strip text, coerce numbers — transforms any messy CSV into an analysis-ready DataFrame. Standardize first, analyse second."

Recording checklist
- Show both BEFORE and AFTER blocks clearly in the terminal.
- Zoom in on the dtypes output so object → float64 changes are visible.
- Keep terminal font at 14pt or larger.
- Video should be approximately 2 minutes; no padding needed.
