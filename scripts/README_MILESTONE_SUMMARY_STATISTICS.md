# Summary Statistics Milestone

## Overview
This milestone focuses on computing basic summary statistics for individual columns in a Pandas DataFrame. Summary statistics help you quickly understand the distribution, central tendency, and spread of your data before making any decisions or assumptions. These statistics form the foundation of Exploratory Data Analysis (EDA).

## Learning Objectives
By completing this milestone, you will:
- Understand what summary statistics represent (mean, median, min, max, std)
- Compute basic statistics for numeric columns
- Interpret statistical outputs correctly
- Compare statistics across different columns and groups
- Build intuition about data distributions
- Identify unusual values using summaries
- Use statistics to guide further analysis

## File Structure
```
scripts/
  └── summary_statistics_milestone.py    # Main script demonstrating summary statistics
data/
  └── raw/
      └── sample_transactions.csv        # Sample CSV file with transaction data
```

## Prerequisites
- Python 3.x installed
- Pandas library installed (`pip install pandas`)
- Basic understanding of Pandas DataFrames
- Completed Pandas DataFrames milestone (recommended)

## How to Run
1. Navigate to the scripts directory:
   ```bash
   cd scripts
   ```

2. Run the Python script:
   ```bash
   python summary_statistics_milestone.py
   ```

## What the Script Demonstrates

### 1. Understanding Common Summary Statistics
The script explains what each statistic means:

| Statistic | Description | What It Tells You |
|-----------|-------------|-------------------|
| **COUNT** | Number of non-missing values | Data completeness |
| **MEAN** | Average value (sum / count) | Central tendency (affected by outliers) |
| **MEDIAN** | Middle value when sorted | Central tendency (resistant to outliers) |
| **MIN** | Smallest value | Lower bound of data range |
| **MAX** | Largest value | Upper bound of data range |
| **STD** | Standard deviation | Spread/variability around mean |
| **25%/75%** | First and third quartiles | Data distribution quartiles |

**Key Insight:** Comparing mean vs median reveals data skewness and outlier presence.

### 2. Computing Statistics for a Single Column
The script demonstrates column-level analysis:

```python
# Select a numeric column
amount_column = df['Amount']

# Compute individual statistics
print(f"Count: {amount_column.count()}")
print(f"Mean: ${amount_column.mean():.2f}")
print(f"Median: ${amount_column.median():.2f}")
print(f"Min: ${amount_column.min():.2f}")
print(f"Max: ${amount_column.max():.2f}")
print(f"Std: ${amount_column.std():.2f}")

# Or use describe() for all statistics at once
print(amount_column.describe())
```

**Output includes:**
- Individual statistic calculations with explanations
- Interpretation of what each number means
- Context-specific insights (e.g., "average transaction is $X")

### 3. Interpreting Results Correctly
The script teaches proper interpretation:

**Mean vs Median Comparison:**
- If Mean > Median: Right-skewed data (few high values pulling average up)
- If Mean < Median: Left-skewed data (few low values pulling average down)
- If Mean ≈ Median: Roughly symmetric distribution

**Understanding Standard Deviation:**
```python
# About 68% of data falls within mean ± 1 std
print(f"68% of values: ${mean - std:.2f} to ${mean + std:.2f}")
```

**Identifying Outliers:**
```python
# Using IQR method
q1 = amount_column.quantile(0.25)
q3 = amount_column.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
```

### 4. Comparing Columns Using Statistics
The script demonstrates comparative analysis:

**Group-by Statistics:**
```python
# Compare statistics across categories
category_stats = df.groupby('Category')['Amount'].describe()
print(category_stats)

# Find category with highest average
max_mean_category = df.groupby('Category')['Amount'].mean().idxmax()
```

**Key Comparisons:**
- Which category has the highest average amount?
- Which category has the most variability (highest std)?
- Which category has the lowest minimum transaction?

### 5. Using Statistics to Guide Further Analysis
The script shows how statistics inform next steps:

**Questions Statistics Help Answer:**
1. Are there unusual patterns in spending?
2. Which categories need budget adjustments?
3. Is there high variability that needs investigation?
4. Are there data quality issues?

**Summary Statistics Example:**
```
Total Transactions: 100
Total Amount:       $12,345.67
Average Amount:     $123.46
Median Amount:      $98.50
Amount Range:       $15.00 - $500.00
Categories:         8
```

### 6. Common Mistakes to Avoid

The script highlights critical mistakes:

❌ **Mistake 1:** Relying only on mean without checking median
   - ✓ Solution: Always compare mean vs median

❌ **Mistake 2:** Ignoring standard deviation
   - ✓ Solution: Check spread alongside central tendency

❌ **Mistake 3:** Not verifying counts for missing data
   - ✓ Solution: Check count vs total rows

❌ **Mistake 4:** Interpreting statistics without context
   - ✓ Solution: Understand what the data represents

❌ **Mistake 5:** Computing statistics on non-numeric columns
   - ✓ Solution: Verify data types first

## Key Concepts Covered

### Essential Methods
| Method | Purpose | Example Output |
|--------|---------|----------------|
| `.count()` | Count non-missing values | 100 |
| `.mean()` | Calculate average | 123.45 |
| `.median()` | Find middle value | 98.50 |
| `.min()` | Find minimum | 15.00 |
| `.max()` | Find maximum | 500.00 |
| `.std()` | Calculate standard deviation | 87.23 |
| `.describe()` | All statistics at once | Series with all stats |
| `.quantile(q)` | Get specific quantile | 75.00 (for q=0.25) |

### Statistical Interpretation Skills
- **Central Tendency:** Understanding mean vs median
- **Spread:** Interpreting standard deviation and range
- **Distribution Shape:** Recognizing skewness from statistics
- **Outlier Detection:** Using IQR method
- **Comparative Analysis:** Group-by statistics

### Data Understanding Principles
- Always inspect statistics before analysis
- Statistics describe data, not explanations
- Use summaries alongside visual inspection
- Avoid overinterpreting single metrics
- Context matters for interpretation

## Expected Output
When you run the script, you'll see:

1. **Section 1:** Explanation of what summary statistics represent
2. **Section 2:** Dataset loading confirmation and structure
3. **Section 3:** Detailed single-column statistics with interpretation
4. **Section 4:** Mean vs median comparison and outlier detection
5. **Section 5:** Comparative statistics across categories
6. **Section 6:** Guidance on using statistics for further analysis
7. **Section 7:** Common mistakes and how to avoid them

## Practice Exercises

After running the script, try these exercises:

1. **Basic Practice:**
   - Compute statistics for all numeric columns
   - Compare mean and median for each
   - Identify which column has the highest variability

2. **Intermediate:**
   - Group by different categorical columns
   - Find the category with highest average
   - Identify potential outliers in each group

3. **Advanced:**
   - Calculate statistics for filtered subsets
   - Compare statistics before/after removing outliers
   - Create a summary table comparing multiple categories

## Video Walkthrough Requirements

Create a ~2 minute screen-capture video demonstrating:

### Required Content:
1. **Select a Column** (20 seconds)
   - Show selecting the Amount column
   - Print first few values

2. **Compute Statistics** (40 seconds)
   - Calculate mean, median, min, max
   - Show using `.describe()` method
   - Explain what each number means

3. **Interpret Results** (40 seconds)
   - Compare mean vs median
   - Explain standard deviation
   - Mention what the range tells you

4. **Compare with Another Category** (20 seconds)
   - Show group-by statistics
   - Compare two categories briefly

### Video Tips:
- Show your screen clearly (full screen terminal/editor)
- Explain as you type or run commands
- Point out key numbers and their meaning
- Keep it concise and focused
- Ensure output is readable

### Submission:
- Upload video to designated platform
- Submit link as instructed
- Ensure video is approximately 2 minutes
- Verify video is screen-facing and visible

## Why This Matters

### Real-World Applications:
- **Personal Finance:** Understanding spending patterns
- **Business Analytics:** Customer behavior analysis
- **Data Quality:** Detecting errors and outliers
- **Decision Making:** Data-driven budget planning
- **Research:** Initial data exploration

### Foundation for Advanced Topics:
- Visualization (histograms, box plots)
- Hypothesis testing
- Machine learning feature understanding
- Time series analysis
- A/B testing

### Professional Skills:
- Data summarization
- Quick data assessment
- Effective communication of findings
- Statistical literacy
- Critical thinking about data

## Common Issues and Solutions

### Issue 1: Statistics Not Computing
**Problem:** Getting NaN or errors
**Solution:** Check data types - ensure column is numeric

```python
# Verify data type
print(df['Amount'].dtype)

# Convert if needed
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
```

### Issue 2: Unexpected Results
**Problem:** Mean seems wrong
**Solution:** Check for missing values and outliers

```python
# Check missing values
print(df['Amount'].isnull().sum())

# Check for outliers
print(df['Amount'].sort_values())
```

### Issue 3: File Not Found Error
**Problem:** Cannot load CSV
**Solution:** Check file path

```python
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(os.path.dirname(current_dir), 'data', 'raw', 'sample_transactions.csv')
```

## Additional Resources

### Recommended Reading (Optional):
- [Pandas Descriptive Statistics Documentation](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics)
- [Understanding Mean vs Median](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data)
- [Standard Deviation Explained Simply](https://www.mathsisfun.com/data/standard-deviation.html)

### Next Milestones:
- Data Visualization (histograms, box plots)
- Data Filtering and Subsetting
- Handling Outliers
- Time Series Analysis
- Correlation Analysis

## Completion Checklist

Before marking this milestone complete, ensure you can:

- [ ] Load a DataFrame and select numeric columns
- [ ] Compute mean, median, min, max for a column
- [ ] Use `.describe()` to get all statistics at once
- [ ] Interpret what each statistic tells you
- [ ] Compare mean vs median to understand distribution
- [ ] Understand what standard deviation indicates
- [ ] Use group-by to compare statistics across categories
- [ ] Identify potential outliers using statistics
- [ ] Verify data types before computing statistics
- [ ] Explain statistics in simple, non-technical terms

## Summary

Computing summary statistics is a fundamental EDA skill. This milestone ensures you can:
- Quantitatively understand individual columns
- Interpret statistics in context
- Identify data patterns and issues early
- Make informed analysis decisions
- Communicate findings clearly

**Remember:** Always understand your data numerically before building models or making decisions. Summary statistics are your first quantitative snapshot of the data.

---

**Milestone Difficulty:** Beginner  
**Estimated Time:** 30-45 minutes  
**Prerequisites:** Pandas DataFrames  
**Type:** Data Understanding (No modeling required)
