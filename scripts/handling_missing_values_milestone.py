"""
Handling Missing Values Using Drop and Fill Strategies
=======================================================
This script demonstrates handling missing values in Pandas DataFrames using
drop and fill strategies.

Learning Objectives:
- Identify missing values in DataFrames
- Drop missing values strategically
- Fill missing values using appropriate methods
- Compare drop vs fill strategies
- Make informed decisions about data cleaning
"""

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("HANDLING MISSING VALUES: DROP AND FILL STRATEGIES")
print("=" * 70)

# ============================================================================
# SECTION 1: Creating Sample Data with Missing Values
# ============================================================================
print("\n1. CREATING SAMPLE DATA WITH MISSING VALUES")
print("-" * 70)

# Create a realistic financial dataset with missing values
financial_data = {
    'Date': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15', 
             '2024-01-20', '2024-01-25', '2024-01-30', '2024-02-01',
             '2024-02-05', '2024-02-10'],
    'Category': ['Groceries', 'Transport', np.nan, 'Utilities', 
                 'Groceries', 'Healthcare', 'Entertainment', 'Groceries',
                 np.nan, 'Transport'],
    'Amount': [125.50, 45.00, 80.00, np.nan, 98.75, 
               200.00, np.nan, 150.00, 75.00, np.nan],
    'Payment_Method': ['Credit Card', 'Cash', 'Debit Card', 'Bank Transfer',
                       np.nan, 'Insurance', 'Cash', 'Credit Card',
                       'Cash', 'Cash'],
    'Store': ['Walmart', np.nan, 'Mall', 'Online', 
              'Target', 'Hospital', np.nan, 'Walmart',
              'Mall', np.nan]
}

df_original = pd.DataFrame(financial_data)

print("\nOriginal DataFrame with Missing Values:")
print(df_original)
print(f"\nOriginal Shape: {df_original.shape}")
print(f"(Rows: {df_original.shape[0]}, Columns: {df_original.shape[1]})")

# ============================================================================
# SECTION 2: Identifying Missing Values
# ============================================================================
print("\n\n2. IDENTIFYING MISSING VALUES")
print("-" * 70)

print("\nMissing values per column:")
missing_count = df_original.isnull().sum()
print(missing_count)

print("\nPercentage of missing values per column:")
missing_percentage = (df_original.isnull().sum() / len(df_original)) * 100
for col, pct in missing_percentage.items():
    print(f"{col}: {pct:.1f}%")

print("\nTotal missing values in DataFrame:", df_original.isnull().sum().sum())

# ============================================================================
# SECTION 3: STRATEGY 1 - Dropping Missing Values
# ============================================================================
print("\n\n3. STRATEGY 1: DROPPING MISSING VALUES")
print("=" * 70)

# 3.1: Drop rows with ANY missing values
print("\n3.1 DROP ROWS WITH ANY MISSING VALUES (dropna())")
print("-" * 70)
df_drop_any = df_original.dropna()

print(f"\nOriginal Shape: {df_original.shape}")
print(f"After dropping rows with ANY missing: {df_drop_any.shape}")
print(f"Rows removed: {df_original.shape[0] - df_drop_any.shape[0]}")

print("\nResult:")
print(df_drop_any)

print("\n⚠️  WARNING: This removes too much data!")
print("   Only 4 out of 10 rows remain (60% data loss)")

# 3.2: Drop rows with ALL values missing
print("\n\n3.2 DROP ROWS WHERE ALL VALUES ARE MISSING")
print("-" * 70)

# Add a row with all missing values for demonstration
df_with_empty_row = df_original.copy()
df_with_empty_row.loc[10] = [np.nan, np.nan, np.nan, np.nan, np.nan]

df_drop_all = df_with_empty_row.dropna(how='all')

print(f"Original with empty row: {df_with_empty_row.shape}")
print(f"After dropping rows where ALL are missing: {df_drop_all.shape}")
print("✅ This is a safer strategy - only removes completely empty rows")

# 3.3: Drop rows with missing values in specific columns
print("\n\n3.3 DROP ROWS WITH MISSING VALUES IN CRITICAL COLUMNS")
print("-" * 70)

df_drop_subset = df_original.dropna(subset=['Amount'])

print(f"\nOriginal Shape: {df_original.shape}")
print(f"After dropping rows with missing Amount: {df_drop_subset.shape}")
print(f"Rows removed: {df_original.shape[0] - df_drop_subset.shape[0]}")

print("\nResult:")
print(df_drop_subset)

print("\n✅ GOOD STRATEGY: Amount is critical for financial analysis")
print("   Rows without amounts cannot be used in calculations")

# 3.4: Drop columns with too many missing values
print("\n\n3.4 DROP COLUMNS WITH EXCESSIVE MISSING VALUES")
print("-" * 70)

threshold = 0.30  # Drop if more than 30% missing
df_drop_columns = df_original.copy()

print(f"\nThreshold: {threshold * 100}% missing")
print("\nMissing value analysis:")

for col in df_original.columns:
    missing_pct = (df_original[col].isnull().sum() / len(df_original))
    print(f"{col}: {missing_pct * 100:.1f}% missing", end="")
    
    if missing_pct > threshold:
        print(" ➜ DROP")
        df_drop_columns = df_drop_columns.drop(columns=[col])
    else:
        print(" ➜ KEEP")

print(f"\nOriginal Columns: {df_original.shape[1]}")
print(f"After dropping high-missing columns: {df_drop_columns.shape[1]}")

# ============================================================================
# SECTION 4: STRATEGY 2 - Filling Missing Values
# ============================================================================
print("\n\n4. STRATEGY 2: FILLING MISSING VALUES")
print("=" * 70)

# 4.1: Fill with a constant value
print("\n4.1 FILL WITH CONSTANT VALUES")
print("-" * 70)

df_fill_constant = df_original.copy()
df_fill_constant['Category'] = df_fill_constant['Category'].fillna('Unknown')
df_fill_constant['Store'] = df_fill_constant['Store'].fillna('Not Specified')

print("\nFilled categorical columns with descriptive constants:")
print(df_fill_constant[['Category', 'Store']])

print("\n✅ GOOD PRACTICE: Use meaningful constants for categorical data")

# 4.2: Fill numeric values with mean
print("\n\n4.2 FILL NUMERIC VALUES WITH MEAN")
print("-" * 70)

df_fill_mean = df_original.copy()
amount_mean = df_original['Amount'].mean()

print(f"Mean of Amount column: ${amount_mean:.2f}")

df_fill_mean['Amount'] = df_fill_mean['Amount'].fillna(amount_mean)

print("\nAmount column after filling with mean:")
print(df_fill_mean['Amount'])

print("\n⚠️  CONSIDERATION: Mean is sensitive to outliers")
print("   Use when data is normally distributed")

# 4.3: Fill numeric values with median
print("\n\n4.3 FILL NUMERIC VALUES WITH MEDIAN")
print("-" * 70)

df_fill_median = df_original.copy()
amount_median = df_original['Amount'].median()

print(f"Median of Amount column: ${amount_median:.2f}")

df_fill_median['Amount'] = df_fill_median['Amount'].fillna(amount_median)

print("\nAmount column after filling with median:")
print(df_fill_median['Amount'])

print("\n✅ BETTER FOR SKEWED DATA: Median is resistant to outliers")

# 4.4: Fill categorical values with mode
print("\n\n4.4 FILL CATEGORICAL VALUES WITH MODE (Most Frequent)")
print("-" * 70)

df_fill_mode = df_original.copy()

# Get mode for Payment_Method
payment_mode = df_original['Payment_Method'].mode()[0]
print(f"Most frequent Payment Method: {payment_mode}")

df_fill_mode['Payment_Method'] = df_fill_mode['Payment_Method'].fillna(payment_mode)

print("\nPayment_Method after filling with mode:")
print(df_fill_mode['Payment_Method'])

print("\n✅ GOOD FOR CATEGORICAL DATA: Uses the most common category")

# 4.5: Forward Fill (use previous value)
print("\n\n4.5 FORWARD FILL (Use Previous Value)")
print("-" * 70)

df_ffill = df_original.copy()
df_ffill['Store'] = df_ffill['Store'].fillna(method='ffill')

print("\nStore column after forward fill:")
print(df_ffill[['Date', 'Store']])

print("\n⚠️  USE CAREFULLY: Assumes values persist over time")
print("   Works well for time-series data")

# ============================================================================
# SECTION 5: Comparing Strategies
# ============================================================================
print("\n\n5. COMPARING DROP VS FILL STRATEGIES")
print("=" * 70)

print("\nDataset Size Comparison:")
print(f"Original:                    {df_original.shape[0]} rows, {df_original.shape[1]} columns")
print(f"After dropna():              {df_drop_any.shape[0]} rows, {df_drop_any.shape[1]} columns (❌ 60% data loss)")
print(f"After drop Amount nulls:     {df_drop_subset.shape[0]} rows, {df_drop_subset.shape[1]} columns (✅ 30% loss)")
print(f"After fill strategies:       {df_original.shape[0]} rows, {df_original.shape[1]} columns (✅ No data loss)")

# Create a comprehensive clean dataset
print("\n\nCREATING A COMPREHENSIVE CLEAN DATASET:")
print("-" * 70)

df_clean = df_original.copy()

# Step 1: Drop rows where Amount is missing (critical column)
print("Step 1: Drop rows with missing Amount (critical for analysis)")
df_clean = df_clean.dropna(subset=['Amount'])
print(f"  Shape: {df_clean.shape}")

# Step 2: Fill categorical columns with appropriate values
print("Step 2: Fill categorical columns with meaningful constants")
df_clean['Category'] = df_clean['Category'].fillna('Unknown')
df_clean['Payment_Method'] = df_clean['Payment_Method'].fillna(
    df_clean['Payment_Method'].mode()[0]
)
df_clean['Store'] = df_clean['Store'].fillna('Not Specified')
print(f"  Shape: {df_clean.shape}")

print("\nFinal Clean Dataset:")
print(df_clean)

print("\nMissing values remaining:")
print(df_clean.isnull().sum())

# ============================================================================
# SECTION 6: Decision-Making Guidelines
# ============================================================================
print("\n\n6. DECISION-MAKING GUIDELINES")
print("=" * 70)

print("""
WHEN TO DROP:
✅ Drop rows when:
   - Critical columns have missing values (e.g., Amount in financial data)
   - Very few rows have missing data (<5%)
   - Missing data represents invalid records
   
✅ Drop columns when:
   - More than 50-70% values are missing
   - Column is not important for analysis
   - Cannot reasonably fill the values

WHEN TO FILL:
✅ Fill with constant when:
   - Missing means "None" or "Unknown" (categorical)
   - Default value makes sense (like 0 for optional features)
   
✅ Fill with mean when:
   - Data is normally distributed
   - Maintaining average is important
   
✅ Fill with median when:
   - Data has outliers
   - Distribution is skewed
   
✅ Fill with mode when:
   - Data is categorical
   - Using most common value makes sense

AVOID:
❌ Never drop all missing data without checking impact
❌ Never fill categorical data with numeric values
❌ Never fill without understanding the data context
❌ Never hide missing data issues from stakeholders

KEY PRINCIPLE:
Always choose the strategy that:
1. Preserves data integrity
2. Minimizes bias
3. Is explainable and justified
4. Considers downstream analysis needs
""")

# ============================================================================
# SECTION 7: Common Mistakes to Avoid
# ============================================================================
print("\n\n7. COMMON MISTAKES TO AVOID")
print("=" * 70)

print("\n❌ MISTAKE 1: Filling categorical data with numeric values")
print("-" * 70)
bad_example = df_original.copy()
bad_example['Category'] = bad_example['Category'].fillna(0)  # WRONG!
print("Don't do: df['Category'].fillna(0)")
print("Why: 'Category' is text, not a number. Use 'Unknown' instead.")

print("\n❌ MISTAKE 2: Dropping data without checking impact")
print("-" * 70)
print(f"dropna() removed {df_original.shape[0] - df_drop_any.shape[0]} rows ({(1 - df_drop_any.shape[0]/df_original.shape[0])*100:.1f}% loss)")
print("Always check: shape before and after")

print("\n❌ MISTAKE 3: Using mean for skewed distributions")
print("-" * 70)
print("Mean is affected by extreme values. Use median for skewed data.")

print("\n✅ CORRECT APPROACH: Always inspect, decide, then apply")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n\n" + "=" * 70)
print("SUMMARY: KEY TAKEAWAYS")
print("=" * 70)

print("""
1. ALWAYS identify missing values first (isnull(), info())
2. UNDERSTAND the pattern and amount of missing data
3. DECIDE based on:
   - Importance of the column
   - Percentage of missing values
   - Nature of the data (numeric vs categorical)
   - Analysis requirements
4. DROP when data is critical and cannot be reasonably filled
5. FILL when you can make reasonable assumptions
6. DOCUMENT your decisions for reproducibility
7. VERIFY results after cleaning

Missing data handling is NOT about removing the problem.
It's about making informed, justifiable decisions that preserve data quality.
""")

print("\n" + "=" * 70)
print("MILESTONE COMPLETE!")
print("=" * 70)
print("\nYou now understand:")
print("✅ How to drop missing values strategically")
print("✅ How to fill missing values appropriately")
print("✅ How to compare different strategies")
print("✅ How to make informed cleaning decisions")
print("✅ How to avoid common pitfalls")

print("\nNext Steps:")
print("→ Practice with real datasets")
print("→ Always document your cleaning decisions")
print("→ Consider the impact on downstream analysis")
print("=" * 70)
