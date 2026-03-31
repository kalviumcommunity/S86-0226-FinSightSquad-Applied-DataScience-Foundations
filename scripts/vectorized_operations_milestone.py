"""
Vectorized Operations Milestone
================================
This milestone demonstrates applying vectorized operations instead of Python loops
when working with NumPy arrays.

Learning Objectives:
- Understand what vectorized operations are
- Replace simple Python loops with array operations
- Write concise and efficient numerical code
- Improve performance and readability
"""

import numpy as np
import time


print("=" * 70)
print("VECTORIZED OPERATIONS MILESTONE")
print("=" * 70)
print()


# ============================================================================
# 1. Understanding Loop-Based vs Vectorized Code
# ============================================================================
print("1. LOOP-BASED VS VECTORIZED CODE")
print("-" * 70)

# Create a sample array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Original array: {arr}")
print()

# Loop-based approach: Square each element
print("A. Loop-Based Approach (Traditional Python):")
result_loop = np.zeros(len(arr))
for i in range(len(arr)):
    result_loop[i] = arr[i] ** 2
print(f"   Code: Uses a for loop to iterate through each element")
print(f"   Result: {result_loop}")
print()

# Vectorized approach: Operation on entire array
print("B. Vectorized Approach (NumPy Style):")
result_vectorized = arr ** 2
print(f"   Code: Single expression, no loop needed")
print(f"   Result: {result_vectorized}")
print()

print("Observations:")
print("- Vectorized code is shorter and more readable")
print("- No need for explicit indexing or loop counters")
print("- NumPy handles the iteration internally")
print("- Both produce the same result")
print()


# ============================================================================
# 2. Applying Vectorized Arithmetic Operations
# ============================================================================
print("\n2. VECTORIZED ARITHMETIC OPERATIONS")
print("-" * 70)

# Create sample arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print()

# Element-wise addition
result_add = arr1 + arr2
print(f"Addition (arr1 + arr2): {result_add}")

# Element-wise subtraction
result_sub = arr1 - arr2
print(f"Subtraction (arr1 - arr2): {result_sub}")

# Element-wise multiplication
result_mul = arr1 * arr2
print(f"Multiplication (arr1 * arr2): {result_mul}")

# Element-wise division
result_div = arr1 / arr2
print(f"Division (arr1 / arr2): {result_div}")

# Scalar operations
scalar = 10
result_scalar = arr1 + scalar
print(f"\nScalar addition (arr1 + {scalar}): {result_scalar}")

# Complex expressions
result_complex = (arr1 * 2 + arr2) / 3
print(f"Complex expression ((arr1 * 2 + arr2) / 3): {result_complex}")
print()

# Performance comparison
print("Performance Comparison:")
large_arr = np.arange(1000000)

# Timing loop-based approach
start_time = time.time()
loop_result = np.zeros(len(large_arr))
for i in range(len(large_arr)):
    loop_result[i] = large_arr[i] * 2 + 5
loop_time = time.time() - start_time

# Timing vectorized approach
start_time = time.time()
vectorized_result = large_arr * 2 + 5
vectorized_time = time.time() - start_time

print(f"Loop-based approach time: {loop_time:.6f} seconds")
print(f"Vectorized approach time: {vectorized_time:.6f} seconds")
print(f"Speedup: {loop_time / vectorized_time:.2f}x faster")
print()


# ============================================================================
# 3. Using Vectorized Comparisons and Conditions
# ============================================================================
print("\n3. VECTORIZED COMPARISONS AND CONDITIONS")
print("-" * 70)

# Create sample data
temperatures = np.array([18, 22, 25, 30, 35, 28, 20, 15, 32, 27])
print(f"Temperature data (°C): {temperatures}")
print()

# Vectorized comparisons
hot_days = temperatures > 30
print(f"Days above 30°C (temperatures > 30): {hot_days}")
print(f"Boolean array showing True for hot days")
print()

cold_days = temperatures < 20
print(f"Days below 20°C (temperatures < 20): {cold_days}")
print()

comfortable_days = (temperatures >= 20) & (temperatures <= 28)
print(f"Comfortable days (20-28°C): {comfortable_days}")
print(f"Using compound conditions with & operator")
print()

# Count using boolean arrays
num_hot_days = np.sum(hot_days)
num_cold_days = np.sum(cold_days)
num_comfortable = np.sum(comfortable_days)

print(f"Count of hot days: {num_hot_days}")
print(f"Count of cold days: {num_cold_days}")
print(f"Count of comfortable days: {num_comfortable}")
print()

# Filtering with boolean indexing
hot_temperatures = temperatures[hot_days]
print(f"Actual hot day temperatures: {hot_temperatures}")
print()

# Comparison example: Loop vs Vectorized
scores = np.array([45, 67, 89, 34, 78, 92, 56, 88])
print(f"Student scores: {scores}")

# Loop-based counting (not recommended)
print("\nLoop-based approach to count passing grades (>= 50):")
count_loop = 0
for score in scores:
    if score >= 50:
        count_loop += 1
print(f"   Result: {count_loop} students passed")

# Vectorized approach (recommended)
print("\nVectorized approach:")
passing = scores >= 50
count_vectorized = np.sum(passing)
print(f"   Result: {count_vectorized} students passed")
print(f"   Boolean array: {passing}")
print()


# ============================================================================
# 4. Avoiding Common Vectorization Mistakes
# ============================================================================
print("\n4. AVOIDING COMMON VECTORIZATION MISTAKES")
print("-" * 70)

print("A. Shape Compatibility:")
arr_a = np.array([1, 2, 3])
arr_b = np.array([10, 20, 30])
arr_c = np.array([1, 2])

print(f"   arr_a: {arr_a} (shape: {arr_a.shape})")
print(f"   arr_b: {arr_b} (shape: {arr_b.shape})")
print(f"   arr_c: {arr_c} (shape: {arr_c.shape})")
print()

# Compatible shapes - works fine
result = arr_a + arr_b
print(f"   arr_a + arr_b (compatible shapes): {result} ✓")

# Incompatible shapes - would cause error
print(f"   arr_a + arr_c (incompatible shapes): Would cause ValueError ✗")
print(f"   Shapes must match for element-wise operations")
print()

print("B. When NOT to Vectorize:")
print("   1. Complex conditional logic with state dependencies")
print("   2. Operations that require results from previous iterations")
print("   3. File I/O operations inside loops")
print("   4. When readability would suffer significantly")
print()

print("C. Good Vectorization Practices:")
numbers = np.array([1, 2, 3, 4, 5])

# Good: Clear and readable
result_good = numbers * 2 + 10
print(f"   Good: result = numbers * 2 + 10")
print(f"   Result: {result_good}")
print()

# Avoid: Overly complex one-liners
# result_bad = ((numbers ** 2 + numbers * 3) / (numbers + 1)) ** 0.5 + ...
print("   Bad: Extremely complex one-liner that sacrifices readability")
print("   Better: Break into intermediate steps with descriptive names")
print()

print("D. Memory Efficiency:")
# Create views, not copies when possible
original = np.arange(10)
view = original[::2]  # This is a view
copy = original[::2].copy()  # This is a copy

print(f"   Original array: {original}")
print(f"   View (every 2nd element): {view}")
print(f"   Views are memory-efficient, copies use more memory")
print()


# ============================================================================
# 5. Practical Examples: Putting It All Together
# ============================================================================
print("\n5. PRACTICAL EXAMPLES")
print("-" * 70)

# Example 1: Calculate average score with bonus
print("Example 1: Student Grades with Bonus")
base_scores = np.array([75, 82, 68, 91, 55, 88, 77, 93])
attendance_bonus = np.array([5, 5, 3, 5, 2, 5, 4, 5])

final_scores = base_scores + attendance_bonus
# Cap at 100
final_scores = np.minimum(final_scores, 100)

print(f"Base scores: {base_scores}")
print(f"Attendance bonus: {attendance_bonus}")
print(f"Final scores (capped at 100): {final_scores}")
print(f"Average final score: {np.mean(final_scores):.2f}")
print()

# Example 2: Temperature conversion
print("Example 2: Temperature Conversion (Celsius to Fahrenheit)")
celsius = np.array([0, 10, 20, 25, 30, 37, 100])
fahrenheit = celsius * 9/5 + 32

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print("Formula: F = C * 9/5 + 32 (applied to entire array)")
print()

# Example 3: Statistical analysis
print("Example 3: Quick Statistical Analysis")
data = np.array([45, 67, 89, 34, 78, 92, 56, 88, 71, 83])

mean = np.mean(data)
std = np.std(data)
above_average = data > mean
outliers = np.abs(data - mean) > 2 * std

print(f"Data: {data}")
print(f"Mean: {mean:.2f}")
print(f"Standard deviation: {std:.2f}")
print(f"Values above average: {data[above_average]}")
print(f"Outliers (>2 std from mean): {data[outliers]}")
print()


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY: KEY TAKEAWAYS")
print("=" * 70)
print("""
1. Vectorization applies operations to entire arrays at once
2. Eliminates the need for explicit Python loops
3. Code is shorter, clearer, and more readable
4. Performance is significantly better (often 10-100x faster)
5. Use comparison operators to create boolean arrays
6. Boolean arrays can filter data or count conditions
7. Ensure shapes are compatible for element-wise operations
8. Prioritize readability over extreme optimization
9. Vectorization is a core NumPy concept and best practice
10. Think "what to do" not "how to loop"

Vectorized operations are the foundation of efficient numerical computing
in Python and are essential for Data Science work.
""")
print("=" * 70)
