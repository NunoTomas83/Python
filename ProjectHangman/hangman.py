import json
import random
import os
import string

""" The hangman game where the user tries to guess the word
by entering a letter at a time.
"""


def get_random_word():
    """ Function to select a random word from the json file
    and returns the selected word. """
    with open("words.json") as json_file:
        # print(word_file.read())
        data_in_file = json.load(json_file)
    my_list = []
    for word in data_in_file["data"]:
        my_list.append(word)

    random_word = random.choice(my_list)
    # print("random word is: {}".format(random_word))
    return random_word.upper()

# Deprecated function
"""def remove_chars(original_string, chars_to_remove):
    # Function to remove unwanted characters from the string
    # and returns the original string with the new format.

    for char in chars_to_remove:
        original_string = original_string.replace(char, "")
    # print(original_string)
    return original_string"""


def hangman():
    """ Function to run the game. """
    word = get_random_word()
    # print(word)
    word_letter = set(word)  # Letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters used

    lives = 5  # magic number, it can be set any number

    # User input
    while len(word_letter) > 0 and lives > 0:
        # Show used letters until the moment
        print("You have used these letters: ", " ".join(used_letters))

        # Current word shown
        word_list = [letter if letter in used_letters else "#" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1  # user loses a life
                print("Letter is not in the word and you just lost 1 life!")

        elif user_letter in used_letters:
            print("Already tried that letter!")

        else:
            print("Invalid guess!")

    if lives == 0:
        print("You lost and were hanged! The correct word was: {}".format(word))
    else:
        print("Congratulations! You guessed the {} word.". format(word))


if __name__ == '__main__':
    hangman()
