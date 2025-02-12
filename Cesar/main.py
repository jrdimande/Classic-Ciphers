# Main function
def Run():
    from Cesar.modules.cesar import cipher
    from Cesar.modules.brute_force import BruteForce
    from Cesar.modules.figlet import art
    from Cesar.modules.cesar import encrypt, decrypt
    from modules.utils import check_key

    art("Caesar Cipher")
    print("Press '0' any time to quit!!")
    flag = True

    while flag:
        print("=========================================================================================================")
        print("=> [1] Encrypt Message   [3] Brute Force <=\n"
              "=> [2] Decrypt Message   [4] Quit        <=\n"
              "=========================================================================================================")

        option = input()

        match option:
        # Encrpyt
            case '1':
                print("=========================================================================================================")
                print("++++++++++++++++++++++++++++++++++ Encrypt Messages +++++++++++++++++++++++++++++++++++++++++++++++++++++")

                message = input("Enter Message: ")
                if message == '4':
                    flag = False
                key =input("Enter key: ")
                if key == '4':
                    flag = False
                valid_key = check_key(key)

                while valid_key:
                    key = input("Enter valid key: ")
                    if key == '4':
                        flag = False
                    valid_key = check_key(key)

                encrypt(message, key)
                print("=========================================================================================================")


            # Decrypt
            case '2':

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
            case '3':
                art('Brute Force')
                message = input("Enter Message: ")
                if message == '0':
                    flag = False

                brute = BruteForce(message)
                brute.run()
            # Quit
            case '4':
                    flag = False
            case _:
                print("Invalid option!")

