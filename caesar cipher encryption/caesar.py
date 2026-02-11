from art import logo

print(logo)

def caesar(text, shift, direction):
    """Encode or decode `text` by `shift`. Direction is 'encode' or 'decode'."""
    result = ""
    shift = shift % 26
    if direction == 'decode':
        shift = -shift

    for ch in text:
        if ch.isalpha():
            lower = ch.lower()
            idx = ord(lower) - ord('a')
            new_idx = (idx + shift) % 26
            new_char = chr(new_idx + ord('a'))
            result += new_char.upper() if ch.isupper() else new_char
        else:
            result += ch

    print(f"The {direction}d result is: {result}")
    return result


if __name__ == '__main__':
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ('encode', 'decode'):
            print("Please type 'encode' or 'decode'.")
            continue

        text = input("Type your message:\n")
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Shift must be an integer.")
            continue

        caesar(text, shift, direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == 'no':
            should_continue = False
            print('Goodbye')