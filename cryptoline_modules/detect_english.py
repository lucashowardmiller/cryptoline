"""Used to classify if certain strings are words or contain words"""
# used to eliminate non whitespace separators
import re
import sqlite3
import os


def load_words():
    """Loads the words document into a set"""
    with open('cryptoline_modules/words.txt') as word_file:
        valid_words = set(word_file.read().lower().split())

    return valid_words


def has_english(string: str):
    """True if a string (separated by anything) has an english word"""

    # Replaces all non letter characters with spaces
    not_letter = re.compile('[^0-9a-zA-Z]+')
    string = not_letter.sub(' ', string)

    # Determines if the current section of the string occurs in the word text file
    for item in string.split(" "):
        if execute_query_contains(item):
            return True
    return False


def verify_db_file():
    """Will error if db does not exist"""
    try:
        con = sqlite3.connect('file:cryptoline_modules/word_database.db?mode=rw', uri=True)
    except:
        print("Building database (One Time Operation)")
        make_database()
        print("Done")
        return False
    return True


def make_database():
    """One time database creation from words.txt file"""
    db_connection = sqlite3.connect("cryptoline_modules/word_database.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute('DROP TABLE IF EXISTS Words ')
    db_cursor.execute('CREATE TABLE Words (valid_word TEXT)')

    with open('cryptoline_modules/words.txt') as word_file:
        valid_words = set(word_file.read().lower().split())

    for item in valid_words:
        db_cursor.execute('INSERT INTO Words VALUES (?)', (item,))

    db_connection.commit()
    db_connection.close()


def execute_query_contains(uknown_word: str):
    """Returns true if the string is contained within the valid_word """
    db = sqlite3.connect("cryptoline_modules/word_database.db")
    db_cursor = db.cursor()

    db_cursor.execute("SELECT rowid FROM Words WHERE valid_word = ?", (uknown_word.lower(),))

    result = db_cursor.fetchone()

    if result is not None:
        return True
    else:
        return False

    db.close()
