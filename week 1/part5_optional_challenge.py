"""
Part 5 — Optional Challenge

This version extends the basic calculator by:
- using functions for each operation
- allowing repeated calculations
- using try/except for invalid number input
- storing calculation history in a list
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def get_number(prompt):
    """Ask for a number until the user enters valid numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


history = []

print("Optional Challenge Calculator")

while True:
    first = get_number("\nEnter the first number: ")
    second = get_number("Enter the second number: ")
    operation = input("Choose operation (+, -, *, /) or type quit: ").strip()

    if operation.lower() == "quit":
        break

    if operation == "+":
        result = add(first, second)

    elif operation == "-":
        result = subtract(first, second)

    elif operation == "*":
        result = multiply(first, second)

    elif operation == "/":
        result = divide(first, second)
        if result is None:
            print("Error: division by zero is not allowed.")
            continue

    else:
        print("Invalid operation.")
        continue

    calculation = f"{first} {operation} {second} = {result}"
    history.append(calculation)
    print("Result:", result)

    again = input("Do you want to continue? (yes/no): ").strip().lower()
    if again != "yes":
        break

print("\nCalculation history:")
if len(history) == 0:
    print("No successful calculations.")
else:
    for item in history:
        print("-", item)
