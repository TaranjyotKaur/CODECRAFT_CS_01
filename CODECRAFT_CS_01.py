def caesar_cipher(text, shift, mode):
    result = ""

    # If decrypting, reverse the shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine ASCII base (A-Z or a-z)
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Shift character with wrap-around using modulo
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Keep spaces, numbers, symbols unchanged
            result += char

    return result


def main():
    print("=== Caesar Cipher Program ===")
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))
    
    mode = input("Type 'encrypt' or 'decrypt': ").lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode selected!")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult: {output}")


if __name__ == "__main__":
    main()