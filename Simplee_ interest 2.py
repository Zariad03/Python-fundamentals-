"""
Simple Interest Calculator

This program asks the user for a name, principal amount, interest rate,
and time in years. It validates the numeric inputs, uses string
manipulation to process text, and calculates simple interest.
"""

import math


def get_positive_number(prompt):
    """Get a valid positive number from the user."""
    while True:
        user_input = input(prompt).strip()

        # Check whether the user entered anything.
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            number = float(user_input)

            # Reject zero, negative numbers, and non-finite values.
            if not math.isfinite(number) or number <= 0:
                print("Please enter a finite number greater than zero.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_name():
    """Ask for a name and clean up the text."""
    while True:
        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty. Please try again.")
            continue

        # Convert the name to title case.
        return name.title()


def analyze_description():
    """Demonstrate string transformation and analysis."""
    description = input("In a few words, describe the calculation: ").strip()

    # Split the description into words and count them.
    words = description.split()
    word_count = len(words)

    # Count occurrences of the word 'interest', ignoring case.
    interest_count = description.lower().split().count("interest")

    print("\n--- Text Analysis ---")
    print(f"Cleaned description: {' '.join(words)}")
    print(f"Number of words: {word_count}")
    print(f"Occurrences of 'interest': {interest_count}")


def main():
    """Run the Simple Interest Calculator."""
    print("Welcome to the Simple Interest Calculator!")

    name = get_name()

    # Collect and validate all three numeric inputs.
    principal = get_positive_number("Enter the principal amount: $")
    rate = get_positive_number("Enter the annual interest rate (%): ")
    time = get_positive_number("Enter the time in years: ")

    # Calculate simple interest.
    interest = (principal * rate * time) / 100

    print("\n--- Calculation Results ---")
    print(f"Hello, {name}!")
    print(f"Principal: ${principal:,.2f}")
    print(f"Interest Rate: {rate:.2f}%")
    print(f"Time: {time:g} years")
    print(f"Simple Interest: ${interest:,.2f}")

    analyze_description()


if __name__ == "__main__":
    main()
