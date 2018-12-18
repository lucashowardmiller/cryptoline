"""Used to classify if certain strings are words or contain words"""
import re


def has_english(string: str):
    """Detects if a string (seperated by spaces) has a word"""

    not_letter = re.compile('[^0-9a-zA-Z]+')
    string = not_letter.sub(' ', string)

    for item in string.split(" "):
        if item in load_words():
            return True
    return False


def is_word(word: str):
    """If a string is a word, returns True, else False"""
    return word.lower() in load_words()


def load_words():
    """Loads the words document intop a set"""
    with open('cryptoline_modules/words.txt') as word_file:
        valid_words = set(word_file.read().lower().split())

    return valid_words