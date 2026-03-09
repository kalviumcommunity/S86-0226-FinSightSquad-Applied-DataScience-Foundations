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
