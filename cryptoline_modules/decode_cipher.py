# used for matching
import re
# rot13
import codecs
# base64
import base64
# type hints
from typing import List, Tuple
# verifying english
from cryptoline_modules import detect_english


def decode_multilayer(cipher_list: List[Tuple[str, str]], max_layers: int, printed_results = []):
    # cipher_list is List[(ciphertext, origination)]
    # max_layers is the number of times the method can call itself recursively
    # printed_results optional argument that allows for printing each answer once
    """Used to solve nested layers of ciphers"""

    results = []
    # runs each ciphertext through a decoding method, and appends the method to ciphertext[1]
    for ciphertext in cipher_list:
        results.append((decode_base85(ciphertext[0]), ciphertext[1] + " => Base85 Decode"))
        results.append((decode_base64(ciphertext[0]), ciphertext[1] + " => Base64 Decode"))
        results.append((decode_base32(ciphertext[0]), ciphertext[1] + " => Base32 Decode"))
        results.append((decode_base16(ciphertext[0]), ciphertext[1] + " => Base16 Decode"))
        results.append((decode_rot13(ciphertext[0]),  ciphertext[1] + " => Rot13 Decode"))
        results.append((decode_mirror(ciphertext[0]), ciphertext[1] + " => Mirror Decode"))
        results.append((decode_morse(ciphertext[0]),  ciphertext[1] + " => Morse Decode"))
        results.append((decode_number_as_phone(ciphertext[0]),  ciphertext[1] + " => Phone Decode"))
        results.append((decode_number_as_letter(ciphertext[0]),  ciphertext[1] + " => Number Decode"))

    # removes blank strings
    results = list(filter(None, results))

    # prints possible decoded text and the decoding methods used
    for possible_match in results:
        if detect_english.has_english(possible_match[0]) and possible_match[0] not in printed_results:
            print(f'{possible_match[0]}: {possible_match[1]}')
            printed_results.append(possible_match[0])

    if max_layers > 0:
        decode_multilayer(results, max_layers - 1, printed_results)


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
    """Used to detect base64"""
    return detect_english.has_english(decode_base64(cipher))


def decode_base32(cipher: str):
    """Used to solve a layer of base32"""
    try:
        return base64.b32decode(cipher).decode("utf-8")
    except:
        return ""


def is_base32(cipher: str):
    """Used to detect base32"""
    return detect_english.has_english(decode_base32(cipher))


def decode_base16(cipher: str):
    """Used to solve a layer of base16"""
    try:
        return base64.b16decode(cipher).decode("utf-8")
    except:
        return ""


def is_base16(cipher: str):
    """Used to detect base16"""
    return detect_english.has_english(decode_base16(cipher))


def decode_base85(cipher: str):
    """Used to solve a layer of base85"""
    try:
        return base64.a85decode(cipher).decode("utf-8")
    except:
        return ""


def is_base85(cipher: str):
    """Used to detect base85"""
    return detect_english.has_english(decode_base85(cipher))


def decode_mirror(cipher: str):
    """Flips the ciphertext. eg. tac => cat """
    return cipher[::-1]


def is_mirror(cipher: str):
    """used to detect mirrored cipher text"""
    return detect_english.has_english(decode_mirror(cipher))


def decode_morse(cipher: str):
    """Can decode well behaved morse"""
    result = ""
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                  '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
                  '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K',
                  '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
                  '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
                  '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
                  '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                  '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                  '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?',
                  '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}

    try:
        for i in cipher.split(" "):
            result = result + morse_dict[i]
    except:
        return result

    return result


def is_morse(cipher: str):
    """Can detect well behaved morse"""
    return detect_english.has_english(decode_morse(cipher))


def decode_binary(cipher: str):
    """Used to solve a layer of binary"""
    # TODO binary machine broke
    try:

        print("good ol go at it sport")
    except:
        return ""
    print("here comes the binary ninja")


def is_binary(cipher: str):
    """Used to detect binary"""
    # TODO see decode_binary(), should function once written
    return detect_english.has_english(decode_binary(cipher))


def decode_number_as_phone(cipher: str):
    """Decodes phone number encoding, eg. 222-2-8 => cat"""
    # todo make werk

    string_result = ""

    # uses the number pad value to lookup the letter

    phone_dict = {'222': 'c', '22': 'b', '2': 'a',
                  '333': 'f', '33': 'e', '3': 'd',
                  '444': 'g', '44': 'h', '4': 'i',
                  '555': 'l', '55': 'k', '5': 'j',
                  '666': 'o', '66': 'n', '6': 'm',
                  '7777': 's', '777': 'r', '77': 'q', '7': 'p',
                  '888': 'v', '88': 'u', '8': 't',
                  '9999': 'z', '999': 'y', '99': 'x', '9': 'w'
                  }

    not_letter = re.compile('[-._|]')
    replaced = re.sub(not_letter, ' ', cipher)

    for item in replaced.split(" "):
        if item in phone_dict:
            string_result = string_result + phone_dict[item]

    return string_result


def decode_number_as_letter(cipher: str):
    """Decodes numbers as letters", eg. 1 2 3 => A B C"""
    string_result = ""

    letter_dict = {'1': 'a', '2': 'b', '3': 'c',
                   '4': 'd', '5': 'e', '6': 'f',
                   '7': 'g', '8': 'h', '9': 'i',
                   '10': 'j', '11': 'k', '12': 'l',
                   '13': 'm', '14': 'n', '15': 'o',
                   '16': 'p', '17': 'q', '18': 'r',
                   '19': 's', '20': 't', '21': 'u',
                   '22': 'v', '23': 'w', '24': 'x',
                   '25': 'y', '26': 'z',
                   }

    not_letter = re.compile('[-._|]')
    replaced = re.sub(not_letter, ' ', cipher)

    for item in replaced.split(" "):
        if item in letter_dict:
            string_result = string_result + letter_dict[item]

    return string_result


def decode_ascii_as_letter(cipher: str):
    print("ascii decode")


def decode_ceaser(cipher: str):
    print("ceaser")


class Letter(object):
    """Used for shifting the values of letters for custom ceaser shifts"""

    def shift(self, value: int):
        """Shifts the value of the letter by the specified value"""

