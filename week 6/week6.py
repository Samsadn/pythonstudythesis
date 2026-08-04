# Week 6 - Strings and Dictionaries
# Moderate participant sample

sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase so repeated words match
sentence = sentence.lower()

# Split the sentence into separate words
words = sentence.split()

# Dictionary for counting word frequency
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

print("Word counts:")

for word in word_counts:
    print(word + ":", word_counts[word])

# Student grade dictionary
student_grades = {
    "Sara": "A",
    "Ali": "B",
    "Maria": "C"
}

print()
print("Student grades:")

for student in student_grades:
    print(student + ":", student_grades[student])
