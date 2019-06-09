import user_selections 

def play_game(word):
    chances: 8
    guesses = ""
    
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

            if guesses not in word:
                chances -= 1
                print(chances, " more guesses remaining!")

                if chances == 0:
                    print(word, " was your word. Sorry!")
                    get_permission()

                