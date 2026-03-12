"""
Identifying Trends Over Time Using Line Plots Milestone
=======================================================

This milestone demonstrates how to work with time-based data, create a line
plot, and interpret long-term trends, short-term changes, and unusual shifts.

Run:
    python scripts/trends_over_time_milestone.py
"""

from pathlib import Path

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "raw" / "monthly_savings_trend.csv"
FIGURE_FILE = ROOT_DIR / "outputs" / "figures" / "trends_over_time_line_plot.png"


print("=" * 78)
print("IDENTIFYING TRENDS OVER TIME USING LINE PLOTS")
print("=" * 78)


# ============================================================================
# 0. Load a dataset with a time-based column
# ============================================================================
print("\n0. LOAD A DATASET WITH A TIME-BASED COLUMN")
print("-" * 78)

df_trends = pd.read_csv(DATA_FILE)

print("Raw dataset preview:")
print(df_trends)
print(f"\nSource file: {DATA_FILE}")
print(f"Time column: month")
print(f"Numeric column: savings_balance_usd")


# ============================================================================
# 1. Understanding time-based data
# ============================================================================
print("\n1. UNDERSTANDING TIME-BASED DATA")
print("-" * 78)

df_trends["month"] = pd.to_datetime(df_trends["month"])
dates_already_sorted = df_trends["month"].is_monotonic_increasing

print(f"Dates already in correct order before sorting? {dates_already_sorted}")
print("Time-based analysis should always follow temporal order.")

df_trends = df_trends.sort_values("month").reset_index(drop=True)

print("\nSorted dataset preview:")
print(df_trends)

interval_days = df_trends["month"].diff().dropna().dt.days
print(f"\nObserved gaps between points (days): {interval_days.tolist()}")
print(
    "These are monthly observations. The spacing is regular by calendar month, "
    "even though the number of days between months varies."
)


# ============================================================================
# 2. Creating a line plot
# ============================================================================
print("\n2. CREATING A LINE PLOT")
print("-" * 78)

FIGURE_FILE.parent.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(10, 5))
plt.plot(
    df_trends["month"],
    df_trends["savings_balance_usd"],
    marker="o",
    linewidth=2.5,
    color="#1f6aa5",
)
plt.title("Monthly Savings Balance Over Time")
plt.xlabel("Month")
plt.ylabel("Savings Balance (USD)")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIGURE_FILE, dpi=150)
plt.close()

print("Line plot created successfully.")
print(f"Saved figure: {FIGURE_FILE}")
print("A line plot connects values in order, making temporal change easy to see.")


# ============================================================================
# 3. Identifying trends
# ============================================================================
print("\n3. IDENTIFYING TRENDS")
print("-" * 78)

starting_value = df_trends.loc[0, "savings_balance_usd"]
ending_value = df_trends.loc[len(df_trends) - 1, "savings_balance_usd"]
overall_change = ending_value - starting_value
overall_pct_change = (overall_change / starting_value) * 100

if overall_change > 0:
    overall_direction = "upward"
elif overall_change < 0:
    overall_direction = "downward"
else:
    overall_direction = "stable"

first_half_average = df_trends.loc[:5, "savings_balance_usd"].mean()
second_half_average = df_trends.loc[6:, "savings_balance_usd"].mean()

print(f"Starting balance: ${starting_value:,.0f}")
print(f"Ending balance: ${ending_value:,.0f}")
print(f"Overall change: ${overall_change:,.0f} ({overall_pct_change:.2f}%)")
print(f"Overall direction: {overall_direction}")
print(f"Average balance in first half of the year: ${first_half_average:,.2f}")
print(f"Average balance in second half of the year: ${second_half_average:,.2f}")

print("\nInterpretation:")
print("- The long-term pattern is upward because the ending value is above the start.")
print("- Month-to-month movement still matters, but single points should not override the full trend.")
print("- Comparing the first and second half helps separate direction from short-term noise.")


# ============================================================================
# 4. Spotting changes and anomalies
# ============================================================================
print("\n4. SPOTTING CHANGES AND ANOMALIES")
print("-" * 78)

df_trends["month_to_month_change"] = df_trends["savings_balance_usd"].diff()

largest_increase_index = df_trends["month_to_month_change"].idxmax()
largest_drop_index = df_trends["month_to_month_change"].idxmin()

largest_increase_row = df_trends.loc[largest_increase_index]
largest_drop_row = df_trends.loc[largest_drop_index]

change_std = df_trends["month_to_month_change"].dropna().std()
unusual_moves = df_trends[
    df_trends["month_to_month_change"].abs() > change_std
][["month", "savings_balance_usd", "month_to_month_change"]]

print(
    "Largest increase: "
    f"{largest_increase_row['month'].date()} -> "
    f"${largest_increase_row['month_to_month_change']:,.0f}"
)
print(
    "Largest drop: "
    f"{largest_drop_row['month'].date()} -> "
    f"${largest_drop_row['month_to_month_change']:,.0f}"
)

print("\nPotentially unusual moves compared with typical month-to-month change:")
if unusual_moves.empty:
    print("- None flagged by this simple threshold.")
else:
    for _, row in unusual_moves.iterrows():
        print(
            f"- {row['month'].date()}: balance ${row['savings_balance_usd']:,.0f}, "
            f"change ${row['month_to_month_change']:,.0f}"
        )

print("\nConceptual takeaway:")
print("- Sudden drops or spikes are signals to investigate, not conclusions by themselves.")
print("- The visual should prompt questions such as what event caused the sharp August drop.")
print("- Line plots are useful because they show both continuity and disruption across time.")


# ============================================================================
# 5. Summary
# ============================================================================
print("\n5. SUMMARY")
print("=" * 78)
print("What this milestone practiced:")
print("1. Loaded a dataset with a time-based column")
print("2. Converted the time column to datetime")
print("3. Sorted the data into the correct temporal order")
print("4. Created a line plot to visualize change over time")
print("5. Identified the overall direction of the trend")
print("6. Flagged sudden changes as prompts for deeper analysis")
print("7. Interpreted the pattern without forecasting or modeling")
print("=" * 78)
print("MILESTONE COMPLETE")
print("=" * 78)