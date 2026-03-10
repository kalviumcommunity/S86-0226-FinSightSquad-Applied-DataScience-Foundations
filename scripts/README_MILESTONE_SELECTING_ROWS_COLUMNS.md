# Selecting Rows and Columns Using Indexing and Slicing Milestone

## Overview

This milestone focuses on selecting rows and columns from Pandas DataFrames using clear, intentional indexing and slicing patterns.

Selection is a core data skill because most downstream issues come from choosing the wrong subset.

## Learning Objectives

By completing this milestone, you will be able to:

- Select a single column and multiple columns by name
- Select rows by position using `iloc`
- Select rows by label using `loc`
- Slice row and column ranges
- Combine row and column selection in one readable expression
- Avoid common indexing mistakes

## File

```text
scripts/selecting_rows_columns_milestone.py
```

## How to Run

From the repository root:

```bash
python scripts/selecting_rows_columns_milestone.py
```

## What the Script Demonstrates

### 0. Load a DataFrame

Creates a small transactions DataFrame with explicit index labels (`TXN100` to `TXN105`) so positional and label-based selection are easy to compare.

### 1. Selecting Columns by Name

- Single column selection:
  ```python
  df_transactions["amount"]
  ```
- Multiple column selection:
  ```python
  df_transactions[["date", "category", "amount"]]
  ```
- Result type behavior:
  - Single column -> `Series`
  - Multiple columns -> `DataFrame`

### 2. Selecting Rows by Position (`iloc`)

- Single row by integer position:
  ```python
  df_transactions.iloc[0]
  ```
- Row slicing by position:
  ```python
  df_transactions.iloc[1:4]
  ```
- Key rule: `iloc` is zero-based and the stop index is excluded.

### 3. Selecting Rows by Label (`loc`)

- Single row by label:
  ```python
  df_transactions.loc["TXN102"]
  ```
- Label slice:
  ```python
  df_transactions.loc["TXN101":"TXN103"]
  ```
- Key rule: label slices with `loc` are inclusive on both ends.

### 4. Selecting Rows and Columns Together

- Combined by position:
  ```python
  df_transactions.iloc[0:3, 1:4]
  ```
- Combined by label:
  ```python
  df_transactions.loc[["TXN100", "TXN103", "TXN105"], ["date", "amount", "payment_method"]]
  ```
- Preferred style: use one `.loc[]` or `.iloc[]` expression instead of chained indexing.

## Common Mistakes to Avoid

- Mixing up `loc` and `iloc`
- Assuming `loc` works with integer position when the index is custom labels
- Forgetting that `iloc` slice stop is excluded
- Forgetting that `loc` label slices are inclusive
- Using chained indexing in unclear ways

## Why This Matters

Precise selection helps you:

- Extract exactly the rows and columns you intend
- Keep data workflows readable and predictable
- Prevent silent selection errors and data leakage
- Build safer cleaning and feature engineering steps

## Completion Checklist

- [ ] Script runs without errors
- [ ] You can explain Series vs DataFrame column selection output
- [ ] You can select rows by position with `iloc`
- [ ] You can select rows by label with `loc`
- [ ] You can combine row and column selection in one expression
- [ ] You can describe the inclusive behavior of `loc` slices
