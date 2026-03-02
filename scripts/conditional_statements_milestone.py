"""
Conditional Statements Milestone

Purpose:
- Practice writing conditional statements for data logic
- Understand if, elif, and else control flow
- Use logical operators to combine conditions
- Build decision-making logic in Python

This script demonstrates:
1. Basic if statements
2. if-else decision branching
3. Multiple conditions with elif
4. Logical operators (and, or, not)
5. Real-world data validation scenarios
"""

print("=" * 60)
print("CONDITIONAL STATEMENTS MILESTONE")
print("=" * 60)
print()

# ============================================================================
# 1. BASIC IF STATEMENTS
# ============================================================================
print("1. BASIC IF STATEMENTS")
print("-" * 60)

# Example 1: Simple numeric condition
budget = 5000
print(f"Budget: ${budget}")

if budget > 3000:
    print("✓ Budget is sufficient for the project")
print()

# Example 2: String comparison
status = "approved"
print(f"Status: {status}")

if status == "approved":
    print("✓ You can proceed with the transaction")
print()

# Example 3: Condition that is false (no output)
savings = 1000
print(f"Savings: ${savings}")

if savings > 5000:
    print("✓ You can invest in premium options")
print("(No output because condition is false)")
print()

# ============================================================================
# 2. IF-ELSE DECISION BRANCHING
# ============================================================================
print("\n2. IF-ELSE DECISION BRANCHING")
print("-" * 60)

# Example 1: Account balance check
balance = 250
print(f"Account Balance: ${balance}")

if balance >= 500:
    print("✓ Balance is healthy")
else:
    print("⚠ Low balance - consider depositing more funds")
print()

# Example 2: Age eligibility
age = 17
print(f"Age: {age}")

if age >= 18:
    print("✓ Eligible to open an independent account")
else:
    print("⚠ Must open a minor account with guardian")
print()

# Example 3: Transaction type
transaction_type = "withdrawal"
print(f"Transaction Type: {transaction_type}")

if transaction_type == "deposit":
    print("✓ Adding funds to account")
else:
    print("✓ Removing funds from account")
print()

# ============================================================================
# 3. MULTIPLE CONDITIONS WITH ELIF
# ============================================================================
print("\n3. MULTIPLE CONDITIONS WITH ELIF")
print("-" * 60)

# Example 1: Credit score evaluation
credit_score = 720
print(f"Credit Score: {credit_score}")

if credit_score >= 750:
    print("✓ Excellent credit - approved for premium rates")
elif credit_score >= 700:
    print("✓ Good credit - approved for standard rates")
elif credit_score >= 650:
    print("⚠ Fair credit - approved with conditions")
else:
    print("✗ Poor credit - application needs review")
print()

# Example 2: Income bracket classification
annual_income = 65000
print(f"Annual Income: ${annual_income}")

if annual_income >= 100000:
    print("Income Bracket: High")
elif annual_income >= 50000:
    print("Income Bracket: Medium")
elif annual_income >= 25000:
    print("Income Bracket: Low")
else:
    print("Income Bracket: Very Low")
print()

# Example 3: Investment risk level
investment_amount = 15000
print(f"Investment Amount: ${investment_amount}")

if investment_amount >= 50000:
    print("Risk Level: High - consider diversification")
elif investment_amount >= 10000:
    print("Risk Level: Moderate - balanced portfolio recommended")
elif investment_amount >= 1000:
    print("Risk Level: Low - growth focused options available")
else:
    print("Risk Level: Minimal - savings account recommended")
print()

# ============================================================================
# 4. LOGICAL OPERATORS (AND, OR, NOT)
# ============================================================================
print("\n4. LOGICAL OPERATORS")
print("-" * 60)

# Example 1: Using AND - both conditions must be true
print("A. Using AND operator")
account_balance = 3000
account_status = "active"
print(f"Balance: ${account_balance}, Status: {account_status}")

if account_balance >= 1000 and account_status == "active":
    print("✓ Eligible for premium features")
else:
    print("✗ Not eligible for premium features")
print()

# Example 2: Using OR - at least one condition must be true
print("B. Using OR operator")
is_student = True
age_applicant = 22
print(f"Student: {is_student}, Age: {age_applicant}")

if is_student or age_applicant >= 65:
    print("✓ Eligible for fee waiver")
else:
    print("✗ Standard fees apply")
print()

# Example 3: Using NOT - inverts the condition
print("C. Using NOT operator")
account_frozen = False
print(f"Account Frozen: {account_frozen}")

if not account_frozen:
    print("✓ Account is accessible - transactions allowed")
else:
    print("✗ Account is frozen - contact support")
print()

# Example 4: Combining multiple operators
print("D. Combining multiple operators")
monthly_income = 4500
existing_loan = False
credit_history = "good"
print(f"Monthly Income: ${monthly_income}")
print(f"Existing Loan: {existing_loan}")
print(f"Credit History: {credit_history}")

if monthly_income >= 4000 and not existing_loan and credit_history == "good":
    print("✓ Loan application: APPROVED")
elif monthly_income >= 3000 and credit_history != "poor":
    print("⚠ Loan application: CONDITIONAL APPROVAL (verification needed)")
else:
    print("✗ Loan application: REJECTED")
print()

# ============================================================================
# 5. REAL-WORLD DATA VALIDATION SCENARIOS
# ============================================================================
print("\n5. REAL-WORLD DATA VALIDATION SCENARIOS")
print("-" * 60)

# Scenario 1: Investment allocation validation
print("A. Investment Allocation Validator")
stocks_percent = 60
bonds_percent = 25
cash_percent = 15
total = stocks_percent + bonds_percent + cash_percent
print(f"Stocks: {stocks_percent}%, Bonds: {bonds_percent}%, Cash: {cash_percent}%")

if total == 100:
    print("✓ Portfolio allocation is valid")
    if stocks_percent > 70:
        print("  ⚠ Warning: High risk portfolio (>70% stocks)")
    elif stocks_percent < 30:
        print("  ⚠ Warning: Conservative portfolio (<30% stocks)")
    else:
        print("  ✓ Balanced portfolio allocation")
else:
    print(f"✗ Invalid allocation - total is {total}%, must be 100%")
print()

# Scenario 2: Transaction validation
print("B. Transaction Validator")
withdrawal_amount = 1200
current_balance = 5000
daily_limit = 2000
print(f"Withdrawal: ${withdrawal_amount}")
print(f"Balance: ${current_balance}")
print(f"Daily Limit: ${daily_limit}")

if withdrawal_amount <= 0:
    print("✗ Invalid amount - must be positive")
elif withdrawal_amount > daily_limit:
    print(f"✗ Transaction denied - exceeds daily limit of ${daily_limit}")
elif withdrawal_amount > current_balance:
    print("✗ Insufficient funds")
else:
    print("✓ Transaction approved")
    remaining = current_balance - withdrawal_amount
    print(f"  New balance will be: ${remaining}")
print()

# Scenario 3: Data quality check
print("C. Data Quality Checker")
expense_value = 250.50
expense_category = "Food"
expense_date = "2026-03-01"
print(f"Expense: ${expense_value}, Category: {expense_category}, Date: {expense_date}")

# Check if all required fields are valid
has_value = expense_value > 0
has_category = expense_category != "" and expense_category is not None
has_date = expense_date != "" and expense_date is not None

if has_value and has_category and has_date:
    print("✓ Data record is complete and valid")
    print("  Ready for database insertion")
else:
    print("✗ Data record is incomplete:")
    if not has_value:
        print("  - Missing or invalid expense value")
    if not has_category:
        print("  - Missing category")
    if not has_date:
        print("  - Missing date")
print()

# ============================================================================
# CONCLUSION
# ============================================================================
print("=" * 60)
print("MILESTONE COMPLETE")
print("=" * 60)
print("\nKey Takeaways:")
print("• if statements check conditions and execute code when true")
print("• else provides an alternative path when condition is false")
print("• elif allows checking multiple conditions in sequence")
print("• and requires ALL conditions to be true")
print("• or requires AT LEAST ONE condition to be true")
print("• not inverts a boolean condition")
print("• Proper indentation is critical for conditional blocks")
print("• Conditions enable data validation and business logic")
print("\nConditional logic is essential for building intelligent programs!")
