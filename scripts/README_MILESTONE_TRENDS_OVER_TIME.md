# Identifying Trends Over Time Using Line Plots Milestone

## Overview

This milestone focuses on identifying trends over time using line plots.

Line plots are one of the clearest ways to analyze time-based data because they
preserve temporal order and make changes easy to see across a continuous
timeline.

## Learning Objectives

By completing this milestone, you will be able to:

- Understand what time-series data represents
- Create a line plot for time-based data
- Identify upward, downward, or stable trends
- Recognize spikes, drops, and short-term volatility
- Interpret patterns over time without jumping to conclusions

## Why This Matters

Common beginner issues include:

- Treating time-based data like unordered data
- Missing long-term direction because values were not visualized
- Overreacting to one unusual point
- Confusing short-term noise with a meaningful trend
- Ignoring whether observations are regularly spaced over time

Time adds context that static summaries cannot provide.

## What You Are Expected to Do

This is a data visualization milestone, not a forecasting or modeling task.

You are expected to:

- Load a dataset with a time-based column
- Convert the time column to a proper datetime type
- Sort the dataset in temporal order
- Create a line plot using time on the x-axis and a numeric variable on the y-axis
- Interpret the overall trend and any visible anomalies

## Files

```text
data/raw/monthly_savings_trend.csv
scripts/trends_over_time_milestone.py
outputs/VIDEO_INSTRUCTIONS_TRENDS_OVER_TIME.txt
```

## How to Run

From the repository root:

```bash
python scripts/trends_over_time_milestone.py
```

## What the Script Demonstrates

### 0. Loading a dataset with a time-based column

- Reads a CSV file containing monthly observations
- Identifies the date column and numeric value column

### 1. Understanding time-based data

- Converts the date column using `pd.to_datetime()`
- Checks whether the dataset is already in time order
- Sorts the data correctly before analysis
- Shows the observed spacing between time points

### 2. Creating a line plot

- Uses the time column on the x-axis
- Uses savings balance on the y-axis
- Applies axis labels and a title
- Saves the figure for review in `outputs/figures/`

### 3. Identifying trends

- Compares the starting and ending values
- Interprets the overall direction of change
- Compares the first half of the year with the second half
- Distinguishes long-term movement from month-to-month variation

### 4. Spotting changes and anomalies

- Computes month-to-month change
- Identifies the sharpest increase and drop
- Flags potentially unusual moves conceptually
- Emphasizes that anomalies should trigger questions, not instant conclusions

## Key Concepts Reinforced

- Time-based data must be analyzed in order
- Line plots highlight continuity across a timeline
- Overall trend matters more than isolated points
- Sudden changes can indicate important events worth investigating
- Temporal visualization is a core part of exploratory data analysis

## Submission Checklist

- [ ] Script runs without errors
- [ ] The time column is converted and sorted correctly
- [ ] A line plot is created and saved successfully
- [ ] The overall trend is described clearly
- [ ] At least one spike or drop is identified and interpreted conceptually
- [ ] Interpretation focuses on observation, not prediction
