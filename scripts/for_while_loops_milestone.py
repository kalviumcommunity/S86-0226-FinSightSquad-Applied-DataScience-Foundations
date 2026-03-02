#!/usr/bin/env python3
"""
Using for and while Loops for Iterative Data Processing Milestone

This script demonstrates:
- for loops over range and lists
- while loops for condition-based repetition
- loop control with break and continue
- safe patterns to avoid infinite loops
"""


def section(title: str) -> None:
    print("\n" + "=" * 64)
    print(title)
    print("=" * 64)


def for_loop_examples() -> None:
    section("1) USING FOR LOOPS FOR ITERATION")

    print("A. Iterate over a range:")
    for day in range(1, 6):
        print(f"Day {day}: process daily expense summary")

    transactions = [120.50, 35.00, 89.99, 15.75]
    print("\nB. Iterate over a list:")
    total_spend = 0.0
    for amount in transactions:
        total_spend += amount
        print(f"Processed transaction: ${amount:.2f}")
    print(f"Total spend: ${total_spend:.2f}")


def while_loop_examples() -> None:
    section("2) USING WHILE LOOPS FOR CONDITION-BASED REPETITION")

    target_savings = 500
    current_savings = 100
    weekly_deposit = 120
    week = 0

    print(
        f"Start savings: ${current_savings}, target: ${target_savings}, "
        f"weekly deposit: ${weekly_deposit}"
    )

    while current_savings < target_savings:
        week += 1
        current_savings += weekly_deposit
        print(f"Week {week}: savings = ${current_savings}")

    print("Savings goal reached. While loop stopped because condition became False.")


def loop_control_examples() -> None:
    section("3) CONTROLLING LOOP FLOW WITH BREAK AND CONTINUE")

    print("A. continue example (skip invalid records):")
    daily_entries = [200, -1, 150, -5, 80]
    valid_total = 0

    for entry in daily_entries:
        if entry < 0:
            print(f"Skipping invalid entry: {entry}")
            continue
        valid_total += entry
        print(f"Accepted entry: {entry}")

    print(f"Valid total: {valid_total}")

    print("\nB. break example (stop on fraud alert):")
    event_stream = ["login", "transfer", "balance_check", "fraud_alert", "logout"]
    for event in event_stream:
        print(f"Event: {event}")
        if event == "fraud_alert":
            print("Fraud alert detected. Stopping processing early with break.")
            break


def avoiding_infinite_loops() -> None:
    section("4) AVOIDING INFINITE LOOPS")

    print("Common cause: condition variable never changes inside while loop.")
    print("Safe pattern: always update loop state and/or use a safety limit.")

    attempts = 0
    max_attempts = 5
    balance = 50
    fee = 15

    while balance > 0 and attempts < max_attempts:
        attempts += 1
        balance -= fee
        print(f"Attempt {attempts}: remaining balance = ${balance}")

    if attempts == max_attempts:
        print("Stopped by safety limit to prevent runaway loops.")
    else:
        print("Stopped because primary condition became False.")


def main() -> None:
    section("USING FOR AND WHILE LOOPS FOR ITERATIVE DATA PROCESSING")
    print("Goal: practice safe, readable iteration logic in Python.")

    for_loop_examples()
    while_loop_examples()
    loop_control_examples()
    avoiding_infinite_loops()

    section("MILESTONE SUMMARY")
    print("- Use for loops when iterating known sequences (lists, ranges).")
    print("- Use while loops when repetition depends on a changing condition.")
    print("- Use continue to skip an iteration and break to exit early.")
    print("- Prevent infinite loops by updating conditions and using safety guards.")


if __name__ == "__main__":
    main()
