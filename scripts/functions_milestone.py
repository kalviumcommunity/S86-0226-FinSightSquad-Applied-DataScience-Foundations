"""Functions milestone examples for the milestone task.

Demonstrates:
- Defining functions with `def`
- Calling functions with positional and keyword arguments
- Default parameters
- Return values vs printing
- Basic recursion
- Local vs global scope

Run:
    python scripts/functions_milestone.py
"""

def greet(name):
    """Return a friendly greeting for `name`."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b=1):
    """Multiply `a` by `b`. `b` has a default value of 1."""
    return a * b


def factorial(n):
    """Return factorial of n (n >= 0) using recursion."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


GLOBAL_COUNT = 0

def increment_local(count):
    """Show that modifying the parameter does not change the global variable."""
    count += 1
    return count


def increment_global():
    """Use the `global` keyword to modify a global variable."""
    global GLOBAL_COUNT
    GLOBAL_COUNT += 1
    return GLOBAL_COUNT


def demonstrate_scope():
    """Print local and global variables to show scope behavior."""
    local_var = "I am local"
    print("Inside demonstrate_scope: local_var=", local_var)
    print("Inside demonstrate_scope: GLOBAL_COUNT=", GLOBAL_COUNT)


def main():
    print(greet("Alice"))

    print("add(2, 3) =>", add(2, 3))
    print("multiply(5) =>", multiply(5))
    print("multiply(a=5, b=3) =>", multiply(a=5, b=3))

    print("factorial(5) =>", factorial(5))

    x = 0
    print("increment_local(x) =>", increment_local(x))
    print("GLOBAL_COUNT before increment_global() =>", GLOBAL_COUNT)
    increment_global()
    print("GLOBAL_COUNT after increment_global() =>", GLOBAL_COUNT)

    demonstrate_scope()


if __name__ == "__main__":
    main()
