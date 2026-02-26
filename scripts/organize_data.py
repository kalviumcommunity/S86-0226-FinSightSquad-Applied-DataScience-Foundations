#!/usr/bin/env python3
"""
Example helper to demonstrate safe data flow:

- Reads files from `data/raw/` (source)
- Writes copies into `data/processed/` (destination)
- Refuses to write into `data/raw/` to prevent contamination

Run: `python scripts/organize_data.py`
"""
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
OUTPUTS = ROOT / "outputs"


def ensure_dirs():
    for p in (RAW, PROCESSED, OUTPUTS, OUTPUTS / "figures", OUTPUTS / "reports"):
        p.mkdir(parents=True, exist_ok=True)


def safe_copy_to_processed(src: Path, dest_name: str):
    src = src.resolve()
    # Protect raw: never write into data/raw
    dest = PROCESSED / dest_name
    if RAW in dest.resolve().parents or dest.resolve() == RAW.resolve():
        raise RuntimeError("Refusing to write into data/raw/")
    shutil.copy2(src, dest)
    print(f"Copied {src} -> {dest}")


def main():
    ensure_dirs()
    files = sorted([p for p in RAW.iterdir() if p.is_file()])
    if not files:
        print(f"No files found in {RAW!s}. Add raw files and re-run the script.")
        sys.exit(0)
    for f in files:
        safe_copy_to_processed(f, f.name)


if __name__ == "__main__":
    main()
