# Week 4 Optional Challenge
# Calculate average without external help

numbers = [6, -3, 0, 9, -1, 4]

positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

for number in numbers:
    total_sum = total_sum + number

    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1

average = total_sum / len(numbers)

print("Numbers:", numbers)
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)
print("Sum:", total_sum)
print("Average:", average)
