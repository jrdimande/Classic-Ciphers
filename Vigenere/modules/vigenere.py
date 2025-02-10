class CipherVigenere:
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    """Method to encrypt message"""
    def encrypt(self, message, key="abc"):
        encrypted_message = ""
        message = message.upper()
        key = key.upper()
        i = 0

        for char in message:
            if char in self.alphabet:
                position = self.alphabet.index(char)
                key_position = self.alphabet.index(key[i % len(key)])
                new_position = (position + key_position) % 26
                new_char = self.alphabet[new_position]
                encrypted_message += new_char
                i += 1
            else:
                encrypted_message += char

        return encrypted_message

    """Method to decrypt message"""
    def decrypt(self, message, key):
        decrypted_message = ""
        message = message.upper()
        key = key.upper()
        i = 0

        for char in message:
            if char in self.alphabet:
                try:
                    position = self.alphabet.index(char)
                    key_position = self.alphabet.index(key[i % len(key)])
                    new_position = (position - key_position) % 26
                    new_char = self.alphabet[new_position]
                    decrypted_message += new_char
                    i += 1
                except ValueError:
                    print("Error!")
            else:
                decrypted_message += char

        return decrypted_message


cipher = CipherVigenere()


def encrypty(message, key):
    result = cipher.encrypt(message, key)
    print(f"Your Message is now encrypted\n"
          f"Encrypted [Message]: {result}.\n")


def decrypt(message, key):
    result = cipher.decrypt(message, key)
    print(f"Your Message is now decrypted\n\n"
          f"Decrypted Message: {result}.\n")


def check_key(key):
    value = False
    for char in key:
        if char.isnumeric():
            value = True

    return value


