# Week 7 Optional Challenge
# Handle missing file with try and except

def analyze_file(file_name, keyword):
    try:
        with open(file_name, "r") as file:
            text = file.read()

        lines = text.splitlines()
        words = text.split()

        keyword_count = 0
        for word in words:
            if word.lower() == keyword.lower():
                keyword_count = keyword_count + 1

        summary = ""
        summary = summary + "File analyzed: " + file_name + "\n"
        summary = summary + "Lines: " + str(len(lines)) + "\n"
        summary = summary + "Words: " + str(len(words)) + "\n"
        summary = summary + "Keyword '" + keyword + "': " + str(keyword_count) + "\n"

        print(summary)

        with open("output.txt", "w") as output:
            output.write(summary)

        print("Summary saved to output.txt")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name.")


analyze_file("sample.txt", "python")
