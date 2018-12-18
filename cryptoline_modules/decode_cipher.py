import codecs
from cryptoline_modules import detect_english


def decode_rot13(cipher: str):
    return codecs.decode(cipher, 'rot_13')


def is_rot13(cipher: str):
    return detect_english.has_english(decode_rot13(cipher))

