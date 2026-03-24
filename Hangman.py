import random
moves = {
    "Holy church has this": "CROSS",
    "Something chipmunks eat":"NUT",
    "Even a pirate has this": "HOOK",
    "Best move to make by a boxer": "UPPERCUT",
}
lives = 6
hint, word = random.choice(list(moves.items()))
blank = ["_"] * len(word)
clean = "_".join(blank)
guessed = set()

while lives > 0 and '_' in blank:
    print(f'Current life: {lives}\n'
          f'The hint for the word {hint}\n'
          f'Word contains {" ".join(blank)}\n'
    )
    if lives == 1:
        print('You have 1 life remaining!')

    guess = input('Input your guess letter one only: ').strip().upper()

    found_match = False
    if len(guess) != 1 or not guess.isalpha():
        print(f'Enter a valid char!\n')
        continue


    for i in range(len(word)):
        if guess == word[i]:
            found_match = True
            blank[i] = guess
    if not found_match:
        lives -= 1

    if guess in guessed:
        print(f"That's guessed already\n")

    guessed.add(guess)

if not '_' in blank:
    print('Congratulations!')
else:
    print('You lost :<')
