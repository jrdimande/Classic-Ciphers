class CipherCesar:
    def __init__(self, key = 1):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        self.key = key

    """ Method to encrypt message """
    def encrypt(self, message, key = 1):
        encrypted_message = ""


        try:
            for char in message:
                position = self.alphabet.index(char.upper())
                new_position = (position + key) % 26
                new_char = self.alphabet[new_position]
                encrypted_message += new_char

        except ValueError:
            print(f"An error ocurred while trying to encrypt message [{message}], please check if the message contains only letters")

        return encrypted_message

    """ Method to decrypt messages """
    def decrypt(self, message, key = 1):
        message.upper()
        decrypted_message = ""

        try:
            for char in message:
                position = self.alphabet.index(char.upper())
                new_position = (position - key) % 26
                new_char = self.alphabet[new_position]
                decrypted_message += new_char

        except ValueError:
            print(f"An error ocurred while trying to decrypt message [{message}], please check if the message contains only letters")

        return decrypted_message



cipher = CipherCesar()



