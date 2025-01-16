from click import option

from cesar import  cipher
import pyfiglet


text = "Cesar Cipher"
ascii_art = pyfiglet.figlet_format(text, font="slant")
print(ascii_art)
print("Press '0' any time to quit!!")

# Encrypt messages
def encrypt(message, key):
        result = cipher.encrypt(message, int(key))
        print(f"Your Message is now encrypted\n"
 
              f"Encrypted [Message]: {result}.\n")
# Decrypt messages
def decrypt(message, key):
    result = cipher.decrypt(message, int(key))
    print(f"Your Message is now decrypted\n\n"
          f"Decrypted Message: {result}.\n")

# Check if key is valid
def check_key(key):
    if key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']:
        return False
    else:
        return True



# main function
def main():
    flag = True

    while flag:
        print("=========================================================================================================")
        print("[1] Encrypt Message\n"
              "[2] Decrypt Message")

        option = input()

        if option == '1':
            message = input("Enter Message: ")
            key =input("Enter key: ")
            valid_key = check_key(key)

            while valid_key:
                key = input("Enter valid key: ")
                valid_key = check_key(key)

            encrypt(message, key)

        elif option == '2':
            message = input("Enter Message: ")
            key = input("Enter key: ")
            valid_key = check_key(key)

            while valid_key:
                key = input("Enter valid key: ")
                valid_key = check_key(key)

            decrypt(message, key)






main()