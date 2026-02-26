Data Organization Milestone — helper script

Usage

- Ensure you have some files in `data/raw/` (these are your untouched inputs).
- Run:

```bash
python scripts/organize_data.py
```

What it does

- Creates required folders if missing (`data/raw`, `data/processed`, `outputs/`).
- Copies files from `data/raw/` into `data/processed/` without modifying the originals.
- Prevents any writes into `data/raw/` to avoid contamination.

Notes

- This is an instructional example — adapt processing logic inside `organize_data.py` when performing real transforms.
- Do not edit files inside `data/raw/`.
