import random

from debugpy.launcher.output import wait_for_remaining_output

words = [
    "clarity", "momentum", "build", "vision", "impact",
    "focus", "resilience", "flow", "growth", "create",
    "iterate", "trust", "craft", "design", "solve",
    "adapt", "scale", "align", "push", "connect"
]

selected_word = random.choice(words)
print(selected_word)
word_count = len(selected_word)
letter_list = []
print(f"Guess the right letter of the {word_count}letter word to save your little man")
for count in range(word_count):
    letter_list.append(selected_word[count])
guessed_letter = ""
score = 0
num = word_count

while num >0:
    guessed_letter = input("Enter the letter \n")
    for letters in letter_list:
        if letters == guessed_letter:
            score += 1
            print("Correct guess!")
    num -= 1

if score == word_count:
    print(f"score={score}, word count ={word_count}")
    print("You won!")
else:
    print(f"score={score}, word count ={word_count}")
    print("you lost!")