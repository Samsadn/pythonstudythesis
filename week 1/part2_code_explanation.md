# Part 2 — Code Explanation

## 1. What variables did you use, and what does each variable store?

I used `left_number` to store the first number entered by the user and `right_number` to store the second number. I used `operator` to store the operation chosen by the user, for example `+`, `-`, `*`, or `/`. When the operation is valid, I use `answer` to store the result before printing it.

## 2. Why do you need to convert input values using `float()` or `int()`?

The `input()` function always returns text. Even if the user types `10`, Python first reads it as the string `"10"`. If I try to add two strings, Python joins them instead of adding them mathematically. For example, `"10" + "5"` becomes `"105"`, not `15`.

I used `float()` because it converts the input into a number and also allows decimal values. This makes the calculator more flexible than using only `int()`.

## 3. How does your `if`, `elif`, and `else` structure decide which operation to run?

The program checks the value stored in `operator`. If the user chooses `+`, the first `if` block runs and the program adds the numbers. If the user chooses `-`, `*`, or `/`, one of the `elif` blocks runs. If the user enters something else, the `else` block runs and shows an invalid operation message.

## 4. How does your program handle division by zero?

The program checks whether `right_number == 0` inside the division block. If the second number is zero, it prints an error message and does not divide. This prevents the program from crashing.

## 5. How does your program handle an invalid operation?

If the user enters an operation that is not `+`, `-`, `*`, or `/`, the final `else` block runs. It prints a clear message telling the user which operations are allowed.

## 6. Which part of your code shows that you understand the task?

The division part shows my understanding because I did not only write the normal calculation. I also handled the special case where the second number is zero. I think the use of `float()` also shows that I understand the difference between user input as text and numbers used for arithmetic.
