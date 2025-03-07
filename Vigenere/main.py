def Run():
    from Cesar.modules import figlet
    from Vigenere.modules.vigenere import cipher

    figlet.art("Vigenere Cipher")
    print("Press '0' any time to quit!!")

    def encrypty(message, key):
        result = cipher.encrypt(message, key)
        print(f"Your Message is now encrypted\n"
              f"Encrypted [Message]: {result}.\n")

    def decrypt(message, key):
        result = cipher.decrypt(message, key)
        print(f"Your Message is now decrypted\n\n"
              f"Decrypted Message: {result}.\n")

    def check_key(key):
        for char in key:
            if char in list("123456789"):
                invalid_key = True
                return invalid_key

        return False

    flag = True

    while flag:
        print("=========================================================================================================")
        print("=> [1] Encrypt Message   [3] Exit <=\n"
              "=> [2] Decrypt Message")
        print("=========================================================================================================")
        option = input()
        if option == '0':
            break

        # Encrypt Messages
        match option:
            case '1':
                message = input("Enter Message: ")
                key = input("Enter key: ")
                check = check_key(key)

                # While key is invalid try again
                while check:
                    print("Key should not contain any digits (1-9).")
                    key = input("Enter a valid key: ")
                    check = check_key(key)

                    if check == False:
                        decrypt(message, key)

                encrypty(message, key)

            case '2':
            # Decrypt Message
                message = input("Enter Message: ")
                key = input("Enter key: ")
                check = check_key(key)

                while check:
                    print("Key should not contain any digits (1-9).")
                    key = input("Enter a valid key: ")
                    check = check_key(key)

                    if check == False:
                        decrypt(message, key)
                decrypt(message, key)
            case  '3':
                break
            case _:
                print("Invalid option!")




