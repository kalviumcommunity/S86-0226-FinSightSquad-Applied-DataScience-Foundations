"""
Summary Statistics Milestone
=============================
This script demonstrates computing and interpreting basic summary statistics
for individual columns in a Pandas DataFrame.

Learning Objectives:
- Understand what summary statistics represent
- Compute basic statistics for numeric columns
- Interpret statistical outputs correctly
- Compare statistics across different columns
- Build intuition about data distributions
"""

# Step 1: Import required libraries
import pandas as pd
import os

print("=" * 70)
print("SUMMARY STATISTICS MILESTONE")
print("=" * 70)

# ============================================================================
# SECTION 1: Understanding Common Summary Statistics
# ============================================================================
print("\n1. UNDERSTANDING COMMON SUMMARY STATISTICS")
print("-" * 70)
print("""
Summary statistics provide a quick numerical overview of your data.
They help you understand distributions before diving into analysis.

Common Statistics:
------------------
COUNT     : Number of non-missing values
MEAN      : Average value (sum / count)
MEDIAN    : Middle value when sorted (50th percentile)
MIN       : Smallest value in the data
MAX       : Largest value in the data
STD       : Standard deviation - measures spread/variability
25%/75%   : First and third quartiles (25th and 75th percentiles)

Why They Matter:
- MEAN shows central tendency (affected by outliers)
- MEDIAN shows middle value (resistant to outliers)
- MIN/MAX show data range
- STD shows how spread out values are
- Comparing mean vs median reveals skewness
""")

# ============================================================================
# SECTION 2: Loading Data for Analysis
# ============================================================================
print("\n2. LOADING DATA FOR ANALYSIS")
print("-" * 70)

# Construct proper path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(os.path.dirname(current_dir), 'data', 'raw', 'sample_transactions.csv')

# Load the transactions dataset
df = pd.read_csv(data_path)

print("\nDataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst few rows:")
print(df.head())

print(f"\nData types:")
print(df.dtypes)

# ============================================================================
# SECTION 3: Computing Statistics for a Single Column
# ============================================================================
print("\n\n3. COMPUTING STATISTICS FOR A SINGLE COLUMN")
print("-" * 70)
print("""
Let's analyze the 'Amount' column step by step.
Working column by column helps you understand each variable individually.
""")

# Select the Amount column
amount_column = df['Amount']

print("\nAmount Column (first 10 values):")
print(amount_column.head(10))

# Compute individual statistics
print("\n--- Individual Statistics for Amount ---")
print(f"Count (non-missing values): {amount_column.count()}")
print(f"Mean (average):            ${amount_column.mean():.2f}")
print(f"Median (middle value):     ${amount_column.median():.2f}")
print(f"Minimum:                   ${amount_column.min():.2f}")
print(f"Maximum:                   ${amount_column.max():.2f}")
print(f"Standard Deviation:        ${amount_column.std():.2f}")

print("\nInterpretation:")
print(f"- The average transaction is ${amount_column.mean():.2f}")
print(f"- Half of transactions are below ${amount_column.median():.2f}")
print(f"- Transactions range from ${amount_column.min():.2f} to ${amount_column.max():.2f}")
print(f"- Typical variation from average: ±${amount_column.std():.2f}")

# Use describe() for comprehensive summary
print("\n--- Using describe() Method ---")
print("The describe() method gives you all statistics at once:")
print(amount_column.describe())

# ============================================================================
# SECTION 4: Interpreting Results Correctly
# ============================================================================
print("\n\n4. INTERPRETING RESULTS CORRECTLY")
print("-" * 70)
print("""
Understanding what the numbers really mean is crucial.
Let's compare mean vs median to understand data distribution.
""")

mean_val = amount_column.mean()
median_val = amount_column.median()

print(f"\nAmount Statistics:")
print(f"Mean:   ${mean_val:.2f}")
print(f"Median: ${median_val:.2f}")
print(f"Difference: ${abs(mean_val - median_val):.2f}")

if mean_val > median_val:
    print("\n✓ Mean > Median suggests:")
    print("  - Data may be right-skewed")
    print("  - A few high values are pulling the average up")
    print("  - Median is more representative of 'typical' value")
elif mean_val < median_val:
    print("\n✓ Mean < Median suggests:")
    print("  - Data may be left-skewed")
    print("  - A few low values are pulling the average down")
    print("  - Median is more representative of 'typical' value")
else:
    print("\n✓ Mean ≈ Median suggests:")
    print("  - Data is roughly symmetric")
    print("  - Both represent 'typical' value well")

# Understanding spread
std_val = amount_column.std()
print(f"\nUnderstanding Spread (Standard Deviation: ${std_val:.2f}):")
print(f"- About 68% of values fall within ${mean_val:.2f} ± ${std_val:.2f}")
print(f"  That's between ${mean_val - std_val:.2f} and ${mean_val + std_val:.2f}")
print(f"- Higher std means more variability in transaction amounts")

# Identifying potential outliers using statistics
print("\n--- Identifying Unusual Values ---")
q1 = amount_column.quantile(0.25)
q3 = amount_column.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"25th percentile (Q1): ${q1:.2f}")
print(f"75th percentile (Q3): ${q3:.2f}")
print(f"Interquartile Range (IQR): ${iqr:.2f}")
print(f"\nPotential outliers: values < ${lower_bound:.2f} or > ${upper_bound:.2f}")

outliers = df[(amount_column < lower_bound) | (amount_column > upper_bound)]
if len(outliers) > 0:
    print(f"Found {len(outliers)} potential outlier(s):")
    print(outliers[['Date', 'Category', 'Amount']])
else:
    print("No statistical outliers detected in this dataset.")

# ============================================================================
# SECTION 5: Comparing Columns Using Statistics
# ============================================================================
print("\n\n5. COMPARING COLUMNS USING STATISTICS")
print("-" * 70)
print("""
Comparing statistics across columns reveals relative patterns.
This helps identify which variables have more variability or different scales.
""")

# For demonstration, let's create a comparison if we add more numeric columns
print("\n--- Statistics for Amount Column ---")
print(df['Amount'].describe())

# Let's group by Category and compare statistics
print("\n--- Comparing Amount Statistics by Category ---")
category_stats = df.groupby('Category')['Amount'].describe()
print(category_stats)

print("\nKey Insights from Comparison:")
print("- Which category has the highest average amount?")
max_mean_category = df.groupby('Category')['Amount'].mean().idxmax()
max_mean_value = df.groupby('Category')['Amount'].mean().max()
print(f"  → {max_mean_category}: ${max_mean_value:.2f}")

print("\n- Which category has the most variability?")
max_std_category = df.groupby('Category')['Amount'].std().idxmax()
max_std_value = df.groupby('Category')['Amount'].std().max()
print(f"  → {max_std_category}: STD = ${max_std_value:.2f}")

print("\n- Which category has the lowest minimum transaction?")
min_category = df.groupby('Category')['Amount'].min().idxmin()
min_value = df.groupby('Category')['Amount'].min().min()
print(f"  → {min_category}: ${min_value:.2f}")

# ============================================================================
# SECTION 6: Using Statistics to Guide Further Analysis
# ============================================================================
print("\n\n6. USING STATISTICS TO GUIDE FURTHER ANALYSIS")
print("-" * 70)
print("""
Summary statistics help you ask better questions about your data.
""")

print("\nQuestions statistics can help answer:")
print("1. Are there unusual patterns in spending?")
print("2. Which categories need budget adjustments?")
print("3. Is there high variability that needs investigation?")
print("4. Are there data quality issues (outliers, missing values)?")

print("\n--- Key Statistics Summary ---")
print(f"Total Transactions: {df.shape[0]}")
print(f"Total Amount:       ${df['Amount'].sum():.2f}")
print(f"Average Amount:     ${df['Amount'].mean():.2f}")
print(f"Median Amount:      ${df['Amount'].median():.2f}")
print(f"Amount Range:       ${df['Amount'].min():.2f} - ${df['Amount'].max():.2f}")
print(f"Categories:         {df['Category'].nunique()}")
print(f"Payment Methods:    {df['Payment_Method'].nunique()}")

# ============================================================================
# SECTION 7: Common Mistakes to Avoid
# ============================================================================
print("\n\n7. COMMON MISTAKES TO AVOID")
print("-" * 70)
print("""
❌ Mistake 1: Relying only on mean without checking median
   → Solution: Always compare mean vs median

❌ Mistake 2: Ignoring standard deviation
   → Solution: Check spread alongside central tendency

❌ Mistake 3: Not verifying counts for missing data
   → Solution: Check count vs total rows

❌ Mistake 4: Interpreting statistics without context
   → Solution: Understand what the data represents

❌ Mistake 5: Computing statistics on non-numeric columns
   → Solution: Verify data types first
""")

# Verify column types before computing statistics
print("\nColumn Data Types:")
print(df.dtypes)
print("\nNumeric Columns:")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print(numeric_cols)

# ============================================================================
# MILESTONE COMPLETE
# ============================================================================
print("\n" + "=" * 70)
print("MILESTONE COMPLETE!")
print("=" * 70)
print("""
You've learned to:
✓ Understand what summary statistics represent
✓ Compute statistics for individual columns
✓ Interpret mean, median, min, max correctly
✓ Understand spread using standard deviation
✓ Compare statistics across groups
✓ Use statistics to guide analysis decisions

Next Steps:
- Practice with different datasets
- Combine with visualization
- Use statistics to identify data quality issues
- Apply to real-world financial analysis
""")
