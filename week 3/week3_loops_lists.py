# Week 3 - Loops and Lists
# Number List Analyzer

numbers = [5, -2, 0, 10, -7, 3]

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

# Go through each number in the list
for number in numbers:
    total_sum = total_sum + number

    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

print("Numbers:", numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
print("Sum:", total_sum)
