from cryptoline_modules import decode_cipher as dc


def main():
    print("Welcome to cryptoline")
    print("Enter a cryptogram to decode")

    print("CryptoLine> ", end=" ")
    entry = input()

    print(dc.decode_layer(entry))

    # str(detect_english.is_word(input()))


if __name__ == '__main__':
    main()
