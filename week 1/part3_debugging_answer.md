# Part 3 — Debugging the Broken Calculator Code

## Broken code

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

print("Result:", result)
```

## 1. What is wrong with this code?

The main problem is that `num1` and `num2` are not converted into numbers. They are still text values because they come directly from `input()`. The code also only handles addition. It does not handle subtraction, multiplication, division, division by zero, or invalid operations.

There is also another problem: `result` is only created if the operation is `+`. If the user enters another operation, Python will still try to print `result`, but the variable will not exist.

## 2. What happens if the user enters 10 and 5?

If the user enters `10`, `5`, and chooses `+`, the program prints:

```text
Result: 105
```

This happens because Python joins the two strings `"10"` and `"5"` instead of adding the numbers.

## 3. Why is `num1 + num2` not safe here?

It is not safe because both values are strings. In Python, `+` with strings means joining text. To do numeric addition, both values must first be converted using `float()` or `int()`.

## 4. How should the input values be converted?

They should be converted like this:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

I would use `float()` because it supports both whole numbers and decimal numbers.

## 5. What operations are missing?

The missing operations are:

- subtraction with `-`
- multiplication with `*`
- division with `/`

## 6. What other error handling should be added?

The program should handle division by zero. It should also handle invalid operations, such as `%` or `abc`. A better version could also use `try` and `except` to handle cases where the user enters text instead of a number.

## Corrected version

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ").strip()

if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 == 0:
        print("Error: division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operation. Please choose +, -, *, or /.")
```
