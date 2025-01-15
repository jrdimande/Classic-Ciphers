import pyfiglet
from vigenere import cipher


text = "Vigenere Cipher"
ascii_art = pyfiglet.figlet_format(text, font="slant")
print(ascii_art)
print("Press '0' any time to quit!!")

def main():
    flag = True

    while flag:
        print("=========================================================================================================")
        print("[1] Encrypt Message\n"
              "[2] Decrypt Message")

        option = input()

        if option == '1':
            message = input("Enter Message: ")
            key = input("Enter key: ")
            result = cipher.encrypt(message, key)
            print(f"Your Message is now encrypted\n"
                  f"Encrypted [Message]: {result}.\n")

        elif option == '2':
            message = input("Enter Message: ")
            key = int(input("Enter key: "))
            result = cipher.decrypt(message, key)
            print(f"Your Message is now decrypted\n\n"
                  f"Decrypted Message: {result}.\n")
        else:
            if option == '0':
                break
            else:
                print("Invalid Input try again!")




main()

