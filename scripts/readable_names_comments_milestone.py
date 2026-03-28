"""
Understanding NumPy Broadcasting with Simple Examples
=====================================================

This milestone demonstrates:
- What broadcasting is and why it exists
- Core broadcasting rules (practical, simple form)
- Scalar-to-array and array-to-array broadcasting
- How to predict output shapes
- How to spot and debug common shape mismatch issues

Run:
    python scripts/readable_names_comments_milestone.py
"""

import numpy as np


def print_array_info(name, array):
    """Print array values and shape in a consistent format."""
    print(f"{name} = {array}")
    print(f"{name}.shape = {array.shape}")


def section_1_scalar_broadcasting():
    """Broadcasting a scalar across every element of an array."""
    print("=" * 72)
    print("1) BROADCASTING WITH SCALARS")
    print("=" * 72)

    monthly_expenses = np.array([1000, 1200, 900, 1100])
    adjustment = 100

    print_array_info("monthly_expenses", monthly_expenses)
    print(f"adjustment (scalar) = {adjustment}")

    updated_expenses = monthly_expenses + adjustment
    print_array_info("updated_expenses", updated_expenses)

    print("Why this works: the scalar is logically stretched to every position.")
    print("Conceptual loop equivalent: for each value -> value + 100")


def section_2_1d_broadcasting():
    """Broadcasting between 1D arrays, including compatible and incompatible cases."""
    print("\n" + "=" * 72)
    print("2) BROADCASTING BETWEEN 1D ARRAYS")
    print("=" * 72)

    base_scores = np.array([50, 60, 70])
    bonus_scores = np.array([5, 10, 15])

    print_array_info("base_scores", base_scores)
    print_array_info("bonus_scores", bonus_scores)

    total_scores = base_scores + bonus_scores
    print_array_info("total_scores", total_scores)
    print("Why this works: same shape (3,) aligns directly.")

    print("\nTrying an incompatible example:")
    short_array = np.array([1, 2, 3])
    long_array = np.array([10, 20, 30, 40])
    print_array_info("short_array", short_array)
    print_array_info("long_array", long_array)

    try:
        _ = short_array + long_array
    except ValueError as error:
        print(f"Broadcasting error: {error}")
        print("Reason: shapes (3,) and (4,) are not compatible.")


def section_3_2d_1d_broadcasting():
    """Broadcasting a 1D array across rows/columns of a 2D array."""
    print("\n" + "=" * 72)
    print("3) BROADCASTING BETWEEN 2D AND 1D ARRAYS")
    print("=" * 72)

    sales_matrix = np.array(
        [
            [100, 200, 300],
            [150, 250, 350],
            [200, 300, 400],
        ]
    )
    regional_adjustment = np.array([10, 20, 30])

    print_array_info("sales_matrix", sales_matrix)
    print_array_info("regional_adjustment", regional_adjustment)

    adjusted_sales = sales_matrix + regional_adjustment
    print_array_info("adjusted_sales", adjusted_sales)
    print("Behavior: 1D array shape (3,) aligns with last dimension (columns).")

    print("\nColumn-wise example using explicit shape (3, 1):")
    row_adjustment = np.array([0, 50, 100]).reshape(3, 1)
    print_array_info("row_adjustment", row_adjustment)

    row_adjusted_sales = sales_matrix + row_adjustment
    print_array_info("row_adjusted_sales", row_adjusted_sales)
    print("Behavior: shape (3, 1) expands across columns for each row.")


def section_4_rules_concept():
    """Conceptual broadcasting rules with small shape checks."""
    print("\n" + "=" * 72)
    print("4) UNDERSTANDING BROADCASTING RULES (CONCEPTUAL)")
    print("=" * 72)

    print("Rule 1: Compare shapes from the rightmost dimension.")
    print("Rule 2: Dimensions are compatible if equal OR one of them is 1.")
    print("Rule 3: Missing leading dimensions are treated like size 1.")
    print("Rule 4: If any compared dimensions are incompatible, operation fails.")

    shape_a = (3, 1)
    shape_b = (1, 4)
    sample_a = np.ones(shape_a)
    sample_b = np.arange(4).reshape(shape_b)
    result = sample_a + sample_b

    print(f"\nExample shapes: {shape_a} + {shape_b} -> {result.shape}")
    print("Why: (3,1) and (1,4) expand to (3,4).")


def main():
    """Run the NumPy broadcasting milestone examples."""
    print("NUMPY BROADCASTING MILESTONE")
    print("Think of broadcasting as logical stretching, not physical copying.\n")

    section_1_scalar_broadcasting()
    section_2_1d_broadcasting()
    section_3_2d_1d_broadcasting()
    section_4_rules_concept()

    print("\n" + "=" * 72)
    print("KEY TAKEAWAYS")
    print("=" * 72)
    print("✓ Scalars broadcast to every element in an array")
    print("✓ Arrays are compared from the rightmost dimensions")
    print("✓ A dimension size of 1 can expand to match another size")
    print("✓ Incompatible dimensions produce a clear ValueError")
    print("✓ Broadcasting helps write loop-free, concise NumPy code")


if __name__ == "__main__":
    main()
