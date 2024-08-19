import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

game_over = False

guessedLetters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessedLetters.append(guess)
        elif letter in guessedLetters:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        game_over = True

    print(f"display:{display}")

