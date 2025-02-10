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
        print("=> [1] Encrypt Message\n"
              "=> [2] Decrypt Message")
        print("=========================================================================================================")
        option = input()
        if option == '0':
            break

        # Encrypt Messages
        if option == '1':
            message = input("Enter Message: ")
            if message == '0':
                break

            key = input("Enter key: ")
            invalid_key = check_key(key)

            while invalid_key:
                print("Key should not contain any digits (1-9).")
                key = input("Enter a valid key: ")

                invalid_key = False
                for char in key:
                    if char in "123456789":
                        invalid_key = True
                        break

            encrypty(message, key)

        # Decrypt Messages
        elif option == '2':
            message = input("Enter Message: ")
            if message == '0':
                break

            key = input("Enter key: ")
            if key == '0':
                break
            invalid_key = check_key(key)

            # While key is invalid prompt key again
            while invalid_key:
                print("Key should not contain any digits (1-9).")
                key = input("Enter a valid key: ")
                if key == '0':
                    decrypt(message, key)
                    break






Run()
