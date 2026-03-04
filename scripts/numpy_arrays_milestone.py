"""
NumPy Arrays from Python Lists - Milestone
===========================================
This script demonstrates creating and working with NumPy arrays from Python lists.
NumPy arrays are the foundation of numerical computing in Data Science.
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAYS FROM PYTHON LISTS - MILESTONE")
print("=" * 60)
print()

# =============================================================================
# 1. UNDERSTANDING NUMPY ARRAYS
# =============================================================================
print("1. UNDERSTANDING NUMPY ARRAYS")
print("-" * 60)

# What makes NumPy arrays different from Python lists?
# - Homogeneous: all elements have the same data type
# - Fixed size: size is set at creation
# - Efficient: optimized for numerical operations
# - Element-wise operations: math works on all elements at once

# Example Python list for comparison
python_list = [1, 2, 3, 4, 5]
print(f"Python list: {python_list}")
print(f"List type: {type(python_list)}")
print()

# =============================================================================
# 2. CREATING NUMPY ARRAYS FROM LISTS
# =============================================================================
print("\n2. CREATING NUMPY ARRAYS FROM LISTS")
print("-" * 60)

# 2.1 Creating a one-dimensional (1D) array
numbers_list = [10, 20, 30, 40, 50]
numbers_array = np.array(numbers_list)

print("2.1 One-Dimensional Array:")
print(f"Original list: {numbers_list}")
print(f"NumPy array: {numbers_array}")
print(f"Array type: {type(numbers_array)}")
print()

# 2.2 Creating another 1D array with different values
expenses = [250, 400, 150, 600, 320]
expenses_array = np.array(expenses)

print("2.2 Another 1D Array (Expenses):")
print(f"Expenses list: {expenses}")
print(f"Expenses array: {expenses_array}")
print()

# 2.3 Creating a two-dimensional (2D) array from nested lists
# Each inner list becomes a row
monthly_expenses = [
    [250, 400, 150],  # January
    [300, 420, 180],  # February
    [280, 390, 170]   # March
]
monthly_array = np.array(monthly_expenses)

print("2.3 Two-Dimensional Array (Monthly Expenses):")
print(f"Nested list: {monthly_expenses}")
print(f"2D NumPy array:\n{monthly_array}")
print()

# 2.4 Creating arrays with different numeric types
integers = np.array([1, 2, 3, 4, 5])
floats = np.array([1.5, 2.7, 3.2, 4.8, 5.1])
mixed = np.array([1, 2.5, 3, 4.7, 5])  # All converted to float

print("2.4 Arrays with Different Numeric Types:")
print(f"Integer array: {integers}")
print(f"Float array: {floats}")
print(f"Mixed array (auto-converted): {mixed}")
print()

# =============================================================================
# 3. INSPECTING ARRAY PROPERTIES
# =============================================================================
print("\n3. INSPECTING ARRAY PROPERTIES")
print("-" * 60)

# 3.1 Array shape (dimensions)
print("3.1 Array Shape:")
print(f"1D array shape: {numbers_array.shape}")
print(f"2D array shape: {monthly_array.shape}")
print(f"Shape explanation: {monthly_array.shape[0]} rows, {monthly_array.shape[1]} columns")
print()

# 3.2 Array data type (dtype)
print("3.2 Array Data Type:")
print(f"Integer array dtype: {integers.dtype}")
print(f"Float array dtype: {floats.dtype}")
print(f"Mixed array dtype: {mixed.dtype}")
print()

# 3.3 Array dimensions (ndim)
print("3.3 Array Dimensions:")
print(f"1D array dimensions: {numbers_array.ndim}")
print(f"2D array dimensions: {monthly_array.ndim}")
print()

# 3.4 Array size (total number of elements)
print("3.4 Array Size:")
print(f"1D array size: {numbers_array.size}")
print(f"2D array size: {monthly_array.size}")
print()

# 3.5 Creating a 3D array for demonstration
quarterly_data = [
    [[100, 120], [110, 130]],  # Quarter 1
    [[105, 125], [115, 135]]   # Quarter 2
]
quarterly_array = np.array(quarterly_data)

print("3.5 Three-Dimensional Array:")
print(f"3D array:\n{quarterly_array}")
print(f"3D array shape: {quarterly_array.shape}")
print(f"3D array dimensions: {quarterly_array.ndim}")
print()

# =============================================================================
# 4. BASIC OPERATIONS ON ARRAYS
# =============================================================================
print("\n4. BASIC OPERATIONS ON ARRAYS")
print("-" * 60)

# 4.1 Element-wise arithmetic operations
revenue = np.array([500, 600, 550, 700, 650])
costs = np.array([200, 250, 220, 280, 260])

print("4.1 Element-wise Arithmetic:")
print(f"Revenue: {revenue}")
print(f"Costs: {costs}")
print(f"Profit (Revenue - Costs): {revenue - costs}")
print(f"Total (Revenue + Costs): {revenue + costs}")
print(f"Profit Margin (Revenue / Costs): {revenue / costs}")
print()

# 4.2 Scalar operations (applied to all elements)
prices = np.array([100, 200, 150, 250, 300])

print("4.2 Scalar Operations:")
print(f"Original prices: {prices}")
print(f"Prices + 50: {prices + 50}")
print(f"Prices * 2: {prices * 2}")
print(f"Prices / 10: {prices / 10}")
print(f"Prices - 20: {prices - 20}")
print()

# 4.3 Mathematical functions
values = np.array([4, 9, 16, 25, 36])

print("4.3 Mathematical Functions:")
print(f"Values: {values}")
print(f"Square root: {np.sqrt(values)}")
print(f"Sum of all values: {np.sum(values)}")
print(f"Mean (average): {np.mean(values)}")
print(f"Maximum value: {np.max(values)}")
print(f"Minimum value: {np.min(values)}")
print()

# 4.4 Operations on 2D arrays
sales_data = np.array([
    [100, 150, 200],
    [120, 160, 210],
    [110, 140, 190]
])

print("4.4 Operations on 2D Arrays:")
print(f"Sales data:\n{sales_data}")
print(f"Total sales (sum of all): {np.sum(sales_data)}")
print(f"Average sales: {np.mean(sales_data)}")
print(f"Sum by rows: {np.sum(sales_data, axis=1)}")
print(f"Sum by columns: {np.sum(sales_data, axis=0)}")
print()

# =============================================================================
# 5. ARRAYS VS LISTS - KEY DIFFERENCES
# =============================================================================
print("\n5. ARRAYS VS LISTS - KEY DIFFERENCES")
print("-" * 60)

# 5.1 Performance comparison (conceptual)
list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]

array_a = np.array(list_a)
array_b = np.array(list_b)

print("5.1 Element-wise Operations:")
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"List A + List B (concatenation): {list_a + list_b}")
print()

print(f"Array A: {array_a}")
print(f"Array B: {array_b}")
print(f"Array A + Array B (element-wise): {array_a + array_b}")
print(f"Array A * 2 (element-wise): {array_a * 2}")
print()

# 5.2 Type consistency
mixed_list = [1, 2, "three", 4.5]  # Lists can have mixed types
uniform_array = np.array([1, 2, 3, 4.5])  # Arrays convert to common type

print("5.2 Type Consistency:")
print(f"Mixed list: {mixed_list}")
print(f"List types: {[type(x) for x in mixed_list]}")
print()
print(f"Uniform array: {uniform_array}")
print(f"Array dtype: {uniform_array.dtype}")
print("(All elements converted to float)")
print()

# 5.3 Memory efficiency
print("5.3 Memory and Performance:")
print("✓ Arrays use less memory for numeric data")
print("✓ Arrays are faster for mathematical operations")
print("✓ Arrays enable vectorized operations (no loops needed)")
print("✓ Arrays are required by most data science libraries")
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("MILESTONE SUMMARY")
print("=" * 60)
print("""
What we learned:
1. NumPy arrays are homogeneous, efficient data structures
2. Create arrays using np.array() from Python lists
3. Arrays can be 1D, 2D, 3D, or higher dimensions
4. Key properties: shape, dtype, ndim, size
5. Element-wise operations work automatically on arrays
6. Arrays are much faster than lists for numerical work

Key takeaways:
✓ Use NumPy arrays for all numerical computations
✓ Arrays are the foundation of Pandas, ML, and data analysis
✓ Element-wise operations make code cleaner and faster
✓ Understanding shape and dtype prevents common errors

You are now ready to work with NumPy arrays in real data science tasks!
""")
print("=" * 60)
