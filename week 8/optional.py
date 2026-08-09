# Week 8 Optional Challenge
# Sorted ranking from highest to lowest score
# Completed without ChatGPT or external help

students = {
    "Anna": 82,
    "Erik": 58,
    "Sara": 91,
    "Omar": 73
}

ranking = []

for student, score in students.items():
    ranking.append((student, score))

ranking.sort(key=lambda item: item[1], reverse=True)

print("Ranking:")

position = 1

for student, score in ranking:
    print(str(position) + ".", student, "-", score)
    position = position + 1
