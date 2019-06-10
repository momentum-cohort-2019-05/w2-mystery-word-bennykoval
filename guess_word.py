import re
import random

def get_permission():
    """Get user's permission to play game; if not, terminate"""
    print("Welcome to Mystery Word! When prompted for input, please type the first letter of your choice.")
    player_consent_str = input("Would you like to guess the word I'm thinking of? Please type (Y)es or (N)o: ").upper()

    if player_consent_str == "Y":
        start_game = get_edition()
        return start_game

    if player_consent_str == "N":
        return input("Press any key to escape. See you later!")

    if player_consent_str is not "N" or "Y":
        print("Sorry, I don't understand. Please try again: ")
        return get_permission()

def get_edition():
    """Take user edition choice, store in chosen_file, move on to difficulty selection"""
    edition_choice_str = input("Choose an edition: (C)ommon, (A)rchaic, or (P)okemon: ").upper()

    edition_choice_list = ["C", "A", "P"] 

    if edition_choice_str == "C":
        chosen_file = "common_words.txt"
        return get_difficulty(chosen_file)
    
    if edition_choice_str == "A":
        chosen_file = "archaic_words.txt"
        return get_difficulty(chosen_file)
    
    if edition_choice_str == "P":
        chosen_file = "pokemon_edition.txt"
        return get_difficulty(chosen_file)

    if edition_choice_str is not edition_choice_list:
        print("We do not have that edition in stock yet. Try another for now: ")
        return get_edition()

def play_game(word):
    """Compare guesses to word, display chances left, display win/loss"""
    chances = 8
    display_guess = []
    wrong_guess = []

    letter_list = [*word]
    print(letter_list)
    # format_underscore = ("_" * len(letter))
    #bananas 
    #letter_list = [*"bananas"]
    #['b', 'a', 'n', 'a', 'n', 'a', 's']
    #chances = 8

    while chances > 0:

        guess = input("Guess a letter: ").upper()

        if guess in letter_list:
            display_guess.append(guess)
            print("display guess: ", display_guess)
            print("guess: ", guess)
            
        else:
            wrong_guess.append(guess)
            (print_word(word, display_guess))
            chances -= 1
            print(chances, " more guesses remaining!")

        if chances == 0:
            print(word, " was your word. Sorry!")
            return get_permission()

        elif word == display_guess:
            print("You did it!")
            return get_permission()

#def print_word(letter, guess):
    #if letter in guess:
        #return letter
    #else:
        #return "_"
#[print_word(letter, display_guess)
 #for letter in word]

def get_difficulty(file):
    """Get user difficulty choice, list letter range in accordnance"""
    level_difficulty_str = input("Choose a difficulty level: (E)asy, (M)edium, or (H)ard? ").upper() 

    if level_difficulty_str == "E":
        letter_range = range(4,7)

    elif level_difficulty_str == "M":
        letter_range = range(6,9)

    elif level_difficulty_str == "H":
        letter_range = range(8, 46)
        #the longest english word is 45 characters
        #it's pneumonoultramicroscopicsilicovolcanoconiosis if anyone cares

    else: 
        print("Sorry, I don't understand. Please try again: ")
        return get_difficulty(file)

    with open(file, "r") as chosen_file:
        word_list = [
            word.upper().strip()
            for word in chosen_file.readlines()
            if len(word.strip()) in letter_range
        ]
    word = random.choice(word_list)
    print(word)
    return play_game(word)

def print_word(word, display_guess):
    output_letters = []
    for letter in word:
        output_letters.append(display_letter(letter, display_guess))
    print(" ".join(output_letters))

def display_letter(letter, display_guess):
    if letter in display_guess:
        return letter
    else:
        return "_"

get_permission()