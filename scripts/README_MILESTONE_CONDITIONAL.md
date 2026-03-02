# Conditional Statements for Data Logic Milestone

## Purpose

This milestone focuses on writing conditional statements to control program flow based on data-driven logic. Conditions allow your code to make decisions, which is essential for validation, branching workflows, and real-world data handling.

Understanding conditional logic is a core programming skill that enables you to move beyond linear scripts and build intelligent behavior into your code.

---

## Learning Objectives

This lesson helps you:

- Understand how conditional statements work in Python
- Use `if`, `elif`, and `else` correctly
- Write conditions based on numeric and string data
- Combine conditions using logical operators
- Apply conditionals to simple data scenarios

By completing this milestone, you will be able to:

- Write clear and correct conditional statements
- Control program flow based on data values
- Handle multiple conditions safely
- Avoid common logic and indentation errors
- Use conditionals confidently in data workflows

---

## Why This Matters

Common beginner issues include:

- Code that runs but produces incorrect results
- Conditions that never trigger as expected
- Incorrect indentation causing logic bugs
- Overly complex or unreadable condition blocks

These problems usually stem from weak conditional logic.

This milestone ensures that:

- Your code behaves predictably
- Decisions are based on correct data checks
- Edge cases are handled intentionally
- Logic is readable and maintainable

Think of conditionals as decision points—this lesson teaches you how to design them clearly.

---

## Run the Script

```bash
python scripts/conditional_statements_milestone.py
```

---

## What the Script Demonstrates

### 1. Basic if Statements

- Use `if` to check a condition
- Execute code when the condition is true
- Observe what happens when the condition is false
- Keep conditions readable and intentional

Examples:
- Budget threshold checks
- Status verification
- Savings level validation

### 2. if-else Decision Branching

- Add `else` blocks where appropriate
- Ensure both outcomes are handled
- Avoid unnecessary nesting
- Clearly separate logic paths

Examples:
- Account balance checks
- Age eligibility verification
- Transaction type handling

### 3. Multiple Conditions with elif

- Use `elif` for multiple condition checks
- Order conditions carefully
- Ensure only one branch executes
- Avoid overlapping or redundant checks

Examples:
- Credit score evaluation
- Income bracket classification
- Investment risk level assessment

### 4. Logical Operators

- Use `and` to require multiple conditions
- Use `or` to allow alternative conditions
- Use `not` to invert conditions
- Keep combined conditions readable

Examples:
- Premium feature eligibility (AND)
- Fee waiver qualification (OR)
- Account accessibility (NOT)
- Loan application approval (combined)

### 5. Real-World Data Validation

- Portfolio allocation validation
- Transaction authorization
- Data quality checking
- Business logic implementation

---

## Expected Learning Outcomes

After completing this milestone, you should be able to:

1. **Differentiate** between `if`, `elif`, and `else` use cases
2. **Write** conditions using comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
3. **Combine** conditions using logical operators (`and`, `or`, `not`)
4. **Predict** which code block will execute given specific input values
5. **Debug** indentation and logic errors in conditional statements
6. **Apply** conditionals to data validation scenarios
7. **Design** readable and maintainable decision structures

---

## Key Concepts Covered

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators
- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Inverts the boolean value

### Control Flow
- `if` - Execute code when condition is True
- `elif` - Check alternative conditions
- `else` - Execute code when all previous conditions are False

---

## Common Pitfalls to Avoid

1. **Indentation Errors**
   ```python
   # WRONG
   if balance > 100:
   print("Sufficient funds")  # IndentationError
   
   # CORRECT
   if balance > 100:
       print("Sufficient funds")
   ```

2. **Using = instead of ==**
   ```python
   # WRONG - Assignment, not comparison
   if status = "approved":
   
   # CORRECT
   if status == "approved":
   ```

3. **Overlapping Conditions**
   ```python
   # POOR - Second condition never reached
   if score >= 70:
       print("Pass")
   elif score >= 60:  # Never reached if score is 75
       print("Borderline")
   ```

4. **Overly Complex Conditions**
   ```python
   # HARD TO READ
   if (a > 5 and b < 10 or c == 3) and not (d >= 7 or e != 2):
   
   # BETTER - Break into smaller checks
   condition1 = a > 5 and b < 10
   condition2 = c == 3
   condition3 = not (d >= 7 or e != 2)
   if (condition1 or condition2) and condition3:
   ```

---

## Video Walkthrough Requirements

Record a ~2 minute screen-capture video demonstrating:

1. **A simple if statement** - Show code execution with true and false conditions
2. **An if–else example** - Demonstrate both branches executing
3. **An if–elif–else example** - Show multiple condition paths
4. **Use of logical operators** - Demonstrate `and`, `or`, or `not`
5. **Explanation of decision outcomes** - Verbally explain why each branch executed

### Video Submission Guidelines

- Submit your work as a Pull Request (if required)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible
- Show actual code execution with print outputs
- Explain your logic verbally as you demonstrate

---

## Next Steps

After mastering conditional statements, you'll be ready to:

- Build more complex data validation logic
- Implement business rules in data workflows
- Create interactive decision-making programs
- Combine conditionals with loops for iteration
- Handle edge cases in data processing

---

## Important Notes

- Focus on correctness, not complexity
- Watch indentation carefully (Python requires consistent spacing)
- Keep conditions readable and maintainable
- Test multiple input values mentally or with prints
- Remember: conditional logic is the backbone of intelligent programs

This milestone ensures you can write clear, correct decisions in Python confidently.
