# Week 7 - File Handling and Mini-Program Design
# Moderate participant sample

def count_keyword(text, keyword):
    # Count how many times the selected keyword appears
    words = text.lower().split()
    keyword = keyword.lower()
    count = 0

    for word in words:
        if word == keyword:
            count = count + 1

    return count


# File names
input_file = "sample.txt"
output_file = "output.txt"
keyword = "python"

# Read the file
with open(input_file, "r") as file:
    text = file.read()

# Count lines
lines = text.splitlines()
line_count = len(lines)

# Count words
words = text.split()
word_count = len(words)

# Count selected keyword
keyword_count = count_keyword(text, keyword)

# Create summary text
summary = ""
summary = summary + "File analyzed: " + input_file + "\n"
summary = summary + "Lines: " + str(line_count) + "\n"
summary = summary + "Words: " + str(word_count) + "\n"
summary = summary + "Keyword '" + keyword + "': " + str(keyword_count) + "\n"

# Print summary
print(summary)

# Write summary to output file
with open(output_file, "w") as file:
    file.write(summary)

print("Summary saved to", output_file)
