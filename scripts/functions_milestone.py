"""
Passing Data into Functions and Returning Results
==================================================

This milestone demonstrates:
- Understanding function parameters and arguments
- Passing data into functions correctly
- Returning results using the return statement
- Using returned values in further computation
- Writing functions that are reusable and predictable
- Avoiding common function mistakes

Run:
    python scripts/functions_milestone.py
"""


# ============================================================================
# SECTION 1: Understanding Parameters and Arguments
# ============================================================================

def greet_person(name):
    """
    Accept a name parameter and return a personalized greeting.
    
    Parameters:
        name (str): The name of the person to greet
        
    Returns:
        str: A personalized greeting message
    """
    return f"Hello, {name}! Welcome to the program."


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    area = length * width
    return area


def create_profile(name, age, city="Unknown"):
    """
    Create a user profile with default parameter for city.
    
    Parameters:
        name (str): User's name
        age (int): User's age
        city (str): User's city (default: "Unknown")
        
    Returns:
        str: A formatted profile string
    """
    return f"Profile: {name}, {age} years old, from {city}"


# ============================================================================
# SECTION 2: Returning Values from Functions
# ============================================================================

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    BEST PRACTICE: Return the value, don't print inside the function.
    """
    result = a + b
    return result


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
        price (float): Original price
        discount_percent (float): Discount percentage (e.g., 20 for 20%)
        
    Returns:
        float: Final price after discount
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


def check_even_odd(number):
    """
    Check if a number is even or odd.
    
    Returns:
        str: "Even" or "Odd"
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def get_grade(score):
    """
    Return a letter grade based on the score.
    Demonstrates multiple return paths.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ============================================================================
# SECTION 3: Using Returned Results
# ============================================================================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    pi = 3.14159
    area = pi * radius ** 2
    return area


def calculate_circle_circumference(radius):
    """Calculate the circumference of a circle."""
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference


def calculate_total_with_tax(price, tax_rate):
    """
    Calculate total price including tax.
    
    Parameters:
        price (float): Base price
        tax_rate (float): Tax rate as decimal (e.g., 0.08 for 8%)
        
    Returns:
        float: Total price with tax
    """
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total


# ============================================================================
# SECTION 4: Composing Functions (Using Results in Other Functions)
# ============================================================================

def get_average(num1, num2, num3):
    """Calculate and return the average of three numbers."""
    total = num1 + num2 + num3
    average = total / 3
    return average


def classify_average(num1, num2, num3):
    """
    Get the average and classify it.
    This demonstrates using a function's return value in another function.
    """
    avg = get_average(num1, num2, num3)
    
    if avg >= 90:
        classification = "Excellent"
    elif avg >= 75:
        classification = "Good"
    elif avg >= 60:
        classification = "Average"
    else:
        classification = "Needs Improvement"
    
    return f"Average: {avg:.2f} - {classification}"


# ============================================================================
# SECTION 5: Common Mistakes to AVOID
# ============================================================================

# MISTAKE 1: Printing instead of returning
def bad_add(a, b):
    """BAD PRACTICE: Prints instead of returning."""
    result = a + b
    print(result)  # This prints but doesn't return
    # No return statement means the function returns None


# MISTAKE 2: Hardcoded values
def bad_calculate_area():
    """BAD PRACTICE: Values are hardcoded, not flexible."""
    length = 5  # Hardcoded
    width = 3   # Hardcoded
    return length * width


# CORRECT VERSION: Parameters make it flexible
def good_calculate_area(length, width):
    """GOOD PRACTICE: Uses parameters for flexibility."""
    return length * width


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def main():
    """Main function to demonstrate all concepts."""
    
    print("=" * 70)
    print("SECTION 1: Understanding Parameters and Arguments")
    print("=" * 70)
    
    # Example 1: Single parameter
    greeting = greet_person("Alice")
    print(greeting)
    
    # Example 2: Multiple parameters
    area = calculate_rectangle_area(10, 5)
    print(f"Rectangle area (10 x 5): {area}")
    
    # Example 3: Default parameters
    profile1 = create_profile("Bob", 25, "New York")
    profile2 = create_profile("Charlie", 30)  # Uses default city
    print(profile1)
    print(profile2)
    
    print("\n" + "=" * 70)
    print("SECTION 2: Returning Values from Functions")
    print("=" * 70)
    
    # Store and use returned values
    sum_result = add_numbers(15, 27)
    print(f"Sum of 15 and 27: {sum_result}")
    
    original_price = 100
    discount = 20
    final_price = calculate_discount(original_price, discount)
    print(f"Original price: ${original_price}, After {discount}% discount: ${final_price}")
    
    number = 17
    result = check_even_odd(number)
    print(f"{number} is {result}")
    
    score = 85
    grade = get_grade(score)
    print(f"Score {score} gets grade: {grade}")
    
    print("\n" + "=" * 70)
    print("SECTION 3: Using Returned Results in Calculations")
    print("=" * 70)
    
    # Convert temperatures and use results
    temp_c = 25
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f}°F")
    
    # Convert back
    converted_back = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F = {converted_back:.2f}°C")
    
    # Calculate circle properties
    radius = 5
    circle_area = calculate_circle_area(radius)
    circle_circumference = calculate_circle_circumference(radius)
    print(f"Circle with radius {radius}:")
    print(f"  Area: {circle_area:.2f}")
    print(f"  Circumference: {circle_circumference:.2f}")
    
    # Use results in further calculations
    base_price = 50
    tax = 0.08
    total_price = calculate_total_with_tax(base_price, tax)
    print(f"Base price: ${base_price}, Total with tax: ${total_price:.2f}")
    
    print("\n" + "=" * 70)
    print("SECTION 4: Composing Functions (Chaining Results)")
    print("=" * 70)
    
    # Using one function's result in another function
    grades = [85, 90, 78]
    average = get_average(grades[0], grades[1], grades[2])
    print(f"Average of {grades}: {average:.2f}")
    
    # Even better: classify the average
    classification = classify_average(85, 90, 78)
    print(classification)
    
    # Chain multiple function calls
    temp_celsius = 30
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    back_to_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"Start: {temp_celsius}°C → Convert to {temp_fahrenheit}°F → Convert back: {back_to_celsius:.2f}°C")
    
    print("\n" + "=" * 70)
    print("SECTION 5: Common Mistakes Demonstration")
    print("=" * 70)
    
    # Mistake 1: Function that prints instead of returns
    print("Calling bad_add(5, 3):")
    result_bad = bad_add(5, 3)
    print(f"Returned value: {result_bad}")  # Will be None!
    
    # Correct approach
    print("\nCalling add_numbers(5, 3):")
    result_good = add_numbers(5, 3)
    print(f"Returned value: {result_good}")  # Will be 8
    
    # Mistake 2: Hardcoded values
    print("\nHardcoded area (always same):", bad_calculate_area())
    print("Flexible area (5, 3):", good_calculate_area(5, 3))
    print("Flexible area (10, 7):", good_calculate_area(10, 7))
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("✓ Functions should RETURN values, not print them")
    print("✓ Use parameters to make functions flexible")
    print("✓ Store returned values in variables for reuse")
    print("✓ Chain function calls by passing results as arguments")
    print("✓ Avoid hardcoding values inside functions")
    print("✓ Every execution path should return a value when needed")
    print("=" * 70)


if __name__ == "__main__":
    main()
