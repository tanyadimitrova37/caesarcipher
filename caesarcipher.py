import sys

print("Enter a message: ", end="")
message = input()
print("Enter a shift value between 1 and 25: ", end="")

try:
    shift = int(input())
    if shift < 1 or shift > 25:
        print("Only numbers between 1 and 25 are allowed")
        sys.exit()
except ValueError:
    print("Only integers are allowed")
    sys.exit()


def caesar_sipher(message, shift):
    new_message = ""
    new_char = ""
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            new_char = chr(base + (ord(char) - base + shift) % 26)
        else:
            new_char = char
        new_message += new_char

    return new_message

encrypted_message = caesar_sipher(message, shift)
print(encrypted_message)
