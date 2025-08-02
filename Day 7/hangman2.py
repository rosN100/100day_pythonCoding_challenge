import random
words = [
    "clarity", "momentum", "build", "vision", "impact",
    "focus", "resilience", "flow", "growth", "create",
    "iterate", "trust", "craft", "design", "solve",
    "adapt", "scale", "align", "push", "connect"
]
selected_word = random.choice(words)
print(selected_word)

word_count = len(selected_word)
# print(word_count)

selected_word_list = []
spaces =""
for letter in range(word_count):
    selected_word_list.append(selected_word[letter])
    spaces += "_"
print(spaces)

# print(selected_word_list)



