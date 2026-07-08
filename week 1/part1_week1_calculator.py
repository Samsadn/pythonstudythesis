"""
Part 1 — Week 1 Simple Calculator

This program asks the user for two numbers and one arithmetic operation.
It supports addition, subtraction, multiplication, and division.
"""

print("Simple Calculator")

# Ask the user for two numbers.
# input() gives text, so float() converts the input into numbers.
left_number = float(input("Enter the first number: "))
right_number = float(input("Enter the second number: "))

# Ask the user which operation should be performed.
operator = input("Choose operation (+, -, *, /): ").strip()

# Choose the calculation based on the selected operator.
if operator == "+":
    answer = left_number + right_number
    print("Result:", answer)

elif operator == "-":
    answer = left_number - right_number
    print("Result:", answer)

elif operator == "*":
    answer = left_number * right_number
    print("Result:", answer)

elif operator == "/":
    # Division by zero is not possible, so this case must be checked.
    if right_number == 0:
        print("Error: division by zero is not allowed.")
    else:
        answer = left_number / right_number
        print("Result:", answer)

else:
    # This handles anything other than +, -, *, or /.
    print("Invalid operation. Please choose +, -, *, or /.")
