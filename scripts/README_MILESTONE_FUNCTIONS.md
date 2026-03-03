# Passing Data into Functions and Returning Results

## Milestone Overview

This milestone focuses on **passing data into Python functions** and **returning results** to build reusable and flexible programs. Understanding how data flows into and out of functions is essential for writing modular, testable, and maintainable code.

Instead of hardcoding values or printing everything, functions should accept inputs and return outputs that can be reused elsewhere in your program.

## Learning Objectives

By completing this milestone, you will be able to:

✓ Define functions that accept input parameters  
✓ Call functions with different arguments  
✓ Return values from functions reliably  
✓ Store and reuse returned results  
✓ Design functions with clear input-output behavior  

## Why This Matters

Common beginner issues include:

- Functions that only print values instead of returning them
- Hardcoded values inside functions
- Difficulty reusing function results
- Confusing data flow across a program

These issues limit scalability and reuse.

This milestone ensures that:

- Functions behave like clear input-output units
- Logic can be reused across the program
- Code is easier to test and extend
- Data flows predictably through functions

**Think of functions as machines—you put data in, and you get results out.**

## What You Are Expected to Do

This is a **Python fundamentals milestone**, not a data analysis task.

You are expected to:

- Define functions with parameters
- Pass values into functions during calls
- Use `return` to send results back
- Print returned values outside the function

No datasets or advanced libraries are required.

---

## Core Concepts

### 1. Understanding Parameters and Arguments

Learn how functions accept input.

You should:

- Define parameters in the function signature
- Pass arguments during function calls
- Match arguments to parameters correctly
- Use meaningful parameter names

This makes functions flexible.

**Example:**
```python
def greet_person(name):
    return f"Hello, {name}!"

message = greet_person("Alice")
print(message)  # Output: Hello, Alice!
```

---

### 2. Returning Values from Functions

Learn how to send data back.

You should:

- Use the `return` statement
- Return a single value or expression
- Understand when a function ends execution
- Avoid unnecessary print statements inside functions

Returning values enables reuse.

**Example:**
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8
```

---

### 3. Using Returned Results

Work with function outputs.

You should:

- Store returned values in variables
- Use returned values in calculations
- Pass returned values to other functions
- Print results only when needed

This builds composable logic.

**Example:**
```python
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

original = 100
final = calculate_discount(original, 20)
print(f"Final price: ${final}")  # Output: Final price: $80.0
```

---

### 4. Avoiding Common Function Mistakes

Understand pitfalls.

You should:

- Avoid hardcoding values
- Avoid mixing print and return incorrectly
- Ensure every execution path returns a value when needed
- Keep function logic focused

Good habits prevent bugs.

**Bad Practice:**
```python
def bad_add(a, b):
    result = a + b
    print(result)  # Prints but doesn't return
    # Returns None by default
```

**Good Practice:**
```python
def good_add(a, b):
    result = a + b
    return result  # Returns the value for reuse
```

---

## File Structure

```
scripts/
└── functions_milestone.py       # Main implementation file
    └── Contains 5 sections:
        1. Understanding Parameters and Arguments
        2. Returning Values from Functions
        3. Using Returned Results
        4. Composing Functions
        5. Common Mistakes to Avoid

outputs/
├── VIDEO_INSTRUCTIONS_FUNCTIONS.txt  # Video recording instructions
└── video_link.txt                     # Submit your video link here
```

---

## Usage

Run the functions milestone examples:

```bash
python scripts/functions_milestone.py
```

The script demonstrates:

- Functions with single and multiple parameters
- Default parameter values
- Returning values vs printing
- Using returned results in calculations
- Chaining function calls
- Common mistakes and how to avoid them

---

## Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating function inputs and outputs.

Your video must include:

1. **A function with parameters** - Show the definition
2. **Passing arguments into the function** - Call it with values
3. **Returning a value** - Show the return statement
4. **Using the returned result elsewhere** - Store and reuse it

See detailed instructions in: `outputs/VIDEO_INSTRUCTIONS_FUNCTIONS.txt`

---

## Submission Guidelines

- [ ] Complete the implementation in `scripts/functions_milestone.py`
- [ ] Run the script and verify all outputs
- [ ] Record a ~2 minute video demonstration
- [ ] Video must be screen-facing and clearly visible
- [ ] Upload video and add link to `outputs/video_link.txt`
- [ ] Submit your work as a Pull Request (if required)

---

## Key Takeaways

✓ **Prefer returning values over printing**  
✓ **Keep functions predictable**  
✓ **Use clear parameter names**  
✓ **Well-designed functions improve program structure**  

Understanding how data flows through functions is critical for clean coding. This milestone ensures you can pass data into functions and return results confidently.

---

## Checklist

- [ ] Define at least 3 functions with different parameter patterns
- [ ] Demonstrate returning values from functions
- [ ] Show using returned values in further computations
- [ ] Explain common mistakes in the video
- [ ] Upload video and add link to `outputs/video_link.txt`

---

## Additional Resources

- Python official documentation: [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Real Python: [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)

---

**Remember:** Functions are the building blocks of reusable code. Master parameter passing and return values to write better programs!
