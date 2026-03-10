#!/usr/bin/env python3
"""
Data Shapes and Column Data Types Milestone

This script demonstrates:
1. Understanding DataFrame shape
2. Identifying rows vs columns
3. Understanding column data types
4. Detecting type-related issues
5. Making informed decisions before data processing

Author: FinSightSquad
Date: 2026-03-09
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Set up paths
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "sample_transactions.csv"


def print_section_header(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def inspect_dataframe_shape(df):
    """
    1. Understanding DataFrame Shape
    
    Shape tells you how much data you're working with.
    - First number: number of rows (observations/records)
    - Second number: number of columns (features/variables)
    """
    print_section_header("1. INSPECTING DATAFRAME SHAPE")
    
    print(f"\nDataFrame Shape: {df.shape}")
    print(f"  - Number of Rows (Observations): {df.shape[0]}")
    print(f"  - Number of Columns (Features): {df.shape[1]}")
    
    print("\n📊 What this means:")
    print(f"   • We have {df.shape[0]} transaction records")
    print(f"   • Each transaction has {df.shape[1]} attributes")
    print(f"   • Total data points: {df.shape[0] * df.shape[1]}")


def understand_rows_columns(df):
    """
    2. Understanding Rows and Columns
    
    - Rows represent individual observations (e.g., transactions)
    - Columns represent features or variables (e.g., Date, Amount)
    """
    print_section_header("2. UNDERSTANDING ROWS AND COLUMNS")
    
    print("\n📋 Column Names:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i}. {col}")
    
    print(f"\n🔢 Total Records: {len(df)}")
    print(f"🏷️  Total Features: {len(df.columns)}")
    
    print("\n💡 Interpretation:")
    print("   • Each ROW = One transaction")
    print("   • Each COLUMN = One attribute of the transaction")
    print("   • This structure allows us to analyze spending patterns")


def inspect_column_data_types(df):
    """
    3. Understanding Column Data Types
    
    Data types control what operations are valid.
    Common Pandas data types:
    - int64: Integers
    - float64: Decimal numbers
    - object: Strings/text or mixed types
    - datetime64: Date and time values
    - bool: True/False values
    """
    print_section_header("3. INSPECTING COLUMN DATA TYPES")
    
    print("\n📝 Column Data Types:")
    print(df.dtypes)
    
    print("\n🔍 Detailed Type Analysis:")
    for col in df.columns:
        dtype = df[col].dtype
        print(f"\n   {col}:")
        print(f"      Type: {dtype}")
        print(f"      Sample values: {df[col].head(3).tolist()}")
        
        # Explain what this type means
        if dtype == 'object':
            print(f"      → Text/categorical data (strings)")
        elif dtype in ['int64', 'int32']:
            print(f"      → Integer numbers (whole numbers)")
        elif dtype in ['float64', 'float32']:
            print(f"      → Floating-point numbers (decimals)")
        elif 'datetime' in str(dtype):
            print(f"      → Date/time values")


def why_types_matter(df):
    """
    Demonstrate why correct data types matter
    """
    print_section_header("WHY DATA TYPES MATTER")
    
    print("\n✅ Correct Types Enable Proper Operations:")
    print(f"   • Average transaction amount: ${df['Amount'].mean():.2f}")
    print(f"   • Total spending: ${df['Amount'].sum():.2f}")
    print(f"   • Max transaction: ${df['Amount'].max():.2f}")
    
    print("\n⚠️  Wrong Types Cause Issues:")
    print("   If 'Amount' was stored as string:")
    
    # Demonstrate the problem
    amount_as_string = df['Amount'].astype(str)
    print(f"   • Trying to sum strings: '{amount_as_string.head(2).sum()}'")
    print("   • This concatenates instead of adding!")
    print("   • Analysis would be completely wrong!")


def detect_type_issues(df):
    """
    4. Detecting Type-Related Issues
    
    Recognize problems early to save time later.
    """
    print_section_header("4. DETECTING TYPE-RELATED ISSUES")
    
    print("\n🔎 Type Issue Detection:")
    
    # Check for numeric columns stored as objects
    print("\n   Checking for numeric columns stored as 'object':")
    for col in df.columns:
        if df[col].dtype == 'object':
            # Try to convert to numeric
            try:
                numeric_test = pd.to_numeric(df[col], errors='coerce')
                if numeric_test.notna().sum() > 0:
                    print(f"   ⚠️  '{col}' is object but contains numeric values!")
            except:
                print(f"   ✓  '{col}' is correctly stored as text")
        else:
            print(f"   ✓  '{col}' ({df[col].dtype}) - Type looks appropriate")
    
    # Check for missing values affecting types
    print("\n   Checking for missing values:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("   ⚠️  Missing values detected:")
        for col, count in missing[missing > 0].items():
            print(f"      - {col}: {count} missing ({count/len(df)*100:.1f}%)")
    else:
        print("   ✓  No missing values detected")
    
    # Check for potential date columns
    print("\n   Checking for date columns stored as text:")
    for col in df.columns:
        if 'date' in col.lower() and df[col].dtype == 'object':
            print(f"   ℹ️  '{col}' might be a date stored as text")
            print(f"      Consider converting: pd.to_datetime(df['{col}'])")


def demonstrate_proper_inspection_workflow(df):
    """
    Show the complete inspection workflow
    """
    print_section_header("COMPLETE INSPECTION WORKFLOW")
    
    print("\n📋 Step-by-Step Data Inspection:")
    
    # Step 1: First look at the data
    print("\n1️⃣  First 5 rows (df.head()):")
    print(df.head())
    
    # Step 2: Basic info
    print("\n2️⃣  DataFrame info (df.info()):")
    df.info()
    
    # Step 3: Statistical summary
    print("\n3️⃣  Statistical summary (df.describe()):")
    print(df.describe())
    
    # Step 4: Check unique values for categorical columns
    print("\n4️⃣  Unique values in categorical columns:")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"   {col}: {df[col].nunique()} unique values")
        print(f"      → {df[col].unique()[:5]}")


def create_problematic_example():
    """
    Create an example DataFrame with type issues for demonstration
    """
    print_section_header("EXAMPLE: DETECTING PROBLEMATIC DATA TYPES")
    
    # Create a DataFrame with intentional type issues
    problematic_data = {
        'transaction_id': ['1', '2', '3', '4', '5'],  # Should be int
        'amount': ['100.50', '200.75', '50.00', 'N/A', '300.00'],  # Should be float, has missing
        'quantity': ['10', '20', '15', '30', '25'],  # Should be int
        'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],  # Should be datetime
        'is_completed': ['True', 'False', 'True', 'True', 'False']  # Should be bool
    }
    
    df_problem = pd.DataFrame(problematic_data)
    
    print("\n⚠️  Problematic DataFrame:")
    print(df_problem)
    
    print("\n❌ Current Data Types (All wrong!):")
    print(df_problem.dtypes)
    
    print("\n🔧 Issues Identified:")
    print("   1. transaction_id: Stored as string, should be integer")
    print("   2. amount: Stored as string, should be float (has 'N/A')")
    print("   3. quantity: Stored as string, should be integer")
    print("   4. date: Stored as string, should be datetime")
    print("   5. is_completed: Stored as string, should be boolean")
    
    print("\n✅ After Proper Conversion:")
    df_fixed = df_problem.copy()
    df_fixed['transaction_id'] = df_fixed['transaction_id'].astype(int)
    df_fixed['amount'] = pd.to_numeric(df_fixed['amount'], errors='coerce')
    df_fixed['quantity'] = df_fixed['quantity'].astype(int)
    df_fixed['date'] = pd.to_datetime(df_fixed['date'])
    df_fixed['is_completed'] = df_fixed['is_completed'].map({'True': True, 'False': False})
    
    print(df_fixed.dtypes)
    print("\n✓  Now calculations work properly!")
    print(f"   Total amount: ${df_fixed['amount'].sum():.2f}")
    print(f"   Average quantity: {df_fixed['quantity'].mean():.1f}")


def main():
    """Main execution function"""
    
    print("\n" + "🎯" * 30)
    print("   DATA SHAPES AND COLUMN DATA TYPES MILESTONE")
    print("🎯" * 30)
    
    # Check if data file exists
    if not DATA_PATH.exists():
        print(f"\n❌ Error: Data file not found at {DATA_PATH}")
        print("Please ensure sample_transactions.csv exists in data/raw/")
        return
    
    # Load the data
    print(f"\n📂 Loading data from: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    print("✓ Data loaded successfully!")
    
    # Run all inspection functions
    inspect_dataframe_shape(df)
    understand_rows_columns(df)
    inspect_column_data_types(df)
    why_types_matter(df)
    detect_type_issues(df)
    demonstrate_proper_inspection_workflow(df)
    
    # Show problematic example
    create_problematic_example()
    
    # Final summary
    print_section_header("KEY TAKEAWAYS")
    print("\n✅ Always check shape after loading data")
    print("✅ Never assume column data types")
    print("✅ Shape and types guide all next steps")
    print("✅ This step prevents downstream errors")
    
    print("\n💡 Best Practices:")
    print("   1. Use df.shape to understand dataset size")
    print("   2. Use df.dtypes to check column types")
    print("   3. Use df.info() for a quick overview")
    print("   4. Use df.describe() for numerical summaries")
    print("   5. Always inspect data before processing")
    
    print("\n" + "=" * 60)
    print("  ✓ Milestone Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
