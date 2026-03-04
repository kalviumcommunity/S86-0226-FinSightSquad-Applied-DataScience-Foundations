"""
NumPy Math Operations - Milestone
==================================
This script demonstrates basic mathematical operations on NumPy arrays.
NumPy allows you to apply operations to entire arrays at once, making
numerical computation faster, cleaner, and more expressive than loops.

Topics Covered:
    1. Element-wise array operations (add, subtract, multiply, divide)
    2. Scalar operations on arrays
    3. Comparing NumPy arrays vs Python lists
    4. Avoiding common mistakes (shape mismatches, type errors)
"""

import numpy as np

print("=" * 60)
print("NUMPY MATH OPERATIONS - MILESTONE")
print("=" * 60)
print()

# =============================================================================
# 1. ELEMENT-WISE ARRAY OPERATIONS
# =============================================================================
print("1. ELEMENT-WISE ARRAY OPERATIONS")
print("-" * 60)

# Create two arrays of the same shape
income  = np.array([3000, 4500, 5200, 4100, 6000])
expenses = np.array([1200, 1800, 2100, 1600, 2400])

print(f"Income  array : {income}")
print(f"Expenses array: {expenses}")
print()

# 1.1 Addition — total monthly cash flow check
addition_result = income + expenses
print(f"1.1 Addition  (income + expenses) : {addition_result}")

# 1.2 Subtraction — net savings per month
subtraction_result = income - expenses
print(f"1.2 Subtraction (income - expenses): {subtraction_result}")

# 1.3 Multiplication — e.g., doubling projected income
multiplication_result = income * expenses
print(f"1.3 Multiplication (income * expenses): {multiplication_result}")

# 1.4 Division — expense-to-income ratio per month
division_result = expenses / income
print(f"1.4 Division (expenses / income)   : {np.round(division_result, 4)}")

print()
print("Key insight: Each operation is applied to CORRESPONDING elements.")
print("Position 0 of income pairs with position 0 of expenses, and so on.")
print()

# =============================================================================
# 2. SCALAR OPERATIONS ON ARRAYS
# =============================================================================
print("\n2. SCALAR OPERATIONS ON ARRAYS")
print("-" * 60)

prices = np.array([100, 200, 150, 300, 250])
print(f"Original prices array: {prices}")
print()

# 2.1 Add a scalar — apply a flat fee of 50 to every price
scalar_add = prices + 50
print(f"2.1 Add scalar 50 to every price   : {scalar_add}")

# 2.2 Subtract a scalar — apply a discount of 20
scalar_subtract = prices - 20
print(f"2.2 Subtract scalar 20 from prices : {scalar_subtract}")

# 2.3 Multiply by a scalar — apply 10% tax factor (multiply by 1.10)
scalar_multiply = prices * 1.10
print(f"2.3 Multiply prices by 1.10 (10% tax): {scalar_multiply}")

# 2.4 Divide by a scalar — convert prices from cents to dollars
prices_cents = np.array([10000, 20000, 15000, 30000, 25000])
scalar_divide = prices_cents / 100
print(f"2.4 Divide cents array by 100 (→ dollars): {scalar_divide}")

print()
print("Key insight: The scalar is broadcast to every element automatically.")
print("No loops needed — NumPy handles it internally and efficiently.")
print()

# =============================================================================
# 3. COMPARING NUMPY ARRAYS AND PYTHON LISTS
# =============================================================================
print("\n3. COMPARING NUMPY ARRAYS AND PYTHON LISTS")
print("-" * 60)

list_a = [10, 20, 30]
list_b = [1, 2, 3]

array_a = np.array(list_a)
array_b = np.array(list_b)

# 3.1 Python list addition — concatenates, does NOT add element-wise
list_addition = list_a + list_b
print(f"Python list addition  [10,20,30] + [1,2,3] = {list_addition}")
print("  → Lists are JOINED (concatenated), not added mathematically.")
print()

# 3.2 NumPy array addition — adds element-wise
array_addition = array_a + array_b
print(f"NumPy array addition  [10,20,30] + [1,2,3] = {array_addition}")
print("  → Arrays are added ELEMENT-WISE: 10+1=11, 20+2=22, 30+3=33")
print()

# 3.3 Python list multiplication — repeats the list
list_multiply = list_a * 3
print(f"Python list multiply  [10,20,30] * 3 = {list_multiply}")
print("  → List is REPEATED 3 times, not multiplied element-wise.")
print()

# 3.4 NumPy scalar multiply — applies to each element
array_multiply = array_a * 3
print(f"NumPy array multiply  [10,20,30] * 3 = {array_multiply}")
print("  → Each element is MULTIPLIED by 3: 10*3=30, 20*3=60, 30*3=90")
print()

print("Summary: NumPy is preferred for math because it treats arrays as")
print("mathematical vectors, not as Python containers.")
print()

# =============================================================================
# 4. AVOIDING COMMON MISTAKES
# =============================================================================
print("\n4. AVOIDING COMMON MISTAKES")
print("-" * 60)

# 4.1 Compatible shapes — must match for element-wise operations
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(f"4.1 Compatible shapes: {a.shape} and {b.shape}")
print(f"    Result of a + b : {a + b}  ✓ Works correctly")
print()

# 4.2 Incompatible shapes — this demonstrates the error (caught safely)
c = np.array([1, 2, 3])
d = np.array([10, 20])
print(f"4.2 Incompatible shapes: {c.shape} and {d.shape}")
try:
    result = c + d
except ValueError as e:
    print(f"    ValueError raised → {e}")
    print("    ✗ Fix: Ensure both arrays have the same shape before operating.")
print()

# 4.3 Integer vs float division
int_array = np.array([10, 20, 30], dtype=int)
divisor   = 3
result_div = int_array / divisor
print(f"4.3 Integer array {int_array} divided by {divisor}:")
print(f"    Result dtype  : {result_div.dtype}  (NumPy auto-promotes to float)")
print(f"    Result values : {result_div}")
print("    → NumPy handles type promotion automatically — no data loss.")
print()

# 4.4 Using loops vs NumPy (performance reminder)
values = np.array([5, 10, 15, 20, 25])

# BAD practice — using a loop for simple array math
loop_result = []
for v in values:
    loop_result.append(v * 2)
print(f"4.4 Loop approach  (avoid this): {loop_result}")

# GOOD practice — vectorized operation
vectorized_result = values * 2
print(f"    NumPy approach (preferred) : {vectorized_result}")
print("    → Vectorized code is shorter, faster, and easier to read.")
print()

# =============================================================================
# 5. QUICK SUMMARY OF ALL OPERATIONS
# =============================================================================
print("\n5. SUMMARY - ALL BASIC MATH OPERATIONS AT A GLANCE")
print("-" * 60)

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 2, 3, 4,  5])

print(f"x = {x}")
print(f"y = {y}")
print()
print(f"x + y  = {x + y}    (element-wise addition)")
print(f"x - y  = {x - y}    (element-wise subtraction)")
print(f"x * y  = {x * y}   (element-wise multiplication)")
print(f"x / y  = {x / y}  (element-wise division)")
print(f"x ** 2 = {x ** 2}    (element-wise power)")
print(f"x + 10 = {x + 10}  (scalar addition)")
print(f"x * 2  = {x * 2}  (scalar multiplication)")
print()

print("=" * 60)
print("MILESTONE COMPLETE: NumPy Math Operations")
print("=" * 60)
print("You can now:")
print("  ✓ Perform element-wise arithmetic on NumPy arrays")
print("  ✓ Apply scalar operations across entire arrays")
print("  ✓ Explain the difference between list math and array math")
print("  ✓ Identify and avoid shape-mismatch errors")
print("  ✓ Write concise, loop-free numerical code using NumPy")
