# Week 6 Optional Challenge - Remove simple punctuation

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

# Remove commas and periods before splitting
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")

words = sentence.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

print("Word counts:")

for word in word_counts:
    print(word + ":", word_counts[word])
