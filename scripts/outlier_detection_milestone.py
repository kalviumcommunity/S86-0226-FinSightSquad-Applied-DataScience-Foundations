"""
Outlier Detection Milestone
============================
This script demonstrates detecting outliers using visual inspection and 
simple statistical rules. Outliers are data points that differ significantly 
from the majority of the data and can strongly influence analysis, 
statistics, and models if not identified early.

Learning Objectives:
- Understand what outliers are and why they matter
- Detect outliers using visual inspection (boxplots and scatter plots)
- Apply simple statistical rules to flag outliers (IQR method, threshold checks)
- Distinguish between valid outliers and data errors
- Build judgment around outlier handling
"""

# Step 1: Import required libraries
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import os

print("=" * 70)
print("OUTLIER DETECTION MILESTONE")
print("=" * 70)

# ============================================================================
# SECTION 1: Understanding Outliers
# ============================================================================
print("\n1. UNDERSTANDING OUTLIERS")
print("-" * 70)
print("""
An outlier is a data point that differs significantly from other observations.

Types of Outliers:
------------------
GLOBAL OUTLIER   : A point far from the rest of the entire dataset
CONTEXTUAL       : A point unusual in a specific context (e.g., $5000 grocery)
COLLECTIVE       : A group of points unusual together

Why Outliers Matter:
--------------------
They can:
  - Distort the mean (average) significantly
  - Inflate standard deviation
  - Skew regression lines
  - Mislead clustering algorithms
  - Indicate data entry errors OR genuinely rare events

Common Examples in Finance:
  - A $10,000 transaction among mostly $50-$200 ones
  - A negative transaction amount (refund or error?)
  - A transaction on a date far outside normal range

Outliers Are Context-Dependent:
  - A $2,000 healthcare bill is unusual but possibly valid
  - A $2,000 grocery bill may be a data entry error
  - Always investigate before deciding what to do

RULE: Detect first. Investigate second. Act third.
""")

# ============================================================================
# SECTION 2: Load and Prepare Data
# ============================================================================
print("\n2. LOADING TRANSACTION DATA")
print("-" * 70)

# Get the path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'data', 'raw', 'sample_transactions.csv')

# Load the data
df = pd.read_csv(csv_path)

print(f"Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows Ã— {df.shape[1]} columns")
print(f"\nColumns: {df.columns.tolist()}")
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Identify numeric columns for outlier analysis
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
print(f"\nNumeric columns available for outlier detection: {numeric_cols}")

# For demonstration, inject a few artificial outliers into a working copy
import numpy as np
df_demo = df.copy()
np.random.seed(42)

# Add artificial extreme values to simulate outliers for demonstration
extra_rows = pd.DataFrame({
    'Date': ['2024-02-01', '2024-02-05', '2024-02-10'],
    'Category': ['Groceries', 'Entertainment', 'Transport'],
    'Amount': [1850.00, 0.50, 950.00],    # extreme high, extreme low, high
    'Type': ['Expense', 'Expense', 'Expense'],
    'Payment_Method': ['Credit Card', 'Cash', 'Debit Card']
})
df_demo = pd.concat([df_demo, extra_rows], ignore_index=True)

print(f"\nWorking dataset for demonstration: {df_demo.shape[0]} rows")
print("\nAmount column summary:")
print(df_demo['Amount'].describe())

# ============================================================================
# SECTION 3: Visual Inspection â€” Boxplot
# ============================================================================
print("\n" + "=" * 70)
print("3. VISUAL OUTLIER DETECTION â€” BOXPLOT")
print("=" * 70)

print("""
Boxplots are the go-to visual tool for spotting outliers.

How to read for outliers:
  - Points plotted BEYOND the whiskers are potential outliers
  - Whiskers extend to: Q1 - 1.5*IQR (lower) and Q3 + 1.5*IQR (upper)
  - Any dot/circle outside these bounds is flagged visually
""")

output_dir = os.path.join(parent_dir, 'outputs', 'figures')
os.makedirs(output_dir, exist_ok=True)

# --- Plot 1: Single column boxplot ---
fig, ax = plt.subplots(figsize=(8, 6))
bp = ax.boxplot(df_demo['Amount'],
                vert=True,
                patch_artist=True,
                boxprops=dict(facecolor='#AED6F1', color='#1A5276'),
                whiskerprops=dict(color='#1A5276', linewidth=1.5),
                capprops=dict(color='#1A5276', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2.5),
                flierprops=dict(marker='o', markerfacecolor='red',
                                markeredgecolor='darkred', markersize=9,
                                linestyle='none', label='Outlier'))

ax.set_title('Outlier Detection: Transaction Amounts\n(Red dots = potential outliers beyond whiskers)',
             fontsize=13, fontweight='bold', pad=12)
ax.set_ylabel('Amount ($)', fontsize=12)
ax.set_xticks([1])
ax.set_xticklabels(['Amount'])
ax.grid(axis='y', alpha=0.35, linestyle='--')

# Annotate the outlier points
q1 = df_demo['Amount'].quantile(0.25)
q3 = df_demo['Amount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers_visual = df_demo[(df_demo['Amount'] < lower_bound) | (df_demo['Amount'] > upper_bound)]['Amount']

for val in outliers_visual:
    ax.annotate(f'  ${val:.2f}', xy=(1, val), fontsize=9,
                color='darkred', va='center')

plt.tight_layout()
boxplot_path = os.path.join(output_dir, 'outlier_boxplot_amount.png')
plt.savefig(boxplot_path, dpi=150)
print(f"âœ“ Boxplot saved: {boxplot_path}")
plt.close()

print(f"""
Boxplot Interpretation â€” Amount Column:
-----------------------------------------
Q1 (25th percentile)  : ${q1:.2f}
Median                : ${df_demo['Amount'].median():.2f}
Q3 (75th percentile)  : ${q3:.2f}
IQR (Q3 - Q1)         : ${iqr:.2f}
Lower Whisker Bound   : ${lower_bound:.2f}  (Q1 - 1.5 Ã— IQR)
Upper Whisker Bound   : ${upper_bound:.2f}  (Q3 + 1.5 Ã— IQR)

Points BEYOND whiskers are plotted as dots â€” these are potential outliers.
""")

# ============================================================================
# SECTION 4: Visual Inspection â€” Scatter Plot
# ============================================================================
print("\n" + "=" * 70)
print("4. VISUAL OUTLIER DETECTION â€” SCATTER PLOT")
print("=" * 70)

print("""
Scatter plots are useful for spotting isolated or unusual clusters.
Plotting values by index (row number) reveals unexplained spikes.
""")

# Create color mask: red for outliers, blue for normal
colors = ['red' if (v < lower_bound or v > upper_bound) else '#2980B9'
          for v in df_demo['Amount']]

fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(range(len(df_demo)), df_demo['Amount'],
           c=colors, s=70, edgecolors='white', linewidths=0.5, zorder=3)

# Draw reference lines for bounds
ax.axhline(y=upper_bound, color='red', linestyle='--', linewidth=1.2,
           label=f'Upper bound (${upper_bound:.2f})')
ax.axhline(y=lower_bound, color='orange', linestyle='--', linewidth=1.2,
           label=f'Lower bound (${lower_bound:.2f})')
ax.axhline(y=df_demo['Amount'].median(), color='green', linestyle='-',
           linewidth=1.2, alpha=0.7, label=f'Median (${df_demo["Amount"].median():.2f})')

ax.set_title('Scatter Plot: Transaction Amounts by Index\n(Red dots = potential outliers)',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Transaction Index', fontsize=11)
ax.set_ylabel('Amount ($)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(alpha=0.3, linestyle='--')
plt.tight_layout()

scatter_path = os.path.join(output_dir, 'outlier_scatter_amount.png')
plt.savefig(scatter_path, dpi=150)
print(f"âœ“ Scatter plot saved: {scatter_path}")
plt.close()

print("""
How to read the scatter plot:
  - Most points cluster in a band around the median
  - Red dots far above or below the reference lines stand out
  - Unexplained spikes signal candidates for investigation
""")

# ============================================================================
# SECTION 5: Detecting Outliers Using Simple Rules â€” IQR Method
# ============================================================================
print("\n" + "=" * 70)
print("5. OUTLIER DETECTION USING THE IQR RULE")
print("=" * 70)

print("""
The IQR (Interquartile Range) Rule:
-------------------------------------
Step 1: Compute Q1 (25th percentile) and Q3 (75th percentile)
Step 2: IQR = Q3 - Q1
Step 3: Lower Bound = Q1 - 1.5 Ã— IQR
Step 4: Upper Bound = Q3 + 1.5 Ã— IQR
Step 5: Flag values outside [Lower Bound, Upper Bound]

This rule is robust: it uses the middle 50% of the data, so extreme 
values do not influence the boundaries themselves.
""")

# Apply IQR rule
q1 = df_demo['Amount'].quantile(0.25)
q3 = df_demo['Amount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outlier_mask = (df_demo['Amount'] < lower_bound) | (df_demo['Amount'] > upper_bound)
outlier_rows = df_demo[outlier_mask].copy()
normal_rows  = df_demo[~outlier_mask].copy()

print(f"IQR Rule Results â€” Amount Column:")
print(f"{'':>2}Q1                 : ${q1:.2f}")
print(f"{'':>2}Q3                 : ${q3:.2f}")
print(f"{'':>2}IQR                : ${iqr:.2f}")
print(f"{'':>2}Lower Bound        : ${lower_bound:.2f}")
print(f"{'':>2}Upper Bound        : ${upper_bound:.2f}")
print(f"\n{'':>2}Total rows         : {len(df_demo)}")
print(f"{'':>2}Normal rows        : {len(normal_rows)}")
print(f"{'':>2}Flagged as outlier : {len(outlier_rows)}")

if len(outlier_rows) > 0:
    print("\nFlagged Outlier Rows:")
    print(outlier_rows[['Date', 'Category', 'Amount', 'Type']].to_string(index=True))

    print("""
Interpretation:
  - HIGH outliers (above upper bound): unusually large transactions
  - LOW outliers (below lower bound): unusually small transactions
  - Each flagged row should be reviewed in context

REMEMBER: IQR flags potential outliers â€” they are not confirmed errors!
""")

# ============================================================================
# SECTION 6: Threshold-Based Rule
# ============================================================================
print("\n" + "=" * 70)
print("6. OUTLIER DETECTION USING A THRESHOLD RULE")
print("=" * 70)

print("""
Threshold rules are domain-specific checks.

Examples:
  - Flag amounts > $1000  (large transaction alert)
  - Flag amounts < $1     (suspiciously small transaction)
  - Flag if amount > mean + 3 Ã— std  (3-sigma rule)

These rules are simpler than IQR and useful when you have domain knowledge.
""")

# Threshold rule: amount > 500 or < 5
high_threshold = 500.0
low_threshold  = 5.0

threshold_flags = df_demo[
    (df_demo['Amount'] > high_threshold) | (df_demo['Amount'] < low_threshold)
].copy()

print(f"Threshold Rule: Amount > ${high_threshold} OR Amount < ${low_threshold}")
print(f"Flagged rows : {len(threshold_flags)}")
if len(threshold_flags) > 0:
    print("\nFlagged Rows:")
    print(threshold_flags[['Date', 'Category', 'Amount', 'Type']].to_string(index=True))

# 3-sigma rule
mean_val = df_demo['Amount'].mean()
std_val  = df_demo['Amount'].std()
sigma_upper = mean_val + 3 * std_val
sigma_lower = mean_val - 3 * std_val

sigma_flags = df_demo[
    (df_demo['Amount'] > sigma_upper) | (df_demo['Amount'] < sigma_lower)
].copy()

print(f"\n3-Sigma Rule: Mean Â± 3 Ã— Std")
print(f"  Mean   : ${mean_val:.2f}")
print(f"  Std    : ${std_val:.2f}")
print(f"  Upper  : ${sigma_upper:.2f}")
print(f"  Lower  : ${sigma_lower:.2f}")
print(f"  Flagged: {len(sigma_flags)} row(s)")

if len(sigma_flags) > 0:
    print(sigma_flags[['Date', 'Category', 'Amount', 'Type']].to_string(index=True))

# ============================================================================
# SECTION 7: Visual Comparison â€” Normal vs Flagged
# ============================================================================
print("\n" + "=" * 70)
print("7. VISUAL COMPARISON: BOXPLOT BY CATEGORY")
print("=" * 70)

print("""
Comparing distributions by category reveals category-specific outliers.
A transaction that looks normal overall may be extreme within its category.
""")

categories = df_demo['Category'].unique()
data_by_cat = [df_demo[df_demo['Category'] == c]['Amount'].values for c in categories]

fig, ax = plt.subplots(figsize=(12, 6))
bp = ax.boxplot(data_by_cat,
                tick_labels=categories,
                patch_artist=True,
                boxprops=dict(facecolor='#A9DFBF', color='#1E8449'),
                whiskerprops=dict(color='#1E8449', linewidth=1.5),
                capprops=dict(color='#1E8449', linewidth=1.5),
                medianprops=dict(color='red', linewidth=2.5),
                flierprops=dict(marker='D', markerfacecolor='crimson',
                                markeredgecolor='darkred', markersize=8))

ax.set_title('Outlier Detection by Category\n(Diamonds beyond whiskers = potential outliers)',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Category', fontsize=11)
ax.set_ylabel('Amount ($)', fontsize=11)
ax.tick_params(axis='x', rotation=15)
ax.grid(axis='y', alpha=0.35, linestyle='--')
plt.tight_layout()

cat_path = os.path.join(output_dir, 'outlier_boxplot_by_category.png')
plt.savefig(cat_path, dpi=150)
print(f"âœ“ Category boxplot saved: {cat_path}")
plt.close()

# ============================================================================
# SECTION 8: Interpreting Outliers Carefully
# ============================================================================
print("\n" + "=" * 70)
print("8. INTERPRETING OUTLIERS CAREFULLY")
print("=" * 70)

print("""
Detecting an outlier is only the beginning. Interpretation matters.

Questions to Ask Before Acting:
---------------------------------
1. Is this value technically possible?       (e.g., negative age = impossible)
2. Is this value domain-reasonable?          (e.g., $5,000 healthcare = plausible)
3. Could this be a data entry error?         (e.g., $12,000 instead of $120?)
4. Is this a rare but real event?            (e.g., annual insurance premium)
5. How many outliers are there?              (1 vs 10% of data â€” very different)
6. Does removing it change the analysis?     (test with and without)

Decision Guide:
---------------
+---------------------+---------------------------+---------------------------+
| Scenario            | Likely Cause              | Suggested Action          |
+---------------------+---------------------------+---------------------------+
| Amount = $0.50      | Data error / test record  | Flag and investigate       |
| Amount = $1,850     | Large purchase (valid?)   | Investigate context        |
| Amount = -$50       | Refund / error            | Check data source          |
| Amount = $999,999   | Typo / system error       | Likely error, investigate  |
+---------------------+---------------------------+---------------------------+

âš ï¸  NEVER automatically remove outliers without understanding them.
âœ“   ALWAYS document your reasoning for any outlier decision.
""")

# ============================================================================
# SECTION 9: Summary of Findings
# ============================================================================
print("\n" + "=" * 70)
print("9. OUTLIER DETECTION SUMMARY")
print("=" * 70)

iqr_count   = outlier_mask.sum()
thresh_count = len(threshold_flags)
sigma_count  = len(sigma_flags)

print(f"""
Detection Method        | Flagged Outliers
------------------------|----------------
IQR Rule (1.5 Ã— IQR)    | {iqr_count} row(s)
Threshold Rule (>500/<5) | {thresh_count} row(s)
3-Sigma Rule (MeanÂ±3Ïƒ)  | {sigma_count} row(s)

Plots Generated:
  âœ“ outlier_boxplot_amount.png        â€” Single column visual inspection
  âœ“ outlier_scatter_amount.png        â€” Index scatter with bounds
  âœ“ outlier_boxplot_by_category.png   â€” Category-level comparison

Key Takeaways:
  1. Visual inspection (boxplot, scatter) gives instant outlier signals
  2. IQR rule is robust â€” not influenced by the extreme values themselves
  3. Threshold rules are useful when domain knowledge defines 'normal'
  4. Multiple methods together give more confidence
  5. Flags are starting points for investigation â€” NOT final verdicts

Next Steps After Detection:
  - Investigate flagged rows in the original data source
  - Consult domain experts if uncertain
  - Document findings clearly
  - Decide: keep, transform, or remove â€” with justification
""")

print("=" * 70)
print("OUTLIER DETECTION MILESTONE â€” COMPLETE")
print("=" * 70)
