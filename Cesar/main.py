from modules.cesar import check_key, encrypt, decrypt
from modules.brute_force import BruteForce
from modules.figlet import art

print("Press '0' any time to quit!!")
art("Caesar Cipher")

# Main function
def main():
    flag = True

    while flag:
        print("=========================================================================================================")
        print("=>  [1] Encrypt Message                                                                                 =\n"
              "=>  [2] Decrypt Message                                                                                  =\n"
              "=>  [3] Brute Force                                                                                      =\n"
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
            art('Brute Force')
            message = input("Enter Message: ")
            if message == '0':
                flag = False

            brute = BruteForce(message)
            brute.run()

        else:
            if option == '0':
                flag = False


main()