# Week 8 - Final Withdrawal and Transfer Test
# Moderate participant sample
# Completed without ChatGPT or external help

def classify_result(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"


students = {
    "Anna": 82,
    "Erik": 58,
    "Sara": 91,
    "Omar": 73
}

# Calculate average score
total_score = 0

for score in students.values():
    total_score = total_score + score

average_score = total_score / len(students)

# Find highest and lowest score
highest_student = ""
highest_score = 0

lowest_student = ""
lowest_score = 100

for student, score in students.items():
    if score > highest_score:
        highest_score = score
        highest_student = student

    if score < lowest_score:
        lowest_score = score
        lowest_student = student

# Print summary
print("Students:", ", ".join(students.keys()))
print()
print("Average score:", round(average_score, 1))
print("Highest score:", highest_student, "-", highest_score)
print("Lowest score:", lowest_student, "-", lowest_score)
print()

for student, score in students.items():
    result = classify_result(score)
    print(student + ":", result)
