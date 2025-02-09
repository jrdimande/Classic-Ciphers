class CipherCesar:
    def __init__(self, key = 3):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        self.key = key

    """ Method to encrypt message """
    def encrypt(self, message, key = 3):
        encrypted_message = ""
        message = message.upper()

        try:
            for char in message:
                if char == ' ':
                    encrypted_message += char
                position = self.alphabet.index(char)
                new_position = (position + key) % 26
                new_char = self.alphabet[new_position]
                encrypted_message += new_char

        except ValueError:
            print(f"An error ocurred while trying to encrypt message [{message}], please check if the message contains only letters")

        return encrypted_message


    """ Method to decrypt messages """
    def decrypt(self, message, key = 3):
        message = message.upper()
        decrypted_message = ""

        try:
            for char in message:
                if char == ' ':
                    decrypted_message += char
                else:
                    position = self.alphabet.index(char.upper())
                    new_position = (position - key) % 26
                    new_char = self.alphabet[new_position]
                    decrypted_message += new_char



        except ValueError:
            print(f"An error ocurred while trying to decrypt message [{message}], please check if the message contains only letters")

        return decrypted_message

cipher = CipherCesar()
# Functiont to Encrypt messages
def encrypt(message, key):
    result = cipher.encrypt(message, int(key))
    print(f"Your Message is now encrypted\n"

          f"[Message]: {result}.\n")


# Function to Decrypt messages
def decrypt(message, key):
    result = cipher.decrypt(message, int(key))
    print(f"Your Message is now decrypted\n\n"
          f"Message: {result}.\n")


# Function to Check if key is valid
def check_key(key):
    if key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
               '19', '20', '21', '22', '23', '24', '25']:
        return False
    else:
        return True



