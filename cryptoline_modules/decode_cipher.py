# rot13
import codecs
# base64
import base64
# verifying english
from cryptoline_modules import detect_english

# this prints stuff to console instead of doing it "properly", but like man I tried
def decode_multilayer(cipher_list: "string list", max_layers: int):
    """Used to solve nested layers"""
    results = []
    # I really don't know a better way to do this
    for cipher in cipher_list:
        results.append(decode_base85(cipher))
        results.append(decode_base64(cipher))
        results.append(decode_base32(cipher))
        results.append(decode_base16(cipher))
        results.append(decode_mirror(cipher))

    # removes blank strings
    results = list(filter(None, results))

    for possible_match in results:
        if detect_english.has_english(possible_match):
            print(possible_match)

    if max_layers > 0:
        decode_multilayer(results, max_layers - 1)


def decode_layer(cipher: str):
    """Used to solve a single layer cipher"""
    # before multiple outputs is added, ordered to minimize false positives

    if is_base64(cipher):
        return decode_base64(cipher)
    if is_base32(cipher):
        return decode_base32(cipher)
    if is_base16(cipher):
        return decode_base16(cipher)
    if is_base85(cipher):
        return decode_base85(cipher)
    if is_mirror(cipher):
        return decode_mirror(cipher)
    if is_rot13(cipher):
        return decode_rot13(cipher)

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
    """Used to solve a layer of binary"""
    return detect_english.has_english(decode_base16(cipher))


def decode_base85(cipher: str):
    try:
        return base64.a85decode(cipher).decode("utf-8")
    except:
        return ""


def is_base85(cipher: str):
    return detect_english.has_english(decode_base85(cipher))


def decode_binary(cipher: str):
    # TODO binary machine broke
    try:

        print("good ol go at it sport")
    except:
        return ""
    print("here comes the binary ninja")


def is_binary(cipher: str):
    """Used to solve a layer of binary"""
    # TODO see decode_binary() should function once written
    return detect_english.has_english(decode_binary(cipher))


def decode_mirror(cipher: str):
    """Flips the ciphertext. eg. tac => cat """
    return cipher[::-1]


def is_mirror(cipher: str):
    return detect_english.has_english(cipher)





def decode_morse():
    print("morsy mo")
