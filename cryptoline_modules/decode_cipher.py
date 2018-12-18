# rot13
import codecs
# base64
import base64
# verifying english
from cryptoline_modules import detect_english


def decode_multilayer(cipher: str, max_layers: int):
    """Used to solve nested layers"""
    print("")


def decode_layer(cipher: str):
    """Used to solve a single layer cipher"""
    if is_rot13(cipher):
        return decode_rot13(cipher)
    if is_base64(cipher):
        return decode_base64(cipher)
    if is_base32(cipher):
        return decode_base32(cipher)
    if is_base16(cipher):
        return decode_base16(cipher)


def decode_rot13(cipher: str):
    """Used to decode rot13"""
    return codecs.decode(cipher, 'rot_13')


def is_rot13(cipher: str):
    """Used to detect rot13"""
    return detect_english.has_english(decode_rot13(cipher))


def decode_base64(cipher: str):
    """Used to solve a layer of base64"""
    try:
        return base64.b64decode(cipher).decode("utf-8")
    except:
        return ""


def is_base64(cipher: str):
    """Used to solve a layer of base64"""
    return detect_english.has_english(decode_base64(cipher))


def decode_base32(cipher: str):
    """Used to solve a layer of base32"""
    try:
        return base64.b32decode(cipher).decode("utf-8")
    except:
        return ""


def is_base32(cipher: str):
    """Used to solve a layer of base32"""
    return detect_english.has_english(decode_base32(cipher))


def decode_base16(cipher: str):
    """Used to solve a layer of base16"""
    try:
        return base64.b16decode(cipher).decode("utf-8")
    except:
        return ""


def is_base16(cipher: str):
    """Used to solve a layer of base16"""
    return detect_english.has_english(decode_base16(cipher))


def decode_ceaser(cipher: str):
    print("cat")

def decode_morse(cipher: str):
    print("morse")
