# Boxplot Visualization Milestone

## Overview
This milestone focuses on visualizing data distributions using boxplots. Boxplots provide a compact summary of a dataset's distribution, making it easy to compare spread, central tendency, and potential outliers across one or more numeric columns. Boxplots complement histograms by highlighting quartiles and outliers clearly.

## Learning Objectives
By completing this milestone, you will:
- Understand what a boxplot represents and its components
- Visualize distribution spread using quartiles
- Identify median and interquartile range (IQR)
- Detect potential outliers visually
- Compare distributions across multiple columns
- Use boxplots as part of Exploratory Data Analysis (EDA)
- Interpret boxplots to make data-driven decisions

## File Structure
```
scripts/
  └── boxplot_visualization_milestone.py    # Main script demonstrating boxplots
data/
  └── raw/
      └── sample_transactions.csv           # Sample CSV file with transaction data
outputs/
  └── figures/
      ├── boxplot_single_column.png        # Single column boxplot
      ├── boxplot_comparison.png           # Multi-category comparison
      └── boxplot_pandas_method.png        # Pandas built-in method
```

## Prerequisites
- Python 3.x installed
- Required libraries:
  - Pandas (`pip install pandas`)
  - Matplotlib (`pip install matplotlib`)
- Basic understanding of Pandas DataFrames
- Completed Summary Statistics milestone (recommended)

## How to Run
1. Navigate to the scripts directory:
   ```bash
   cd scripts
   ```

2. Run the Python script:
   ```bash
   python boxplot_visualization_milestone.py
   ```

3. View the generated plots in the `outputs/figures/` directory

## What the Script Demonstrates

### 1. Understanding Boxplots
The script explains boxplot components:

| Component | Description | What It Shows |
|-----------|-------------|---------------|
| **Box** | Contains middle 50% of data | Interquartile Range (Q1 to Q3) |
| **Line in Box** | Red line inside the box | Median (50th percentile) |
| **Whiskers** | Lines extending from box | Min/Max values within 1.5 × IQR |
| **Dots/Circles** | Points beyond whiskers | Potential outliers |
| **IQR** | Height of the box (Q3 - Q1) | Spread of middle 50% |

**Key Insight:** Boxplots show distribution summary at a glance - center, spread, and outliers.

### 2. Creating a Boxplot for a Single Column
The script demonstrates single-column visualization:

```python
# Create a boxplot for the Amount column
plt.figure(figsize=(8, 6))
plt.boxplot(df['Amount'])
plt.title('Distribution of Transaction Amounts')
plt.ylabel('Amount ($)')
plt.show()
```

**Output includes:**
- Visual boxplot with colored components
- Interpretation of median, quartiles, and IQR
- Identification of any outliers
- Statistical summary alongside the plot

### 3. Comparing Boxplots Across Categories
The script shows side-by-side comparison:

```python
# Compare amounts across categories
data_by_category = [df[df['Category'] == cat]['Amount'] 
                    for cat in categories]
plt.boxplot(data_by_category, labels=categories)
```

**Comparison reveals:**
- Which categories have higher/lower typical values
- Which categories have more variability
- Which categories have outliers
- Relative spread across different groups

### 4. Interpreting Outliers
The script calculates outlier boundaries:

```python
q1 = df['Amount'].quantile(0.25)
q3 = df['Amount'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Amount'] < lower_bound) | 
              (df['Amount'] > upper_bound)]
```

**Important Notes:**
- Outliers are NOT always errors
- May represent legitimate extreme values
- Always investigate in context
- Don't remove blindly

### 5. Using Pandas Built-in Method
Quick boxplot creation using Pandas:

```python
df.boxplot(column='Amount', by='Category')
```

**Benefits:**
- Faster for exploratory analysis
- Less code required
- Automatic grouping support

## Key Concepts

### Five-Number Summary
A boxplot visualizes these five key statistics:
1. **Minimum** - Lower whisker endpoint
2. **Q1 (25th percentile)** - Bottom of box
3. **Median (50th percentile)** - Line in box
4. **Q3 (75th percentile)** - Top of box
5. **Maximum** - Upper whisker endpoint

### Interquartile Range (IQR)
- **Definition:** Q3 - Q1
- **Meaning:** Spread of the middle 50% of data
- **Usage:** Measure of variability resistant to outliers
- **Outlier Rule:** Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR

### When to Use Boxplots

✅ **Use boxplots when you need to:**
- Quickly see data distribution summary
- Compare distributions across groups
- Identify outliers visually
- Assess spread and symmetry
- Present data to non-technical audiences

❌ **Don't use boxplots when:**
- You need to see exact data distribution shape (use histogram)
- Dataset is very small (< 10 points)
- You need to see exact values (use scatter plot)
- Data is categorical (use bar chart)

## Common Pitfalls to Avoid

### 1. Misinterpreting the Box
❌ **Wrong:** "The box shows the full data range"
✅ **Correct:** "The box shows the middle 50% of data (Q1 to Q3)"

### 2. Treating All Outliers as Errors
❌ **Wrong:** "This point is an outlier, so I'll delete it"
✅ **Correct:** "This point is an outlier. Let me investigate why."

### 3. Ignoring Context
❌ **Wrong:** "Category A has outliers, it's bad data"
✅ **Correct:** "Category A has outliers - maybe large purchases are normal here"

### 4. Comparing Different Scales
❌ **Wrong:** Comparing boxplots of dollars vs. percentages directly
✅ **Correct:** Normalize or standardize before comparison

## Best Practices

### For Clear Boxplots:
1. **Label everything clearly** - axes, title, categories
2. **Use color thoughtfully** - different colors for different groups
3. **Show sample sizes** - especially when comparing groups
4. **Add grid lines** - makes reading values easier
5. **Rotate labels** - if category names are long

### For Better Analysis:
1. **Combine with summary statistics** - numbers + visuals
2. **Compare with histograms** - see full distribution shape
3. **Investigate outliers** - understand why they exist
4. **Consider sample size** - small samples have unstable outliers
5. **Look at the story** - what does the distribution tell you?

## Video Demonstration Requirements

Create a ~2 minute screen-capture video showing:

### Part 1: Single Column Boxplot (45 seconds)
- Load the transaction data
- Create a boxplot for the Amount column
- Point to and explain: box, median line, whiskers, outliers
- Interpret what the plot shows about the data

### Part 2: Comparing Categories (45 seconds)
- Create side-by-side boxplots for different categories
- Compare medians across categories
- Identify which categories have more variability
- Discuss any outliers observed

### Part 3: Interpretation (30 seconds)
- Explain what you learned from the boxplots
- Discuss how boxplots complement other EDA methods
- Show saved plot files

**Tips for a Great Video:**
- Keep it concise and focused
- Speak clearly and explain as you demonstrate
- Show your code and the resulting plots
- Highlight key insights
- Stay within 2 minutes (±15 seconds)

## Expected Output

When you run the script, you should see:

1. **Console Output:**
   - Explanation of boxplot components
   - Summary statistics for the Amount column
   - Interpretation of median, quartiles, IQR
   - Outlier detection results
   - Comparison statistics by category
   - Best practices and key takeaways

2. **Visual Output:**
   - Three boxplot figures displayed
   - Clear labels and colors
   - Professional-looking plots

3. **Saved Files:**
   - `boxplot_single_column.png`
   - `boxplot_comparison.png`
   - `boxplot_pandas_method.png`

## Submission Guidelines

1. **Code Submission:**
   - Submit as Pull Request (if required)
   - Include the Python script
   - Ensure all figures are generated successfully

2. **Video Submission:**
   - Duration: ~2 minutes (1:45 - 2:15 acceptable)
   - Format: Screen capture with clear visuals
   - Content: Cover all required sections
   - Quality: Clear audio and visible code/plots
   - Submit link as instructed

3. **Verification:**
   - Run script successfully
   - All three plots generated
   - Understand all interpretations
   - Can explain boxplot components

## Why This Matters

Common beginner issues:
- **Missing outliers** when relying only on averages
- **Difficulty comparing distributions** across columns
- **Over-reliance on histograms** for all insights
- **Misinterpreting spread and variability**

Boxplots solve these by:
- Making outliers immediately visible
- Enabling easy side-by-side comparison
- Showing spread and center simultaneously
- Providing a standard summary format

## Additional Resources

### Further Learning:
- [Pandas Boxplot Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html)
- [Understanding Boxplots](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)
- [Interpreting Outliers in Boxplots](https://www.statisticshowto.com/box-plot-outliers/)

### Related Milestones:
- Summary Statistics Milestone (foundation)
- Histogram Visualization (complementary skill)
- Line Plot Visualization (time series)

## Success Criteria

You have successfully completed this milestone when you can:

✅ Create a boxplot for any numeric column
✅ Explain what each component of a boxplot represents
✅ Calculate and interpret IQR
✅ Identify and interpret outliers
✅ Compare distributions using side-by-side boxplots
✅ Explain when to use boxplots vs. other visualizations
✅ Record a clear 2-minute video demonstration

---

**Remember:** Visualizing data distributions using boxplots is a powerful EDA skill. Boxplots summarize and compare numeric distributions clearly before you move deeper into analysis. Master this tool, and you'll make better data-driven decisions!
