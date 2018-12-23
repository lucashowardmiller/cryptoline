"""Used to classify if certain strings are words or contain words"""
# used to eliminate non whitespace separators
import re


def load_words():
    """Loads the words document into a set"""
    with open('cryptoline_modules/words.txt') as word_file:
        valid_words = set(word_file.read().lower().split())

    return valid_words


def has_english(string: str):
    """True if a string (separated by anything) has an english word"""

    WORD_SET = load_words()

    # Replaces all non letter characters with spaces
    not_letter = re.compile('[^0-9a-zA-Z]+')
    string = not_letter.sub(' ', string)

    # Determines if the current section of the string occurs in the word text file
    for item in string.split(" "):
        if item in WORD_SET:
            return True
    return False


def is_word(word: str):
    """If a string is a word, returns True, else False"""
    return word.lower() in load_words()
