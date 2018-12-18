from cryptoline_modules import detect_english
from cryptoline_modules import  decode_cipher as dc


def main():
    print("Welcome to cryptoline")
    print("Enter a cryptogram to decode")

    print("CryptoLine> ", end=" ")
    entry = input()
    if dc.is_rot13(entry):
        print(dc.decode_rot13(entry))

    # str(detect_english.is_word(input()))


if __name__ == '__main__':
    main()
