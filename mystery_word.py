import re
import random

print("Welcome to Mystery Word! When prompted for input, please type the first letter of your choice.")
player_consent_str = input("Would you like to guess the word I'm thinking of? Please type (Y)es or (N)o: ").upper()

def get_permission():
    if player_consent_str == "Y":
        start_game = True
        start_game = get_edition(file)
        return start_game

    if player_consent_str == "N":
        start_game = False
        return print("Type quit() or Command-Z plus Return to exit. See you later!")

    if player_consent_str is not "N" or "Y":
        print("Sorry, I don't understand. Please try again: ")
        return player_consent_str

def get_edition(file):
    """Take user edition choice, store in chosen_file, move on to difficulty selection"""
    edition_choice_str = input("Choose an edition: (C)ommon, (A)rchaic, or (P)okemon: ").upper()

    if edition_choice_str == "C":
        chosen_file = "common_words.txt"
        game_cont = get_difficulty(chosen_file)
    return game_cont
    
    if edition_choice_str == "A":
        chosen_file = "archaic_words.txt"
        game_cont = get_difficulty(chosen_file)
    return game_cont
    
    if edition_choice_str == "P":
        chosen_file = "pokemon_edition.txt"
        game_cont = get_difficulty(chosen_file)
    return game_cont

    if edition_choice_str is not "C" or "A" or "P":
        print("We do not have that edition in stock yet. Try another for now: ")
    return get_edition(chosen_file)

def get_difficulty(file):

    level_difficulty_str = input("Choose a difficulty level: (E)asy, (M)edium, or (H)ard? ").upper() 

    if level_difficulty_str == "E" or "EASY":
        char_range = range(4,7)

    elif level_difficulty_str == "M" or "MEDIUM":
        char_range = range(6,9)

    elif level_difficulty_str == "H" or "HARD":
        char_range = range(8, 46)
        #the longest english word is 45 characters
        #it's pneumonoultramicroscopicsilicovolcanoconiosis if anyone cares

    else: 
        print("Sorry, I don't understand. Please try again: ")

    with open(file, "r") as chosen_file:
        word_list = [
            word.upper().strip()
            for word in chosen_file.readlines()
            if len(word.strip()) in char_range
        ]
    return word_list