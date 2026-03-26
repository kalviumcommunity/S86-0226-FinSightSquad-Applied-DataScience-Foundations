"""
Selecting Rows and Columns Using Indexing and Slicing
=====================================================

This milestone demonstrates precise DataFrame selection using:
- Column selection by name
- Row selection by position with iloc
- Row selection by label with loc
- Row and column selection together
- Safe, readable selection patterns

Run:
    python scripts/selecting_rows_columns_milestone.py
"""

import pandas as pd


print("=" * 70)
print("SELECTING ROWS AND COLUMNS USING INDEXING AND SLICING")
print("=" * 70)


# ============================================================================
# SECTION 0: Load a DataFrame for Selection Practice
# ============================================================================
print("\n0. LOAD A DATAFRAME")
print("-" * 70)

transactions_data = {
    "date": [
        "2026-03-01",
        "2026-03-02",
        "2026-03-03",
        "2026-03-04",
        "2026-03-05",
        "2026-03-06",
    ],
    "category": [
        "Groceries",
        "Transport",
        "Entertainment",
        "Utilities",
        "Groceries",
        "Healthcare",
    ],
    "amount": [85.50, 22.00, 40.00, 120.00, 63.25, 95.00],
    "payment_method": [
        "Card",
        "Cash",
        "Card",
        "Transfer",
        "Card",
        "Card",
    ],
    "city": ["Seattle", "Seattle", "Seattle", "Seattle", "Seattle", "Seattle"],
}

transaction_index = ["TXN100", "TXN101", "TXN102", "TXN103", "TXN104", "TXN105"]

# Use explicit labels so label-based selection is clear and intentional.
df_transactions = pd.DataFrame(transactions_data, index=transaction_index)

print("DataFrame loaded:")
print(df_transactions)
print(f"\nShape: {df_transactions.shape}")


# ============================================================================
# SECTION 1: Selecting Columns by Name
# ============================================================================
print("\n1. SELECTING COLUMNS BY NAME")
print("-" * 70)

single_column = df_transactions["amount"]
print("\na) Single column selection: df_transactions['amount']")
print(single_column)
print(f"Type returned: {type(single_column)}")

multiple_columns = df_transactions[["date", "category", "amount"]]
print("\nb) Multiple column selection: df_transactions[['date', 'category', 'amount']]")
print(multiple_columns)
print(f"Type returned: {type(multiple_columns)}")

print("\nObservation:")
print("- Single column returns a Series")
print("- Multiple columns return a DataFrame")


# ============================================================================
# SECTION 2: Selecting Rows by Position (iloc)
# ============================================================================
print("\n2. SELECTING ROWS BY POSITION (iloc)")
print("-" * 70)

first_row_by_position = df_transactions.iloc[0]
print("\na) First row by position: df_transactions.iloc[0]")
print(first_row_by_position)

rows_2_to_4_by_position = df_transactions.iloc[1:4]
print("\nb) Row slice by position: df_transactions.iloc[1:4]")
print(rows_2_to_4_by_position)

print("\nPosition notes:")
print("- iloc uses zero-based positions")
print("- The stop index in iloc slices is excluded")

safe_position = 10
print("\nc) Safe positional selection check")
if safe_position < len(df_transactions):
    print(df_transactions.iloc[safe_position])
else:
    print(
        f"Position {safe_position} is out of range for DataFrame length {len(df_transactions)}"
    )


# ============================================================================
# SECTION 3: Selecting Rows by Label (loc)
# ============================================================================
print("\n3. SELECTING ROWS BY LABEL (loc)")
print("-" * 70)

one_row_by_label = df_transactions.loc["TXN102"]
print("\na) Single row by label: df_transactions.loc['TXN102']")
print(one_row_by_label)

label_slice = df_transactions.loc["TXN101":"TXN103"]
print("\nb) Label slice: df_transactions.loc['TXN101':'TXN103']")
print(label_slice)

print("\nLabel notes:")
print("- loc uses index labels, not integer positions")
print("- Label slicing with loc is inclusive on both ends")

label_to_check = "TXN999"
print("\nc) Safe label selection check")
if label_to_check in df_transactions.index:
    print(df_transactions.loc[label_to_check])
else:
    print(f"Label '{label_to_check}' is not present in the DataFrame index")


# ============================================================================
# SECTION 4: Selecting Rows and Columns Together
# ============================================================================
print("\n4. SELECTING ROWS AND COLUMNS TOGETHER")
print("-" * 70)

subset_by_position = df_transactions.iloc[0:3, 1:4]
print("\na) Combined selection by position: df_transactions.iloc[0:3, 1:4]")
print(subset_by_position)

subset_by_label = df_transactions.loc[
    ["TXN100", "TXN103", "TXN105"], ["date", "amount", "payment_method"]
]
print(
    "\nb) Combined selection by label: df_transactions.loc[['TXN100', 'TXN103', 'TXN105'], ['date', 'amount', 'payment_method']]"
)
print(subset_by_label)

print("\nc) Avoid chained indexing (concept)")
print("Preferred: df_transactions.loc[['TXN100', 'TXN101'], ['amount']]")
preferred_selection = df_transactions.loc[["TXN100", "TXN101"], ["amount"]]
print(preferred_selection)


# ============================================================================
# SECTION 5: Summary
# ============================================================================
print("\n5. SUMMARY")
print("=" * 70)
print("What this milestone practiced:")
print("1. Selecting specific columns by name")
print("2. Selecting rows by position with iloc")
print("3. Selecting rows by label with loc")
print("4. Slicing row and column ranges")
print("5. Combining row and column selection clearly")
print("6. Checking labels and positions before selecting")
print("=" * 70)
print("MILESTONE COMPLETE")
print("=" * 70)
