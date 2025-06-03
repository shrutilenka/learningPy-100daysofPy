import random
from hangman_words import word_list

print("Welcome to the Hangman game!")

selected_word = random.choice(word_list)
word_length = len(selected_word)
print(f"The word has {word_length} letters")

letter_positions = {}
for index, letter in enumerate(selected_word):
    if letter not in letter_positions:
        letter_positions[letter] = []
    letter_positions[letter].append(index)

display_word = ["_"] * word_length
print(display_word)
lives = word_length
guessed_letters = set()

while lives > 0 and "_" in display_word:
    guess = input("\nGuess a letter: ").lower().strip()

    if len(guess) != 1:
        print("Please enter exactly one character.")
        continue
    if not guess.isalpha():
        print("Please enter an alphabetic character.")
        continue
    if guess in guessed_letters:
        print("You've already guessed this letter.")
        continue

    guessed_letters.add(guess)

    if guess in letter_positions:
        print("Correct!")
        for position in letter_positions[guess]:
            display_word[position] = guess
    else:
        print("Wrong guess!")
        lives -= 1
        print(f"Lives remaining: {lives}")

    print(display_word)

if "_" not in display_word:
    print("Congratulations! You won!")
else:
    print(f"Game over! You lost. The word was: {selected_word}")
