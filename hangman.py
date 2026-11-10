import random

def hangman():
    words = ["python", "codealpha", "internship", "developer", "hangman"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    lives = 6
    guessed_letters = []

    print("=== CodeAlpha Hangman Game ===")
    print(f"Word: {' '.join(guessed)}")

    while lives > 0 and "_" in guessed:
        guess = input(f"\nLives: {lives} | Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed!")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print(f"Correct! Word: {' '.join(guessed)}")
        else:
            lives -= 1
            print(f"Wrong! Word: {' '.join(guessed)}")

    if "_" not in guessed:
        print(f"\nYou Won! The word was: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

# Intern: FAISUL HAMEER AFANA | ID: CA/DF1/434642
hangman()
