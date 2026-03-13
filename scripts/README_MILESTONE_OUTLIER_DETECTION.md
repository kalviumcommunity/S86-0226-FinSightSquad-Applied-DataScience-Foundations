# Outlier Detection Milestone

## Overview
This milestone focuses on detecting outliers using visual inspection and simple statistical rules. Outliers are data points that differ significantly from the majority of the data and can strongly influence analysis, statistics, and models if not identified early. Learning to spot outliers visually and with basic rules helps you decide when they deserve attention, investigation, or special handling.

## Learning Objectives
By completing this milestone, you will:
- Understand what outliers are and why they matter
- Detect outliers using visual inspection (boxplots and scatter plots)
- Apply simple statistical rules to flag potential outliers (IQR method, threshold checks)
- Distinguish between valid outliers and data errors
- Build informed judgment around outlier handling
- Avoid blindly removing extreme values

## File Structure
```
scripts/
  └── outlier_detection_milestone.py         # Main script for outlier detection
data/
  └── raw/
      └── sample_transactions.csv            # Sample CSV file with transaction data
outputs/
  └── figures/
      ├── outlier_boxplot_amount.png          # Single column boxplot with outliers highlighted
      ├── outlier_scatter_amount.png          # Scatter plot with IQR bounds
      └── outlier_boxplot_by_category.png     # Category-level boxplot comparison
```

## Prerequisites
- Python 3.x installed
- Required libraries:
  - Pandas (`pip install pandas`)
  - Matplotlib (`pip install matplotlib`)
  - NumPy (`pip install numpy`)
- Basic understanding of Pandas DataFrames
- Completed Summary Statistics milestone (recommended)
- Completed Boxplot Visualization milestone (recommended)

## How to Run
1. Navigate to the scripts directory:
   ```bash
   cd scripts
   ```

2. Run the Python script:
   ```bash
   python outlier_detection_milestone.py
   ```

3. View the generated plots in the `outputs/figures/` directory

## What the Script Demonstrates

### 1. Understanding Outliers
The script explains what makes a value an outlier:

| Outlier Type | Description | Example |
|--------------|-------------|---------|
| **Global Outlier** | Far from the entire dataset | $1,850 in a dataset of $50–$200 transactions |
| **Contextual Outlier** | Unusual in a specific context | $500 grocery when typical is $100 |
| **Collective Outlier** | Group of values unusual together | 10 back-to-back $999 charges |

**Why Outliers Matter:**
- Distort the mean significantly
- Inflate standard deviation
- Skew regression lines and model predictions
- May indicate data entry errors OR genuinely rare but valid events

### 2. Visual Detection — Boxplot
The script creates an annotated boxplot for the `Amount` column:

```python
plt.boxplot(df['Amount'], patch_artist=True,
            flierprops=dict(marker='o', markerfacecolor='red', markersize=9))
```

**How to Read the Boxplot for Outliers:**
- The **box** spans Q1 to Q3 (middle 50% of data)
- **Whiskers** extend to Q1 − 1.5×IQR and Q3 + 1.5×IQR
- Any **dot beyond the whiskers** is a potential outlier

### 3. Visual Detection — Scatter Plot
An index scatter plot reveals spikes and isolated values:

```python
colors = ['red' if (v < lower_bound or v > upper_bound) else 'blue'
          for v in df['Amount']]
plt.scatter(range(len(df)), df['Amount'], c=colors)
plt.axhline(upper_bound, color='red', linestyle='--')
plt.axhline(lower_bound, color='orange', linestyle='--')
```

**What to Look For:**
- Points far above or below the median line
- Unexplained isolated spikes in the plot

### 4. IQR Rule (Interquartile Range Method)
A robust statistical method not influenced by extreme values:

```python
q1 = df['Amount'].quantile(0.25)
q3 = df['Amount'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Amount'] < lower_bound) | (df['Amount'] > upper_bound)]
```

**Steps:**
1. Compute Q1 and Q3
2. Calculate IQR = Q3 − Q1
3. Set Lower Bound = Q1 − 1.5×IQR
4. Set Upper Bound = Q3 + 1.5×IQR
5. Flag values outside these bounds

### 5. Threshold-Based Rule
Domain-specific checks for custom definitions of "normal":

```python
# Business rule: flag unusually large or tiny transactions
high_threshold = 500.0
low_threshold  = 5.0
flagged = df[(df['Amount'] > high_threshold) | (df['Amount'] < low_threshold)]
```

**3-Sigma Rule:**
```python
mean = df['Amount'].mean()
std  = df['Amount'].std()
sigma_flags = df[(df['Amount'] > mean + 3*std) | (df['Amount'] < mean - 3*std)]
```

### 6. Careful Interpretation
The script emphasizes thoughtful decision-making:

| Scenario | Likely Cause | Suggested Action |
|----------|-------------|------------------|
| Amount = $0.50 | Test record / data error | Flag and investigate |
| Amount = $1,850 | Large valid purchase? | Investigate context |
| Amount = −$50 | Refund or entry error | Check data source |
| Amount = $999,999 | Typo / system error | Likely error, investigate |

## Key Concepts

### IQR Rule vs Threshold Rule

| Aspect | IQR Rule | Threshold Rule |
|--------|----------|----------------|
| **Based on** | Data distribution | Domain knowledge |
| **Adapts to data** | Yes | No |
| **Influenced by extremes** | No (uses middle 50%) | Depends on threshold |
| **Best for** | Unknown distributions | Known business rules |

### Why Not Remove Outliers Immediately?
- Outliers often carry **important information**
- They may represent **rare but real events**
- Removing them without justification **biases** the analysis
- Some models (e.g., fraud detection) **rely on** outlier patterns

## Common Mistakes to Avoid

❌ **Mistake 1:** Ignoring extreme values entirely  
✓ **Solution:** Always inspect unusual values — they may reveal data issues

❌ **Mistake 2:** Removing outliers automatically without investigation  
✓ **Solution:** Detect → Investigate → Decide with reasoning

❌ **Mistake 3:** Letting outliers distort mean and std  
✓ **Solution:** Use median and IQR for robust summaries alongside mean/std

❌ **Mistake 4:** Treating all outliers as errors  
✓ **Solution:** Consider context — a high healthcare bill is unusual but valid

❌ **Mistake 5:** Using only one detection method  
✓ **Solution:** Combine visual inspection with at least one statistical rule

## Detection Workflow

```
Load Data
    │
    ▼
Compute Summary Statistics  ←── Understand the typical range
    │
    ▼
Visual Inspection ──── Boxplot (IQR-based whiskers)
    │               └── Scatter Plot (index vs value)
    ▼
Apply Statistical Rules ──── IQR Rule (1.5 × IQR bounds)
    │                    └── Threshold or 3-Sigma Rule
    ▼
List Flagged Values
    │
    ▼
Investigate Context  ←── Is this a valid observation or an error?
    │
    ▼
Document Findings  ←── Record what was found and reasoning
    │
    ▼
Decide: Keep / Transform / Remove  ←── Only after full investigation
```

## Output Files

| File | Description |
|------|-------------|
| `outlier_boxplot_amount.png` | Boxplot with outlier values annotated in red |
| `outlier_scatter_amount.png` | Scatter plot with IQR reference lines |
| `outlier_boxplot_by_category.png` | Side-by-side boxplots per spending category |

## Bonus Resources
- **Understanding Outliers with Boxplots** — How the 5-number summary relates to outlier detection
- **IQR Explained** — Why 1.5×IQR is the standard threshold
- **Outlier Detection in EDA** — How outlier detection fits into the full EDA pipeline

---
*Outlier detection is a key EDA skill. Detect early, investigate carefully, act thoughtfully.*
