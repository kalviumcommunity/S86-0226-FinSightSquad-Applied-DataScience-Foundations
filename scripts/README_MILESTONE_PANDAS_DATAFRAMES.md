# Pandas DataFrames Milestone

## Overview
This milestone focuses on creating Pandas DataFrames from dictionaries and files, which is a core skill for working with real-world data. DataFrames are the primary structure used in Pandas to represent tabular data similar to spreadsheets or database tables.

## Learning Objectives
By completing this milestone, you will:
- Understand what a Pandas DataFrame represents
- Create DataFrames from Python dictionaries
- Load DataFrames from common file formats (CSV)
- Inspect DataFrame structure and contents
- Recognize common issues during data loading

## File Structure
```
scripts/
  └── pandas_dataframes_milestone.py    # Main script demonstrating DataFrame operations
data/
  └── raw/
      └── sample_transactions.csv       # Sample CSV file for loading demonstration
```

## Prerequisites
- Python 3.x installed
- Pandas library installed (`pip install pandas`)
- Basic understanding of Python dictionaries

## How to Run
1. Navigate to the scripts directory:
   ```bash
   cd scripts
   ```

2. Run the Python script:
   ```bash
   python pandas_dataframes_milestone.py
   ```

## What the Script Demonstrates

### 1. Understanding DataFrames
- What a DataFrame represents (2D labeled data structure)
- Comparison to spreadsheets and database tables
- Key components: rows, columns, index, values

### 2. Creating DataFrames from Dictionaries
The script demonstrates two examples:

**Example 1: Monthly Expenses**
```python
expenses_dict = {
    'Month': ['January', 'February', 'March', 'April'],
    'Income': [5000, 5200, 4800, 5100],
    'Expenses': [3200, 3500, 3100, 3300],
    'Savings': [1800, 1700, 1700, 1800]
}
df_expenses = pd.DataFrame(expenses_dict)
```

**Example 2: Stock Portfolio**
```python
portfolio_dict = {
    'Stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'Shares': [10, 5, 15, 3, 8],
    'Purchase_Price': [150.5, 2800.0, 300.25, 3400.0, 700.0],
    'Current_Price': [175.0, 2900.0, 350.0, 3500.0, 750.0]
}
df_portfolio = pd.DataFrame(portfolio_dict)
```

### 3. Loading DataFrames from Files
Demonstrates loading a CSV file using `pd.read_csv()`:
```python
df_transactions = pd.read_csv('sample_transactions.csv')
```

The sample CSV contains transaction data with columns:
- Date
- Category
- Amount
- Type
- Payment_Method

### 4. Inspecting DataFrame Structure
The script demonstrates essential methods for inspecting DataFrames:

| Method | Purpose |
|--------|---------|
| `df.head()` | View first few rows |
| `df.tail()` | View last few rows |
| `df.shape` | Get dimensions (rows, columns) |
| `df.columns` | Get column names |
| `df.dtypes` | Check data types |
| `df.info()` | Comprehensive overview |
| `df.describe()` | Statistical summary |
| `df.isnull().sum()` | Check for missing values |
| `df['column'].unique()` | Get unique values |
| `df['column'].value_counts()` | Count occurrences |

## Key Concepts Covered

### DataFrame vs Series
- **DataFrame**: 2D table with rows and columns
- **Series**: 1D array (single column)
- Accessing one column returns a Series
- Accessing multiple columns returns a DataFrame

### Dictionary to DataFrame Conversion
- Dictionary keys → Column names
- Dictionary values → Column data (must be equal length)
- Each key-value pair becomes a column

### File Loading Considerations
- Headers are automatically detected from the first row
- File paths can be relative or absolute
- Common formats: CSV, Excel, JSON, SQL
- `pd.read_csv()` is the most common method

### Data Inspection Best Practices
1. **Always inspect after loading**: Use `head()` to verify data loaded correctly
2. **Check shape**: Ensure expected number of rows and columns
3. **Verify data types**: Ensure columns have correct types (int, float, string, etc.)
4. **Look for missing values**: Use `isnull().sum()` to find gaps in data
5. **Understand the index**: Default is numeric (0, 1, 2...) but can be customized

## Common Beginner Issues

### Issue 1: Dictionary Lists of Different Lengths
❌ **Wrong:**
```python
data = {'A': [1, 2], 'B': [3, 4, 5]}  # Different lengths!
df = pd.DataFrame(data)  # Error!
```

✅ **Correct:**
```python
data = {'A': [1, 2, 3], 'B': [3, 4, 5]}  # Same length
df = pd.DataFrame(data)
```

### Issue 2: File Not Found
❌ **Wrong:**
```python
df = pd.read_csv('data.csv')  # File doesn't exist or wrong path
```

✅ **Correct:**
```python
import os
file_path = os.path.join('data', 'raw', 'data.csv')
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    print("File not found!")
```

### Issue 3: Confusion Between Series and DataFrame
```python
# Single column access returns Series
series = df['Amount']  # Series
print(type(series))  # <class 'pandas.core.series.Series'>

# Multiple columns return DataFrame
df_subset = df[['Amount', 'Date']]  # DataFrame
print(type(df_subset))  # <class 'pandas.core.frame.DataFrame'>
```

## Output Sections
When you run the script, you'll see:

1. **Section 1**: Conceptual explanation of DataFrames
2. **Section 2**: Dictionary to DataFrame examples
3. **Section 3**: File loading demonstration
4. **Section 4**: Comprehensive inspection methods
5. **Section 5**: Summary and key takeaways

## Video Walkthrough Requirements
Create a ~2 minute screen-capture video demonstrating:

1. **Introduction (15 seconds)**
   - Explain what DataFrames are
   - Why they're important for data science

2. **Dictionary to DataFrame (30 seconds)**
   - Show creating a dictionary
   - Convert to DataFrame
   - Display the result

3. **File Loading (30 seconds)**
   - Show the CSV file content
   - Load it using pd.read_csv()
   - Display the loaded DataFrame

4. **Inspection Methods (30 seconds)**
   - Demonstrate head(), shape, columns
   - Show info() or describe()
   - Explain what each tells you

5. **Conclusion (15 seconds)**
   - Summarize importance
   - Mention next steps in data analysis

## Submission Checklist
- [ ] Script runs without errors
- [ ] All sections display correctly
- [ ] Sample CSV file is present
- [ ] DataFrames are created from dictionaries
- [ ] Data loads successfully from CSV
- [ ] Inspection methods demonstrate structure
- [ ] Video is recorded (~2 minutes)
- [ ] Video is screen-facing and clearly visible
- [ ] Video link is submitted as instructed

## Next Steps
After completing this milestone, you should:
1. Learn about data cleaning and handling missing values
2. Explore data filtering and selection techniques
3. Practice data transformations (groupby, merge, pivot)
4. Work with real-world datasets from sources like Kaggle

## Additional Resources
- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
- [DataFrame Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Why This Matters
> "Most real Data Science work begins with loading data correctly."

DataFrames are:
- The foundation of data analysis in Python
- Used in 90%+ of data science projects
- Essential for machine learning pipelines
- The bridge between raw data and insights

Mastering DataFrame creation ensures:
- ✅ You can handle external data confidently
- ✅ Your data is structured correctly from the start
- ✅ Downstream analysis is smoother
- ✅ You avoid common beginner mistakes

---

**Milestone Complete!** 🎉

You now have a solid foundation for working with Pandas DataFrames. Keep practicing with different datasets to build confidence.
