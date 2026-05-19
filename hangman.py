import random

words = ["python", "computer", "hangman", "programming", "developer"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

display_word = ["_"] * len(word)

while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input")
        continue

    if guess in guessed_letters:
        print("Already guessed")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print("Correct")
    else:
        wrong_guesses += 1
        print("Wrong")

if "_" not in display_word:
    print("You won")
    print("Word:", word)
else:
    print("You lost")
    print("Word:", word)
