from cesar import  cipher
import pyfiglet


text = "Cesar Cipher"
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
            result = cipher.encrypt(message)
            print(f"Your Message is now encrypted\n"
                  f"Encrypted [Message]: {result}.\n")

        elif option == '2':
            message = input("Enter Message: ")
            result = cipher.decrypt(message)
            print(f"Your Message is now decrypted\n"
                  f"Decrypted Message: {result}.\n")
        else:
            if option == '0':
                break
            else:
                print("Invalid Input try again!")




main()

