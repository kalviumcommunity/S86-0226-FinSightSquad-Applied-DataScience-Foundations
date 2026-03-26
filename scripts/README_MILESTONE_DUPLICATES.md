# Identifying and Removing Duplicate Records Milestone

## Overview

This milestone focuses on detecting, inspecting, and removing duplicate records in Pandas DataFrames.

Duplicate data is a common data quality issue that can skew analysis, inflate counts, and produce incorrect conclusions if not handled intentionally.

## Learning Objectives

By completing this milestone, you will be able to:

- Understand what duplicate records are
- Detect duplicate rows in a DataFrame
- Identify duplicates across all columns or selected columns
- Remove duplicates safely and intentionally
- Verify that deduplication worked correctly

## Why This Matters

Common beginner issues include:

- Counting duplicate records as unique observations
- Inflated metrics and misleading summaries
- Removing duplicates without inspecting them first
- Losing important information during cleanup

This milestone helps ensure:

- Each row represents a meaningful observation
- Aggregations and summary statistics are more accurate
- Data integrity is preserved
- Downstream analysis is more trustworthy

## File

```text
scripts/duplicate_records_milestone.py
```

## How to Run

From the repository root:

```bash
python scripts/duplicate_records_milestone.py
```

## What the Script Demonstrates

### 1. Understanding Duplicate Records

- Exact duplicates (all columns match)
- Partial duplicates (selected key columns match)
- Common reasons duplicates happen in real workflows

### 2. Detecting Duplicate Rows

- `df.duplicated()` for full-row duplicate detection
- Counting duplicates with boolean masks
- Inspecting duplicate entries before removal
- Detecting partial duplicates using a `subset` of columns

### 3. Removing Duplicate Records

- `df.drop_duplicates()` for exact row deduplication
- `df.drop_duplicates(subset=..., keep="first")`
- `df.drop_duplicates(subset=..., keep="last")`
- Understanding how deduplication changes dataset size

### 4. Verifying Results

- Comparing row counts before and after cleanup
- Re-checking duplicate counts after removal
- Confirming that selected deduplication rules worked
- Printing clear validation checks

## Key Pandas Methods Used

- `duplicated()`
- `drop_duplicates()`
- `sum()` on boolean masks
- `sort_values()` to inspect duplicate groups
- `shape` and `len()` for size comparison

## Video Walkthrough (~2 Minutes)

Your video should include:

1. Detecting duplicate records
2. Inspecting duplicate rows and duplicate groups
3. Removing duplicates (exact and subset-based)
4. Comparing shape before and after deduplication
5. Explaining why deduplication matters for data quality

## Submission Checklist

- [ ] Script runs without errors
- [ ] Duplicate rows are detected clearly
- [ ] Duplicate inspection is shown before removal
- [ ] Deduplication is applied intentionally
- [ ] Before/after row counts are shown
- [ ] Remaining duplicates are rechecked
- [ ] Video recorded (~2 minutes)
- [ ] Video link submitted as instructed

## Important Notes

- Always inspect duplicates before dropping rows
- For partial duplicates, choose `subset` columns based on business logic
- `keep` strategy (`first` or `last`) should be explainable
- Data cleaning decisions should be documented and reproducible

Clean, deduplicated data is a foundation for trustworthy analysis.
