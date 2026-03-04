# Understanding Array Shape, Dimensions, and Index Positions - Milestone

## Overview

This milestone focuses on understanding array shape, dimensions, and index positions in NumPy. Correctly interpreting array structure is essential for safe indexing, preventing index errors, and writing predictable numerical code.

Before slicing, reshaping, or advanced operations, you must understand how arrays are laid out.

## Learning Objectives

This lesson is to help you:

- ✓ Understand what shape and dimensions mean in NumPy
- ✓ Identify 1D, 2D, and higher-dimensional arrays
- ✓ Access elements using correct index positions
- ✓ Visualize row/column layout clearly
- ✓ Avoid common indexing mistakes

## Skills You Will Gain

By completing this milestone, you will be able to:

1. Interpret array shapes confidently
2. Understand dimensions and axes at a basic level
3. Access elements using proper indexing
4. Navigate rows and columns correctly
5. Prevent index-related bugs

## Why This Matters

Common beginner issues include:

- Index errors due to incorrect positions
- Confusion between rows and columns
- Misunderstanding array dimensions
- Incorrect assumptions about array layout

These mistakes cause bugs that are difficult to diagnose.

This milestone ensures that:

- You understand how data is organized in arrays
- You can access and manipulate values safely
- Your code behaves consistently and predictably
- You are ready for slicing and reshaping later

Think of array shape as the blueprint of your data.

---

## What You Are Expected to Do

This is a NumPy fundamentals milestone, not a data analysis task.

You are expected to:

- ✓ Inspect array shape and dimensions
- ✓ Work with 1D and 2D arrays
- ✓ Access elements using index positions
- ✓ Print results to observe behavior

**No datasets or advanced NumPy operations are required.**

---

## Milestone Components

### 1. Understanding Array Shape

Learn what shape represents.

You should:

- Inspect the shape of arrays
- Understand what each number in shape means
- Identify rows and columns in 2D arrays
- Recognize how shape changes with dimensions

Shape defines how data is organized.

### 2. Understanding Dimensions (ndim)

Learn how dimensions work.

You should:

- Identify number of dimensions in an array
- Distinguish between 1D and 2D arrays
- Understand axes at a basic level
- Relate dimensions to shape

Dimensions describe data complexity.

### 3. Accessing Elements Using Index Positions

Learn correct indexing.

You should:

- Access elements in 1D arrays
- Access elements in 2D arrays using row and column indices
- Use zero-based indexing correctly
- Avoid out-of-range index access

Correct indexing prevents runtime errors.

### 4. Visualizing Array Layout

Build a clear mental model.

You should:

- Visualize arrays as grids/tables
- Map index positions to values
- Understand row and column ordering
- Use simple examples for clarity

Visualization improves intuition.

### 5. Avoiding Indexing Mistakes

Practice safe indexing.

You should:

- Check valid index ranges when needed
- Read shape before selecting positions
- Separate row and column logic in 2D arrays
- Confirm assumptions with printed output

This helps prevent hidden bugs.

---

## Running the Script

To complete this milestone:

1. **Navigate to the scripts directory:**

   ```bash
   cd scripts
   ```

2. **Run the Python script:**

   ```bash
   python array_shape_dimensions_index_positions_milestone.py
   ```

3. **Observe the output carefully**
   - Shape and dimensions of each array
   - Correct index access examples
   - Index-to-value layout mapping
   - Safe handling of invalid positions

## Expected Output

The script demonstrates:

1. Shape for 1D, 2D, and 3D arrays
2. `ndim` and basic axis meaning
3. 1D and 2D indexing using positions
4. Grid layout visualization with index mapping
5. Index safety checks that prevent out-of-range errors

## Key Concepts Covered

### Shape and Dimensions

```python
import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(vector.shape)  # (3,)
print(matrix.shape)  # (2, 3)
print(vector.ndim)   # 1
print(matrix.ndim)   # 2
```

### Index Positions

```python
print(vector[0])      # first element
print(vector[2])      # third element

print(matrix[0, 1])   # row 0, column 1
print(matrix[1, 2])   # row 1, column 2
```

### Safe Indexing Mindset

```python
row = 1
column = 2

if 0 <= row < matrix.shape[0] and 0 <= column < matrix.shape[1]:
    print(matrix[row, column])
else:
    print("Index out of range")
```

---

## Common Mistakes to Avoid

1. **Mixing row and column positions**
   - In 2D arrays, always use `array[row, column]`

2. **Forgetting zero-based indexing**
   - First element/index starts at `0`, not `1`

3. **Accessing out-of-range positions**
   - Check shape before indexing

4. **Assuming 1D and 2D indexing are identical**
   - 1D uses one index, 2D uses two indices

---

## Next Steps

After completing this milestone:

1. Practice indexing with your own small arrays
2. Try reading full rows and columns
3. Move on to slicing and reshaping with confidence
