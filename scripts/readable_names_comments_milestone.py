"""
Writing Readable Variable Names and Comments (PEP 8 Basics)
============================================================

This milestone demonstrates:
- Writing clear, descriptive variable names
- Following basic PEP 8 naming conventions (snake_case)
- Adding comments that explain intent (the "why")
- Avoiding over-commenting and misleading comments
- Improving overall code readability for team collaboration

Run:
    python scripts/readable_names_comments_milestone.py
"""


# ============================================================================
# SECTION 1: Good vs Poor Variable Names
# ============================================================================

def poor_variable_names_example():
    """Example showing vague names that make code harder to read."""
    x = 2500
    y = 0.07
    z = x * y
    return z


def clear_variable_names_example():
    """Example showing descriptive names that communicate intent."""
    monthly_income = 2500
    savings_rate = 0.07
    monthly_savings = monthly_income * savings_rate
    return monthly_savings


# ============================================================================
# SECTION 2: Following Basic PEP 8 Naming Conventions
# ============================================================================

MAX_RECOMMENDED_HOURS_PER_WEEK = 40


def calculate_weekly_study_hours(hours_per_day, days_per_week):
    """Use snake_case naming for variables and function names."""
    weekly_study_hours = hours_per_day * days_per_week
    return weekly_study_hours


def calculate_hours_status(weekly_study_hours):
    """Use clear naming and a constant to keep rules easy to read."""
    if weekly_study_hours <= MAX_RECOMMENDED_HOURS_PER_WEEK:
        return "Balanced workload"
    return "Heavy workload"


# ============================================================================
# SECTION 3: Writing Useful Comments (Explain Why, Not What)
# ============================================================================

def build_monthly_budget(expenses_by_category):
    """
    Create a budget summary from category expenses.

    We separate essentials from non-essentials so learners can quickly see
    where fixed obligations are concentrated before planning optional spending.
    """
    essentials_total = (
        expenses_by_category["rent"]
        + expenses_by_category["utilities"]
        + expenses_by_category["food"]
    )

    non_essentials_total = (
        expenses_by_category["entertainment"]
        + expenses_by_category["subscriptions"]
    )

    total_monthly_expenses = essentials_total + non_essentials_total

    return {
        "essentials_total": essentials_total,
        "non_essentials_total": non_essentials_total,
        "total_monthly_expenses": total_monthly_expenses,
    }


# ============================================================================
# SECTION 4: Avoiding Common Readability Mistakes
# ============================================================================

def compute_score_with_unclear_style():
    """Poor readability example: vague names and noisy comments."""
    # add 10
    a = 10
    # add 5
    b = 5
    # plus
    c = a + b
    return c


def compute_total_score(base_score, bonus_points):
    """
    Better readability example with clear names.

    Bonus points are separated from base score to make grading policy explicit.
    """
    total_score = base_score + bonus_points
    return total_score


# ============================================================================
# SECTION 5: Practical Refactor Demonstration
# ============================================================================

def refactor_dataset_metrics(dataset_rows, missing_values_count):
    """
    Calculate and return basic dataset quality metrics.

    Missing-value ratio is included because it is often used as a quick quality
    signal before moving to deeper analysis.
    """
    if dataset_rows == 0:
        missing_value_ratio = 0
    else:
        missing_value_ratio = missing_values_count / dataset_rows

    quality_summary = {
        "dataset_rows": dataset_rows,
        "missing_values_count": missing_values_count,
        "missing_value_ratio": missing_value_ratio,
    }
    return quality_summary


def main():
    """Run all readability examples for the milestone walkthrough."""

    print("=" * 70)
    print("SECTION 1: Good vs Poor Variable Names")
    print("=" * 70)
    poor_result = poor_variable_names_example()
    clear_result = clear_variable_names_example()
    print(f"Poor naming result (works, hard to read): {poor_result}")
    print(f"Clear naming result (same logic, easier to read): {clear_result}")

    print("\n" + "=" * 70)
    print("SECTION 2: PEP 8 Naming Conventions")
    print("=" * 70)
    weekly_study_hours = calculate_weekly_study_hours(hours_per_day=3, days_per_week=6)
    workload_status = calculate_hours_status(weekly_study_hours)
    print(f"Weekly study hours: {weekly_study_hours}")
    print(f"Status: {workload_status}")

    print("\n" + "=" * 70)
    print("SECTION 3: Useful Comments")
    print("=" * 70)
    expense_data = {
        "rent": 900,
        "utilities": 120,
        "food": 300,
        "entertainment": 100,
        "subscriptions": 50,
    }
    budget_summary = build_monthly_budget(expense_data)
    print(f"Budget summary: {budget_summary}")

    print("\n" + "=" * 70)
    print("SECTION 4: Avoiding Readability Mistakes")
    print("=" * 70)
    unclear_score = compute_score_with_unclear_style()
    readable_score = compute_total_score(base_score=10, bonus_points=5)
    print(f"Unclear style score: {unclear_score}")
    print(f"Readable style score: {readable_score}")

    print("\n" + "=" * 70)
    print("SECTION 5: Refactor Demonstration")
    print("=" * 70)
    metrics = refactor_dataset_metrics(dataset_rows=1000, missing_values_count=35)
    print(f"Dataset metrics: {metrics}")

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("✓ Use descriptive variable names that communicate purpose")
    print("✓ Follow snake_case for variables and function names")
    print("✓ Use constants for fixed values to improve clarity")
    print("✓ Write comments that explain why a decision exists")
    print("✓ Avoid over-commenting obvious lines")
    print("✓ Keep naming and comment style consistent in the file")
    print("=" * 70)


if __name__ == "__main__":
    main()
