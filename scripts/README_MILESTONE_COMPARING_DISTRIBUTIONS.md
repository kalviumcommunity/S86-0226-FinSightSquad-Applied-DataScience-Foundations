# Comparing Distributions Across Multiple Columns Milestone

## Overview

This milestone focuses on comparing distributions across multiple numeric columns in a Pandas DataFrame.

Comparing distributions helps you understand how variables behave relative to each other and reveals patterns that single-column analysis cannot show.

## Learning Objectives

By completing this milestone, you will be able to:

- Understand what a data distribution represents
- Compare central tendency across columns
- Compare spread and variability across columns
- Identify differences and similarities between variables
- Build intuition for multi-column analysis

## Why This Matters

Common beginner issues include:

- Analyzing columns in isolation
- Missing relationships between variables
- Comparing raw values instead of distributions
- Drawing conclusions without context

Most real insights come from comparison, not isolation.

## What You Are Expected to Do

This is a data understanding milestone, not a modeling task.

You are expected to:

- Load a DataFrame with multiple numeric columns
- Compute summary statistics for each column
- Compare distributions using statistics
- Interpret differences meaningfully

No visualization or modeling is required.

## File

```text
scripts/comparing_distributions_milestone.py
```

## How to Run

From repository root:

```bash
python scripts/comparing_distributions_milestone.py
```

## What the Script Demonstrates

1. **Understanding distributions across columns**
   - Defines distribution in practical terms
   - Frames comparison mindset before interpretation

2. **Comparing central tendency**
   - Computes mean and median for each numeric column
   - Compares mean-minus-median to hint at potential skew

3. **Comparing spread and variability**
   - Computes min, max, range, standard deviation, Q1, Q3, IQR
   - Uses coefficient of variation (CV%) to compare relative variability across scales

4. **Identifying patterns and anomalies conceptually**
   - Flags potential unusual values with a simple z-score threshold
   - Emphasizes that anomalies are prompts for questions, not final conclusions

5. **Summary output**
   - Recaps the full comparison workflow clearly

## Key Concepts Reinforced

- Central tendency is only part of the story
- Spread explains consistency vs volatility
- Relative variability is useful when columns have different units/scales
- Comparison adds context that single-column analysis cannot provide
- EDA should raise better questions before decisions are made

## Submission Checklist

- [ ] Script runs without errors
- [ ] Mean and median are compared across columns
- [ ] Range and standard deviation are compared across columns
- [ ] At least one relative variability measure is interpreted
- [ ] Potential unusual values are identified conceptually
- [ ] Interpretation avoids unsupported conclusions
