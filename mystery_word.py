import user_selections 

def restart(get_permission):

def play_game(word):
    guesses = ""
    chances: 8

    while chances > 0:
        failed = 0

        for letter in word:
            if letter in guesses:
                print(letter)
            else:
                print("_")
                failed += 1

            if failed == 0:
                print("You did it!")

            guesses = input("Guess a letter: ")
            total_guesses += guesses
                