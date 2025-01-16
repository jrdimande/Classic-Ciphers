from cesar import  cipher
from brute_force import BruteForce
import pyfiglet


text = "Cesar Cipher"
ascii_art = pyfiglet.figlet_format(text, font="big")
print(ascii_art)
print("Press '0' any time to quit!!")

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
    if key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']:
        return False
    else:
        return True



# Main function
def main():
    flag = True

    while flag:
        print("=========================================================================================================")
        print("=   [1] Encrypt Message                                                                                 =\n"
              "=   [2] Decrypt Message                                                                                 =\n"
              "=   [3] Brute Force                                                                                     =\n"
              "=========================================================================================================")

        option = input()

        # Encrpyt
        if option == '1':
            print("=========================================================================================================")
            print("++++++++++++++++++++++++++++++++++ Encrypt Messages +++++++++++++++++++++++++++++++++++++++++++++++++++++")

            message = input("Enter Message: ")
            if message == '0':
                flag = False
            key =input("Enter key: ")
            if key == '0':
                flag = False
            valid_key = check_key(key)

            while valid_key:
                key = input("Enter valid key: ")
                if key == '0':
                    flag = False
                valid_key = check_key(key)

            encrypt(message, key)
            print("=========================================================================================================")


        # Decrypt
        elif option == '2':

            print("=========================================================================================================")
            print("++++++++++++++++++++++++++++++++++ Decrypt Messages +++++++++++++++++++++++++++++++++++++++++++++++++++++")
            message = input("Enter Message: ")
            if message == '0':
                flag = False
            key = input("Enter key: ")
            if key == '0':
                flag = False
            valid_key = check_key(key)

            while valid_key:
                key = input("Enter valid key: ")
                if key == '0':
                    flag = False
                valid_key = check_key(key)

            decrypt(message, key)
            print("=========================================================================================================")

        # Brake Cipher
        elif option == '3':
            text = "Brute Force"
            ascii_art = pyfiglet.figlet_format(text, font="big")
            print(ascii_art)
            message = input("Enter Message: ")
            if message == '0':
                flag = False

            brute = BruteForce(message)
            brute.run()

        else:
            if option == '0':
                flag = False







main()