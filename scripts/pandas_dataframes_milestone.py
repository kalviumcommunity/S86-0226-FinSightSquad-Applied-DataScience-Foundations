"""
Pandas DataFrames Milestone
===========================
This script demonstrates creating and working with Pandas DataFrames from
dictionaries and files.

Learning Objectives:
- Import Pandas correctly
- Create DataFrames from dictionaries
- Load DataFrames from files
- Inspect DataFrame structure and contents
"""

# Step 1: Import Pandas
import pandas as pd
import os

print("=" * 60)
print("PANDAS DATAFRAMES MILESTONE")
print("=" * 60)

# ============================================================================
# SECTION 1: Understanding Pandas DataFrames
# ============================================================================
print("\n1. UNDERSTANDING PANDAS DATAFRAMES")
print("-" * 60)
print("""
A DataFrame is a 2-dimensional labeled data structure with columns.
Think of it like:
- A spreadsheet (Excel/Google Sheets)
- A database table
- A dictionary of Series objects

Key components:
- Rows: Individual records (indexed)
- Columns: Variables/features with names
- Index: Row labels (default: 0, 1, 2...)
- Values: The actual data
""")

# ============================================================================
# SECTION 2: Creating DataFrames from Dictionaries
# ============================================================================
print("\n2. CREATING DATAFRAMES FROM DICTIONARIES")
print("-" * 60)

# Example 1: Simple financial data
print("\nExample 1: Monthly Expenses")
expenses_dict = {
    'Month': ['January', 'February', 'March', 'April'],
    'Income': [5000, 5200, 4800, 5100],
    'Expenses': [3200, 3500, 3100, 3300],
    'Savings': [1800, 1700, 1700, 1800]
}

# Create DataFrame from dictionary
df_expenses = pd.DataFrame(expenses_dict)

print("\nDictionary structure:")
print(expenses_dict)

print("\nDataFrame created:")
print(df_expenses)

print("\nColumn names:")
print(df_expenses.columns.tolist())

print("\nData types:")
print(df_expenses.dtypes)

# Example 2: Stock portfolio data
print("\n" + "-" * 60)
print("Example 2: Stock Portfolio")
portfolio_dict = {
    'Stock': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'],
    'Shares': [10, 5, 15, 3, 8],
    'Purchase_Price': [150.5, 2800.0, 300.25, 3400.0, 700.0],
    'Current_Price': [175.0, 2900.0, 350.0, 3500.0, 750.0]
}

df_portfolio = pd.DataFrame(portfolio_dict)

print("\nStock Portfolio DataFrame:")
print(df_portfolio)

# Calculate profit/loss
df_portfolio['Profit_Loss'] = (df_portfolio['Current_Price'] - df_portfolio['Purchase_Price']) * df_portfolio['Shares']

print("\nWith calculated Profit/Loss column:")
print(df_portfolio)

# ============================================================================
# SECTION 3: Creating DataFrames from Files
# ============================================================================
print("\n3. CREATING DATAFRAMES FROM FILES")
print("-" * 60)

# Define file path
data_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
csv_file = os.path.join(data_folder, 'sample_transactions.csv')

# Check if file exists, if not, we'll create it
if not os.path.exists(csv_file):
    print(f"\nCreating sample CSV file at: {csv_file}")
    os.makedirs(data_folder, exist_ok=True)
    
    # Create sample data
    sample_data = pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-01-15', 
                 '2024-01-20', '2024-01-25', '2024-01-30'],
        'Category': ['Groceries', 'Transport', 'Entertainment', 'Utilities', 
                     'Groceries', 'Healthcare', 'Entertainment'],
        'Amount': [125.50, 45.00, 80.00, 150.00, 98.75, 200.00, 65.50],
        'Type': ['Expense', 'Expense', 'Expense', 'Expense', 
                 'Expense', 'Expense', 'Expense'],
        'Payment_Method': ['Credit Card', 'Cash', 'Debit Card', 'Bank Transfer',
                          'Credit Card', 'Insurance', 'Cash']
    })
    sample_data.to_csv(csv_file, index=False)
    print("Sample CSV file created successfully!")

# Load DataFrame from CSV
print(f"\nLoading data from CSV file...")
df_transactions = pd.read_csv(csv_file)

print("\nDataFrame loaded from CSV:")
print(df_transactions)

print("\nFile loading information:")
print(f"- File path: {csv_file}")
print(f"- Headers automatically detected: {df_transactions.columns.tolist()}")
print(f"- Rows loaded: {len(df_transactions)}")

# ============================================================================
# SECTION 4: Inspecting DataFrame Structure
# ============================================================================
print("\n4. INSPECTING DATAFRAME STRUCTURE")
print("-" * 60)

print("\nDataFrame: df_transactions")
print("\na) First 3 rows using head():")
print(df_transactions.head(3))

print("\nb) Last 3 rows using tail():")
print(df_transactions.tail(3))

print("\nc) Shape (rows, columns):")
print(f"Shape: {df_transactions.shape}")
print(f"Rows: {df_transactions.shape[0]}, Columns: {df_transactions.shape[1]}")

print("\nd) Column names:")
print(df_transactions.columns.tolist())

print("\ne) Data types:")
print(df_transactions.dtypes)

print("\nf) Basic information using info():")
print(df_transactions.info())

print("\ng) Statistical summary using describe():")
print(df_transactions.describe())

print("\nh) Index information:")
print(f"Index: {df_transactions.index}")
print(f"Index range: {df_transactions.index.min()} to {df_transactions.index.max()}")

# Additional inspection examples
print("\n" + "-" * 60)
print("Additional Inspection Examples:")
print("-" * 60)

print("\nAccessing a single column (returns a Series):")
print(df_transactions['Amount'])
print(f"Type: {type(df_transactions['Amount'])}")

print("\nAccessing multiple columns (returns a DataFrame):")
print(df_transactions[['Date', 'Category', 'Amount']])

print("\nChecking for missing values:")
print(df_transactions.isnull().sum())

print("\nUnique values in 'Category' column:")
print(df_transactions['Category'].unique())

print("\nValue counts for 'Category':")
print(df_transactions['Category'].value_counts())

# ============================================================================
# SECTION 5: Summary and Key Takeaways
# ============================================================================
print("\n5. SUMMARY AND KEY TAKEAWAYS")
print("=" * 60)
print("""
What we learned:

1. DataFrames are 2D labeled data structures (like tables/spreadsheets)

2. Creating from Dictionaries:
   - Keys become column names
   - Values become column data
   - Perfect for programmatic data creation

3. Loading from Files:
   - pd.read_csv() is the most common method
   - Headers are automatically detected
   - File path can be relative or absolute

4. Essential Inspection Methods:
   - df.head() / df.tail() → View rows
   - df.shape → Dimensions (rows, columns)
   - df.columns → Column names
   - df.dtypes → Data types
   - df.info() → Comprehensive overview
   - df.describe() → Statistical summary

5. Why DataFrames Matter:
   - Standard structure for data analysis
   - Easy data manipulation
   - Integration with visualization libraries
   - Foundation for machine learning

Next Steps:
- Learn data cleaning and handling missing values
- Explore data filtering and selection
- Practice data transformations
- Work with real-world datasets
""")

print("\n" + "=" * 60)
print("MILESTONE COMPLETE!")
print("=" * 60)
