import random
words = {
    "Keeps the doctor away": "APPLE",
    "Monkey's favorite": "BANANA",
    "Something to drink": "GRAPE",
}
lives = 6
random_hint = random.choice(list(words.keys()))
random_word = words[random_hint]
blank = ["_"] * len(random_word)
clean_blank = " ".join(blank)

while lives > 0 and '_' in blank:
    print(
        f'The secret hint is "{random_hint}",\n'
        f'{clean_blank}\n'
        f'Your current life remaining: {lives}'
    )
    found = False

    user_input = input("Enter your guess here: ").upper().strip()
    if len(user_input) != 1:
        print("That's not a valid guess. It should be one character only")
    for i, letter in enumerate(random_word):
        if user_input == letter:
            blank[i] = letter
            found = True
    clean_blank = " ".join(blank)
    if not found:
        lives -= 1
print(f'Done the correct word is: {random_word}')