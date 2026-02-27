"""
First Data Analysis Script
===========================
This script demonstrates basic data analysis using Python.
It performs simple calculations on sample financial data.

Purpose: Learn how to create and run Python scripts for data analysis
Author: Kalvium Student
Date: February 27, 2026
"""

# Sample financial data - monthly expenses in dollars
monthly_expenses = [1200, 1350, 1100, 1500, 1250, 1400]
months = ["January", "February", "March", "April", "May", "June"]

print("=" * 50)
print("MoneyMind: First Data Analysis Script")
print("=" * 50)
print()

# 1. Display raw data
print("📊 Monthly Expenses Data:")
print("-" * 50)
for month, expense in zip(months, monthly_expenses):
    print(f"{month:10s}: ${expense:,.2f}")
print()

# 2. Calculate basic statistics
total_expenses = sum(monthly_expenses)
average_expense = total_expenses / len(monthly_expenses)
max_expense = max(monthly_expenses)
min_expense = min(monthly_expenses)
expense_range = max_expense - min_expense

# 3. Display analysis results
print("📈 Analysis Results:")
print("-" * 50)
print(f"Total Expenses:   ${total_expenses:,.2f}")
print(f"Average Expense:  ${average_expense:,.2f}")
print(f"Highest Month:    ${max_expense:,.2f}")
print(f"Lowest Month:     ${min_expense:,.2f}")
print(f"Expense Range:    ${expense_range:,.2f}")
print()

# 4. Find the month with highest and lowest expenses
highest_month = months[monthly_expenses.index(max_expense)]
lowest_month = months[monthly_expenses.index(min_expense)]

print("🎯 Key Insights:")
print("-" * 50)
print(f"• {highest_month} had the highest expenses (${max_expense:,.2f})")
print(f"• {lowest_month} had the lowest expenses (${min_expense:,.2f})")

# 5. Calculate percentage difference from average
print(f"• Expense variation range: {(expense_range/average_expense)*100:.1f}% of average")
print()

# 6. Budget recommendations
budget_target = average_expense * 0.9  # 10% reduction goal
print("💡 Budget Recommendation:")
print("-" * 50)
print(f"Target monthly expense: ${budget_target:,.2f}")
print(f"This represents a 10% reduction from the current average.")
print()

print("=" * 50)
print("✅ Analysis Complete!")
print("=" * 50)
