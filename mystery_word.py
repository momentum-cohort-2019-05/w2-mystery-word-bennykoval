import re
import random

print("Welcome to Mystery Word!")
player_consent = input("Would you like to guess the word I'm thinking of? Please type (Y)es or (N)o: ").lower()
level_difficulty_str = input("Choose a difficulty level: (E)asy, (M)edium, or (H)ard? ").lower() 
print("Good luck!")

def player_consent(word):
    if player_consent == "n":
        return exit()
    
    if player_consent == "y":
        return level_difficulty_str
    
    else: 
        print("Sorry, I don't understand. Please try again: ")

def get_difficulty(word):

    if level_difficulty_str == "e" or "easy":
        return range(4,7)

    if level_difficulty_str == "m" or "medium":
        return range(6,9)

    if level_difficulty_str == "h" or "hard":
        return range(8, 46)
        #the longest english word is 45 characters
        #it's pneumonoultramicroscopicsilicovolcanoconiosis if anyone cares


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

with open(file) as chosen_file:
    word_freq = print_word_freq(chosen_file.read())
    for word, freq in word_freq[:31]:
        print(word, '|', freq, "*" * freq)