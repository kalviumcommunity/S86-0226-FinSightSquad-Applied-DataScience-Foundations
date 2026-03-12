"""
Boxplot Visualization Milestone
================================
This script demonstrates visualizing data distributions using boxplots.
Boxplots provide a compact summary of a dataset's distribution, making it 
easy to compare spread, central tendency, and potential outliers.

Learning Objectives:
- Understand what a boxplot represents
- Visualize distribution spread using quartiles
- Identify median and interquartile range (IQR)
- Detect potential outliers visually
- Compare distributions across multiple columns
"""

# Step 1: Import required libraries
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import os

print("=" * 70)
print("BOXPLOT VISUALIZATION MILESTONE")
print("=" * 70)

# ============================================================================
# SECTION 1: Understanding Boxplots
# ============================================================================
print("\n1. UNDERSTANDING BOXPLOTS")
print("-" * 70)
print("""
A boxplot (box-and-whisker plot) shows a 5-number summary of data:
- Minimum (lower whisker)
- First Quartile (Q1 - 25th percentile) - bottom of box
- Median (Q2 - 50th percentile) - line inside box
- Third Quartile (Q3 - 75th percentile) - top of box
- Maximum (upper whisker)

Key Components:
---------------
BOX          : Contains middle 50% of data (from Q1 to Q3)
LINE IN BOX  : Represents the median value
WHISKERS     : Extend to min/max (within 1.5 × IQR from quartiles)
DOTS/CIRCLES : Outliers beyond whiskers
IQR          : Interquartile Range (Q3 - Q1) - measures spread

Why Boxplots Matter:
- Quick visual summary of distribution
- Easy comparison across multiple columns
- Clear outlier identification
- Shows spread and skewness at a glance
- Complements histograms for EDA
""")

# ============================================================================
# SECTION 2: Load and Prepare Data
# ============================================================================
print("\n2. LOADING TRANSACTION DATA")
print("-" * 70)

# Get the path to the CSV file (parent directory's data/raw folder)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
csv_path = os.path.join(parent_dir, 'data', 'raw', 'sample_transactions.csv')

# Load the data
df = pd.read_csv(csv_path)

print(f"Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nFirst few rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nNumeric columns available for boxplot:")
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
print(numeric_cols)

# ============================================================================
# SECTION 3: Creating a Boxplot for a Single Column
# ============================================================================
print("\n" + "=" * 70)
print("3. CREATING A BOXPLOT FOR A SINGLE COLUMN")
print("=" * 70)

print("""
Let's create a boxplot for the 'Amount' column to visualize the 
distribution of transaction amounts.
""")

# Compute summary statistics first
print("\nSummary statistics for Amount column:")
print(df['Amount'].describe())

# Create a boxplot for the Amount column
plt.figure(figsize=(8, 6))
plt.boxplot(df['Amount'], vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'))

plt.title('Distribution of Transaction Amounts', fontsize=14, fontweight='bold')
plt.ylabel('Amount ($)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Save the figure
output_dir = os.path.join(parent_dir, 'outputs', 'figures')
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'boxplot_single_column.png'), dpi=150)
print(f"\n✓ Boxplot saved to: {os.path.join(output_dir, 'boxplot_single_column.png')}")

plt.show()

# ============================================================================
# SECTION 4: Interpreting the Boxplot
# ============================================================================
print("\n" + "=" * 70)
print("4. INTERPRETING THE BOXPLOT")
print("=" * 70)

# Calculate key values manually for interpretation
q1 = df['Amount'].quantile(0.25)
q2 = df['Amount'].quantile(0.50)  # median
q3 = df['Amount'].quantile(0.75)
iqr = q3 - q1
lower_whisker = df['Amount'].min()
upper_whisker = df['Amount'].max()

# Calculate outlier boundaries
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identify outliers
outliers = df[(df['Amount'] < lower_bound) | (df['Amount'] > upper_bound)]['Amount']

print(f"""
Boxplot Interpretation for 'Amount' Column:
-------------------------------------------
Median (Q2)         : ${q2:.2f}  ← Middle value (50% above, 50% below)
First Quartile (Q1) : ${q1:.2f}  ← 25% of data is below this
Third Quartile (Q3) : ${q3:.2f}  ← 75% of data is below this
IQR (Q3 - Q1)       : ${iqr:.2f}  ← Spread of middle 50% of data
Lower Whisker       : ${lower_whisker:.2f}
Upper Whisker       : ${upper_whisker:.2f}

Outlier Boundaries:
Lower Bound        : ${lower_bound:.2f}  (Q1 - 1.5 × IQR)
Upper Bound        : ${upper_bound:.2f}  (Q3 + 1.5 × IQR)
Number of Outliers : {len(outliers)}

Key Insights:
- The median shows the typical transaction amount
- The box height (IQR) shows variability in typical transactions
- Outliers (if any) may represent unusual spending patterns
- Symmetry of box indicates distribution shape
""")

if len(outliers) > 0:
    print(f"\nOutlier values detected:")
    print(outliers.values)
    print("""
    ⚠️ NOTE: Outliers are not always errors!
    They may represent:
    - Large one-time purchases
    - Rare but legitimate transactions
    - Data entry errors (need verification)
    
    Always investigate outliers in context before removing them.
    """)
else:
    print("\n✓ No outliers detected in this dataset.")

# ============================================================================
# SECTION 5: Comparing Boxplots Across Multiple Columns
# ============================================================================
print("\n" + "=" * 70)
print("5. COMPARING BOXPLOTS ACROSS CATEGORIES")
print("=" * 70)

print("""
One of boxplot's strengths is comparing distributions side by side.
Let's compare transaction amounts across different categories.
""")

# Group by category and create side-by-side boxplots
categories = df['Category'].unique()
data_by_category = [df[df['Category'] == cat]['Amount'].values for cat in categories]

plt.figure(figsize=(12, 6))
box_parts = plt.boxplot(data_by_category, 
                        labels=categories,
                        patch_artist=True,
                        boxprops=dict(facecolor='lightgreen', color='darkgreen'),
                        whiskerprops=dict(color='darkgreen'),
                        capprops=dict(color='darkgreen'),
                        medianprops=dict(color='red', linewidth=2),
                        flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'))

# Color each box differently for better visualization
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lavender']
for patch, color in zip(box_parts['boxes'], colors[:len(categories)]):
    patch.set_facecolor(color)

plt.title('Transaction Amount Distribution by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig(os.path.join(output_dir, 'boxplot_comparison.png'), dpi=150)
print(f"\n✓ Comparison boxplot saved to: {os.path.join(output_dir, 'boxplot_comparison.png')}")

plt.show()

# Print comparison statistics
print("\nComparison Statistics by Category:")
print("-" * 70)
comparison_stats = df.groupby('Category')['Amount'].agg([
    ('Count', 'count'),
    ('Median', 'median'),
    ('Mean', 'mean'),
    ('Std', 'std'),
    ('Min', 'min'),
    ('Max', 'max')
]).round(2)
print(comparison_stats)

print("""
Insights from Comparison:
- Categories with higher boxes have more variability
- Compare medians (red lines) to see typical amounts per category
- Wider boxes indicate more spread in that category
- Categories with outliers need special attention
- Helps identify which categories have unusual spending patterns
""")

# ============================================================================
# SECTION 6: Using Pandas Built-in Boxplot
# ============================================================================
print("\n" + "=" * 70)
print("6. USING PANDAS BUILT-IN BOXPLOT METHOD")
print("=" * 70)

print("""
Pandas provides a convenient .boxplot() method for quick visualization.
This is useful for rapid EDA without manual matplotlib configuration.
""")

# Create boxplot using Pandas
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(column='Amount', by='Category', ax=ax, grid=False,
           patch_artist=True)

plt.suptitle('')  # Remove default title
plt.title('Transaction Amounts by Category (Pandas Method)', fontsize=14, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the figure
plt.savefig(os.path.join(output_dir, 'boxplot_pandas_method.png'), dpi=150)
print(f"\n✓ Pandas boxplot saved to: {os.path.join(output_dir, 'boxplot_pandas_method.png')}")

plt.show()

# ============================================================================
# SECTION 7: Best Practices and Important Notes
# ============================================================================
print("\n" + "=" * 70)
print("7. BEST PRACTICES FOR BOXPLOTS")
print("=" * 70)

print("""
✓ DO:
-----
- Use boxplots for numeric data only
- Combine boxplots with summary statistics for complete understanding
- Compare multiple distributions side by side
- Investigate outliers in context (don't remove blindly)
- Use boxplots as part of comprehensive EDA
- Consider the scale when comparing multiple columns
- Look at both median and IQR for full picture

✗ DON'T:
--------
- Don't use boxplots for categorical data
- Don't remove outliers without investigation
- Don't rely only on boxplots (use histograms too)
- Don't ignore the context of your data
- Don't assume all outliers are errors
- Don't compare boxplots with very different scales directly

Key Takeaways:
--------------
1. Boxplots summarize distributions using 5 key numbers
2. They make outlier detection visual and immediate
3. Side-by-side comparison is their major strength
4. Always interpret outliers in context
5. Combine with other EDA tools for best results
""")

# ============================================================================
# COMPLETION MESSAGE
# ============================================================================
print("\n" + "=" * 70)
print("MILESTONE COMPLETE!")
print("=" * 70)
print("""
Congratulations! You have completed the Boxplot Visualization Milestone.

You now know how to:
✓ Create boxplots for single columns
✓ Interpret median, quartiles, and IQR
✓ Identify outliers visually
✓ Compare distributions across multiple columns
✓ Use boxplots as an effective EDA tool

Next Steps:
1. Record your 2-minute video demonstration
2. Submit your code and video link as instructed
3. Explore bonus resources for deeper understanding

All generated figures are saved in: {}/outputs/figures/
""".format(parent_dir))
