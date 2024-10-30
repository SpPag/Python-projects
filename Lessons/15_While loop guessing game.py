# ok so let's make a guessing game.

character_class = "Acolyte"
guessed_character_class = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guessed_character_class != character_class and not out_of_guesses:
    if guess_count < guess_limit:
        guessed_character_class = input("What class am I playing?")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sadly, you lose. Better luck next time.")
else:
    print("You win")
