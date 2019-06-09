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
        return print("See you later!")

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

def get_difficulty(file):

    level_difficulty_str = input("Choose a difficulty level: (E)asy, (M)edium, or (H)ard? ").upper() 

    if level_difficulty_str == "E":
        char_range = range(4,7)

    elif level_difficulty_str == "M":
        char_range = range(6,9)

    elif level_difficulty_str == "H":
        char_range = range(8, 46)
        #the longest english word is 45 characters
        #it's pneumonoultramicroscopicsilicovolcanoconiosis if anyone cares

    else: 
        print("Sorry, I don't understand. Please try again: ")
        return get_difficulty(file)

    with open(file, "r") as chosen_file:
        word_list = [
            word.upper().strip()
            for word in chosen_file.readlines()
            if len(word.strip()) in char_range
        ]
    word = random.choice(word_list)
    print(word)
    return word_list

get_permission()

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