import random
moves = {
    "Holy church has this": "CROSS",
    "Something chipmunks eat":"NUT",
    "Even a pirate has this": "HOOK",
    "Best move to make by a boxer": "UPPERCUT",
}
lives = 6
hint, word = random.choice(list(moves.items()))
blank = ['_'] * len(word)
clean = ''.join(blank)

user = input('Before anything else input your name. ').title()
print(f'Welcome to the hangman game {user}!\n'
      f'Hey {user}! Ready to test your vocabulary?\n'
      f'In Hangman, you have to guess the secret word\n'
      f'one letter at a time before you run out of attempts and the drawing is complete.\n'
)

while lives > 0 and '_' in blank:
    print(
        f'Hint for secret word: {hint},\n'
        f'Letters in hidden word: {' '.join(blank)}\n'
        f'Your remaining lives: {lives}\n'
    )

    guess = input("Guess a letter inside this hidden word: ").upper().strip()

    if lives == 2:
        print(f'Warning! One life left.\n')
    elif len(guess) != 1 or not guess.isalpha():
        print('Invalid guess! One letter only')
        continue

    found_match = False
    for i in range(len(word)):
        if guess == word[i]:
            blank[i] = guess
            found_match = True

    if not found_match:
        lives -= 1
    elif '_' not in blank:
        print("Congratulations! You've fully filled the letters")
