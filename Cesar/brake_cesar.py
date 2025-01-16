alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
message = input("Enter message: ")


def decrypt(message, key):
    message = message.upper()
    decrypted_message = ""

    for char in message:
        if char == ' ':
            decrypted_message += char
        else:
            position = alphabet.index(char.upper())
            new_position = (position - key) % 26
            new_char = alphabet[new_position]
            if key == 13 and new_char == ' ':
                decrypted_message += ' '
            else:
                decrypted_message += new_char

    print(f"[{key}] {decrypted_message}")


for key in range(26):
    decrypt(message, key)

