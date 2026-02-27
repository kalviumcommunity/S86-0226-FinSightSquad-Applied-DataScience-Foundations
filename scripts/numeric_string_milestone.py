#!/usr/bin/env python3
"""
Numeric and String Data Types Milestone

This script demonstrates:
- Numeric data types (int, float)
- String data type operations
- Safe and unsafe mixing of numbers and strings
- Explicit type conversion
- Type inspection for debugging

Run:
    python scripts/numeric_string_milestone.py
"""


def section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def numeric_examples() -> None:
    section("1) WORKING WITH NUMERIC DATA TYPES")

    whole_number = 25
    decimal_number = 7.5

    print(f"whole_number = {whole_number} (type: {type(whole_number).__name__})")
    print(f"decimal_number = {decimal_number} (type: {type(decimal_number).__name__})")

    print("\nBasic arithmetic:")
    print(f"Addition: {whole_number} + {decimal_number} = {whole_number + decimal_number}")
    print(f"Subtraction: {whole_number} - {decimal_number} = {whole_number - decimal_number}")
    print(f"Multiplication: {whole_number} * {decimal_number} = {whole_number * decimal_number}")
    print(f"Division: {whole_number} / 4 = {whole_number / 4}")
    print(f"Floor division: {whole_number} // 4 = {whole_number // 4}")

    precision_demo = 0.1 + 0.2
    print("\nPrecision note:")
    print(f"0.1 + 0.2 = {precision_demo}")


def string_examples() -> None:
    section("2) UNDERSTANDING STRING DATA TYPES")

    first_name = "Ada"
    role = "Data Scientist"

    print(f"first_name = {first_name} (type: {type(first_name).__name__})")
    print(f"role = {role} (type: {type(role).__name__})")

    full_label = first_name + " - " + role
    print("\nString operations:")
    print(f"Concatenation: {full_label}")
    print(f"Uppercase: {role.upper()}")
    print(f"First character of first_name: {first_name[0]}")


def mixing_types_examples() -> None:
    section("3) MIXING NUMBERS AND STRINGS SAFELY")

    age_number = 21
    age_text = "21"

    print(f"age_number = {age_number} (type: {type(age_number).__name__})")
    print(f"age_text = {age_text} (type: {type(age_text).__name__})")

    print("\nIncorrect mixing example:")
    try:
        result = "Age next year: " + (age_number + 1)
        print(result)
    except TypeError as error:
        print(f"TypeError captured: {error}")

    print("\nCorrect conversion examples:")
    print("Age next year: " + str(age_number + 1))
    print(f"Convert string to number then add: int('{age_text}') + 1 = {int(age_text) + 1}")


def inspect_types_examples() -> None:
    section("4) INSPECTING DATA TYPES")

    values = [42, 3.14, "42", "hello"]
    for value in values:
        print(f"Value: {value!r:<8} -> type: {type(value).__name__}")

    print("\nType checks:")
    print(f"isinstance(42, int): {isinstance(42, int)}")
    print(f"isinstance(3.14, float): {isinstance(3.14, float)}")
    print(f"isinstance('42', str): {isinstance('42', str)}")


def main() -> None:
    section("PYTHON NUMERIC + STRING DATA TYPES MILESTONE")
    print("Goal: Understand how Python handles numbers and text.")

    numeric_examples()
    string_examples()
    mixing_types_examples()
    inspect_types_examples()

    section("MILESTONE SUMMARY")
    print("- Numeric and string values behave differently.")
    print("- Use explicit conversion when combining text and numbers.")
    print("- Check types early to prevent debugging issues later.")


if __name__ == "__main__":
    main()
