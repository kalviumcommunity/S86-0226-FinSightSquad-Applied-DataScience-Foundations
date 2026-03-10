"""
Identifying and Removing Duplicate Records Milestone
===================================================

This milestone demonstrates how to detect, inspect, and remove duplicate
records in a Pandas DataFrame.

Run:
    python scripts/duplicate_records_milestone.py
"""

import pandas as pd


print("=" * 72)
print("IDENTIFYING AND REMOVING DUPLICATE RECORDS")
print("=" * 72)


# ============================================================================
# 1. Understanding Duplicate Records
# ============================================================================
print("\n1. UNDERSTANDING DUPLICATE RECORDS")
print("-" * 72)
print("Duplicate records can be:")
print("- Exact duplicates: all columns match another row")
print("- Partial duplicates: only selected key columns match")
print("- Caused by repeated data entry, merges, imports, or system retries")


# ============================================================================
# 2. Load Sample Data With Intentional Duplicates
# ============================================================================
print("\n2. LOAD DATA WITH INTENTIONAL DUPLICATES")
print("-" * 72)

transactions = {
    "transaction_id": [
        "TXN001", "TXN002", "TXN003", "TXN003", "TXN004", "TXN005", "TXN006", "TXN007"
    ],
    "customer_id": [
        "C101", "C102", "C103", "C103", "C104", "C102", "C105", "C102"
    ],
    "date": [
        "2026-03-01", "2026-03-01", "2026-03-02", "2026-03-02", "2026-03-03", "2026-03-01", "2026-03-04", "2026-03-01"
    ],
    "category": [
        "Groceries", "Transport", "Utilities", "Utilities", "Healthcare", "Transport", "Entertainment", "Transport"
    ],
    "amount": [
        54.20, 18.00, 120.00, 120.00, 75.00, 18.00, 40.00, 18.00
    ],
    "payment_method": [
        "Card", "Cash", "Card", "Card", "Card", "Cash", "Card", "Cash"
    ],
}

df = pd.DataFrame(transactions)
print("Original DataFrame:")
print(df)
print(f"\nOriginal shape: {df.shape}")


# ============================================================================
# 3. Detecting Duplicate Rows
# ============================================================================
print("\n3. DETECTING DUPLICATE ROWS")
print("-" * 72)

# Mark duplicates across all columns; keep='first' marks later repeats as True.
exact_duplicate_mask = df.duplicated()
exact_duplicate_count = exact_duplicate_mask.sum()

print("Duplicate indicator for exact row matches (all columns):")
print(exact_duplicate_mask)
print(f"\nExact duplicate row count: {exact_duplicate_count}")

if exact_duplicate_count > 0:
    print("\nExact duplicate rows found:")
    print(df[exact_duplicate_mask])

# Detect duplicates using selected columns to find repeated business events.
subset_cols = ["customer_id", "date", "amount", "category"]
partial_duplicate_mask = df.duplicated(subset=subset_cols, keep=False)
partial_duplicate_count = partial_duplicate_mask.sum()

print("\nDuplicate indicator using selected columns:")
print(f"Subset columns: {subset_cols}")
print(partial_duplicate_mask)
print(f"\nRows involved in partial duplicates: {partial_duplicate_count}")

if partial_duplicate_count > 0:
    print("\nPotential duplicate groups based on subset columns:")
    print(df[partial_duplicate_mask].sort_values(by=subset_cols))


# ============================================================================
# 4. Removing Duplicate Records
# ============================================================================
print("\n4. REMOVING DUPLICATE RECORDS")
print("-" * 72)

# A) Remove only exact duplicate rows (safe first pass).
df_no_exact_dupes = df.drop_duplicates()
print("A) After removing exact duplicates (all columns):")
print(df_no_exact_dupes)
print(f"Shape after exact deduplication: {df_no_exact_dupes.shape}")

# B) Remove duplicates by selected business keys and keep the first record.
df_keep_first = df.drop_duplicates(subset=subset_cols, keep="first")
print("\nB) After deduplication on subset columns (keep='first'):")
print(df_keep_first)
print(f"Shape after subset deduplication (keep='first'): {df_keep_first.shape}")

# C) Alternative: keep the last record.
df_keep_last = df.drop_duplicates(subset=subset_cols, keep="last")
print("\nC) After deduplication on subset columns (keep='last'):")
print(df_keep_last)
print(f"Shape after subset deduplication (keep='last'): {df_keep_last.shape}")


# ============================================================================
# 5. Verifying Deduplication Results
# ============================================================================
print("\n5. VERIFYING DEDUPLICATION RESULTS")
print("-" * 72)

before_rows = len(df)
after_rows = len(df_keep_first)
removed_rows = before_rows - after_rows

print(f"Rows before deduplication: {before_rows}")
print(f"Rows after deduplication (subset keep='first'): {after_rows}")
print(f"Rows removed: {removed_rows}")

remaining_exact_duplicates = df_keep_first.duplicated().sum()
remaining_partial_duplicates = df_keep_first.duplicated(subset=subset_cols).sum()

print(f"\nRemaining exact duplicates: {remaining_exact_duplicates}")
print(f"Remaining subset duplicates: {remaining_partial_duplicates}")

print("\nValidation checks:")
print(f"- Exact duplicate check passed: {remaining_exact_duplicates == 0}")
print(f"- Subset duplicate check passed: {remaining_partial_duplicates == 0}")

print("\nDeduplication note:")
print("Always inspect duplicates before removal to avoid dropping important records.")
print("Choose keep='first' or keep='last' based on business context.")

print("\n" + "=" * 72)
print("MILESTONE COMPLETE")
print("=" * 72)
