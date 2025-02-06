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
                position = self.alphabet.index(char)
                key_position = self.alphabet.index(key[i % len(key)])
                new_position = (position - key_position) % 26
                new_char = self.alphabet[new_position]
                decrypted_message += new_char
                i += 1
            else:
                decrypted_message += char

        return decrypted_message


cipher = CipherVigenere()
