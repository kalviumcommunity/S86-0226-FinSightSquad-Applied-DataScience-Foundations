"""
Comparing Distributions Across Multiple Columns Milestone
=========================================================

This milestone demonstrates how to compare distributions across multiple
numeric columns in a Pandas DataFrame using summary statistics.

Run:
    python scripts/comparing_distributions_milestone.py
"""

import pandas as pd


print("=" * 78)
print("COMPARING DISTRIBUTIONS ACROSS MULTIPLE COLUMNS")
print("=" * 78)


# ============================================================================
# 0. Load a DataFrame with multiple numeric columns
# ============================================================================
print("\n0. LOAD A DATAFRAME WITH MULTIPLE NUMERIC COLUMNS")
print("-" * 78)

df_metrics = pd.DataFrame(
    {
        "monthly_spend": [1200, 1400, 1350, 1600, 1500, 1700, 1550, 2100, 1450, 1650],
        "transaction_count": [48, 52, 50, 61, 58, 66, 57, 93, 54, 60],
        "savings_rate_pct": [18.0, 20.0, 19.0, 17.0, 21.0, 16.0, 20.0, 5.0, 22.0, 18.0],
        "investment_return_pct": [2.4, 1.8, 2.1, 2.7, 1.9, 2.5, 2.2, -1.5, 2.0, 2.3],
    }
)

print("DataFrame preview:")
print(df_metrics)
print(f"\nShape: {df_metrics.shape}")
print(f"Numeric columns: {df_metrics.columns.tolist()}")


# ============================================================================
# 1. Understanding distributions across columns
# ============================================================================
print("\n1. UNDERSTANDING DISTRIBUTIONS ACROSS COLUMNS")
print("-" * 78)
print(
    "A distribution shows how values are spread for one column. "
    "Comparing columns side by side gives context that single-column analysis misses."
)
print("\nWe will compare columns using:")
print("- Central tendency: mean and median")
print("- Spread: min, max, range, std, and IQR")
print("- Relative variability: coefficient of variation (std/mean)")


# ============================================================================
# 2. Compare central tendency
# ============================================================================
print("\n2. COMPARING CENTRAL TENDENCY")
print("-" * 78)

central_tendency = pd.DataFrame(
    {
        "mean": df_metrics.mean(numeric_only=True),
        "median": df_metrics.median(numeric_only=True),
    }
)
central_tendency["mean_minus_median"] = central_tendency["mean"] - central_tendency["median"]

print("Central tendency summary:")
print(central_tendency.round(3))

print("\nInterpretation notes:")
for column_name, row in central_tendency.iterrows():
    gap = row["mean_minus_median"]
    if abs(gap) < 0.1:
        note = "mean and median are very close (more balanced center)."
    elif gap > 0:
        note = "mean is above median (possible right skew or high-value pull)."
    else:
        note = "mean is below median (possible left skew or low-value pull)."
    print(f"- {column_name}: {note}")


# ============================================================================
# 3. Compare spread and variability
# ============================================================================
print("\n3. COMPARING SPREAD AND VARIABILITY")
print("-" * 78)

q1 = df_metrics.quantile(0.25, numeric_only=True)
q3 = df_metrics.quantile(0.75, numeric_only=True)

spread_summary = pd.DataFrame(
    {
        "min": df_metrics.min(numeric_only=True),
        "max": df_metrics.max(numeric_only=True),
        "range": df_metrics.max(numeric_only=True) - df_metrics.min(numeric_only=True),
        "std": df_metrics.std(numeric_only=True),
        "q1": q1,
        "q3": q3,
        "iqr": q3 - q1,
    }
)

# Coefficient of variation helps compare variability across columns with
# different scales.
spread_summary["cv_pct"] = (spread_summary["std"] / central_tendency["mean"]) * 100

print("Spread summary:")
print(spread_summary.round(3))

highest_std_col = spread_summary["std"].idxmax()
lowest_std_col = spread_summary["std"].idxmin()
highest_cv_col = spread_summary["cv_pct"].idxmax()
lowest_cv_col = spread_summary["cv_pct"].idxmin()

print("\nVariability comparison:")
print(f"- Highest absolute variability (std): {highest_std_col}")
print(f"- Lowest absolute variability (std): {lowest_std_col}")
print(f"- Highest relative variability (CV%): {highest_cv_col}")
print(f"- Lowest relative variability (CV%): {lowest_cv_col}")


# ============================================================================
# 4. Identify patterns and anomalies conceptually
# ============================================================================
print("\n4. IDENTIFYING PATTERNS AND ANOMALIES")
print("-" * 78)

z_scores = (df_metrics - df_metrics.mean()) / df_metrics.std(ddof=1)

print("Potential unusual values (|z-score| > 2):")
found_unusual = False
for column_name in z_scores.columns:
    unusual_rows = z_scores.index[z_scores[column_name].abs() > 2].tolist()
    if unusual_rows:
        found_unusual = True
        values = df_metrics.loc[unusual_rows, column_name].tolist()
        print(f"- {column_name}: rows {unusual_rows} -> values {values}")

if not found_unusual:
    print("- None found using this threshold in the sample data.")

print("\nConceptual takeaways:")
print("- Compare center and spread together before making claims.")
print("- Larger range/std suggests more volatility, not automatically better or worse.")
print("- Mean-vs-median gaps can hint at skew or outlier influence.")
print("- Unusual points are prompts for deeper questions, not instant conclusions.")


# ============================================================================
# 5. Summary
# ============================================================================
print("\n5. SUMMARY")
print("=" * 78)
print("What this milestone practiced:")
print("1. Loaded a DataFrame with multiple numeric columns")
print("2. Computed summary statistics for each column")
print("3. Compared means and medians across columns")
print("4. Compared range, standard deviation, and IQR")
print("5. Compared relative variability using coefficient of variation")
print("6. Flagged potentially unusual values conceptually")
print("7. Interpreted differences without jumping to conclusions")
print("=" * 78)
print("MILESTONE COMPLETE")
print("=" * 78)
