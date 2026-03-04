"""
Understanding Array Shape, Dimensions, and Index Positions - Milestone
======================================================================

This milestone focuses on NumPy fundamentals:
- Understanding array shape
- Understanding dimensions (ndim)
- Accessing values using index positions
- Visualizing row/column layout
- Avoiding common index mistakes

Run:
    python scripts/array_shape_dimensions_index_positions_milestone.py
"""

import numpy as np


def section_header(title):
    """Print a consistent section header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def show_shape_examples():
    """Demonstrate what shape means for 1D, 2D, and 3D arrays."""
    section_header("1. UNDERSTANDING ARRAY SHAPE")

    one_dimensional = np.array([10, 20, 30, 40, 50])
    two_dimensional = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    three_dimensional = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])

    print(f"1D array: {one_dimensional}")
    print(f"1D shape: {one_dimensional.shape} -> (number_of_elements,)")

    print("\n2D array:")
    print(two_dimensional)
    print(f"2D shape: {two_dimensional.shape} -> (rows, columns)")

    print("\n3D array:")
    print(three_dimensional)
    print(f"3D shape: {three_dimensional.shape} -> (layers, rows, columns)")


def show_dimension_examples():
    """Demonstrate ndim and basic axis meaning."""
    section_header("2. UNDERSTANDING DIMENSIONS (ndim)")

    one_dimensional = np.array([100, 200, 300])
    two_dimensional = np.array([
        [11, 12, 13],
        [21, 22, 23],
    ])
    three_dimensional = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ])

    print(f"1D ndim: {one_dimensional.ndim}")
    print(f"2D ndim: {two_dimensional.ndim}")
    print(f"3D ndim: {three_dimensional.ndim}")

    print("\nBasic axis meaning for 2D arrays:")
    print("- axis 0: moves down rows")
    print("- axis 1: moves across columns")
    print(f"2D shape example: {two_dimensional.shape} -> 2 rows, 3 columns")


def show_indexing_examples():
    """Demonstrate index access for 1D and 2D arrays."""
    section_header("3. ACCESSING ELEMENTS USING INDEX POSITIONS")

    monthly_savings = np.array([400, 520, 610, 480, 700])
    print(f"1D array (monthly_savings): {monthly_savings}")
    print(f"Index 0: {monthly_savings[0]}")
    print(f"Index 2: {monthly_savings[2]}")
    print(f"Last element index 4: {monthly_savings[4]}")

    student_scores = np.array([
        [85, 90, 88],
        [78, 82, 80],
        [92, 95, 94],
    ])

    print("\n2D array (student_scores):")
    print(student_scores)
    print(f"Shape: {student_scores.shape} -> 3 rows, 3 columns")
    print("Use array[row_index, column_index] for 2D indexing")
    print(f"student_scores[0, 0]: {student_scores[0, 0]}")
    print(f"student_scores[1, 2]: {student_scores[1, 2]}")
    print(f"student_scores[2, 1]: {student_scores[2, 1]}")


def show_layout_visualization():
    """Map grid positions to values to build indexing intuition."""
    section_header("4. VISUALIZING ARRAY LAYOUT")

    grid = np.array([
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33],
    ])

    print("Grid:")
    print(grid)
    print("\nIndex map (row, column) -> value:")
    for row_index in range(grid.shape[0]):
        for column_index in range(grid.shape[1]):
            value = grid[row_index, column_index]
            print(f"({row_index}, {column_index}) -> {value}")


def show_safe_indexing_practices():
    """Show common mistakes and how to avoid index errors."""
    section_header("5. AVOIDING COMMON INDEXING MISTAKES")

    values = np.array([5, 10, 15])
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
    ])

    print(f"1D values: {values} (shape: {values.shape})")
    print(f"2D matrix:\n{matrix} (shape: {matrix.shape})")

    one_d_index = 3
    if 0 <= one_d_index < values.shape[0]:
        print(f"Safe 1D access values[{one_d_index}] = {values[one_d_index]}")
    else:
        print(
            f"Unsafe 1D index {one_d_index}: valid range is 0 to {values.shape[0] - 1}"
        )

    row_index = 1
    column_index = 3
    row_in_range = 0 <= row_index < matrix.shape[0]
    column_in_range = 0 <= column_index < matrix.shape[1]

    if row_in_range and column_in_range:
        print(f"Safe 2D access matrix[{row_index}, {column_index}] = {matrix[row_index, column_index]}")
    else:
        print(
            "Unsafe 2D index "
            f"({row_index}, {column_index}): valid row range is 0 to {matrix.shape[0] - 1}, "
            f"valid column range is 0 to {matrix.shape[1] - 1}"
        )


def main():
    """Run the complete milestone walkthrough."""
    print("=" * 70)
    print("UNDERSTANDING ARRAY SHAPE, DIMENSIONS, AND INDEX POSITIONS")
    print("=" * 70)

    show_shape_examples()
    show_dimension_examples()
    show_indexing_examples()
    show_layout_visualization()
    show_safe_indexing_practices()

    section_header("MILESTONE SUMMARY")
    print("What you practiced:")
    print("1. Interpreting shape for 1D, 2D, and 3D arrays")
    print("2. Understanding dimensions using ndim")
    print("3. Accessing elements by correct index positions")
    print("4. Mapping row/column positions to real values")
    print("5. Preventing index errors with bounds awareness")
    print("\nYou are now ready for slicing and reshaping in later milestones.")


if __name__ == "__main__":
    main()
