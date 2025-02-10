class BruteForce:
    def __init__(self, message):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.message = message


    def decrypt(self,message, key):
        message = self.message
        message = message.upper()
        decrypted_message = ""

        for char in message:
            if char == ' ':
                decrypted_message += char
            else:
                try:
                    position = self.alphabet.index(char.upper())
                    new_position = (position - key) % 26
                    new_char = self.alphabet[new_position]
                    if key == 13 and new_char == ' ':
                        decrypted_message += ' '
                except Exception:
                    print('Error!')
                else:
                    decrypted_message += new_char

        print(f"[{key}] {decrypted_message}")



    def run(self):
        for key in range(26):
            self.decrypt(self.message, key)

        print("\n\nFinished")


