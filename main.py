import Cesar.main as cae
from  Cesar.modules.figlet import art
import Vigenere.main as vig

art("CipherLock", 'tarty')

while True:
    print("=========================================================================================================")
    print("=> [1] Vigenere [3] INFO <= \n"
          "=> [2] Caesar   [4] Exit <=")
    print("=========================================================================================================")

    option = input("")

    match option:
        case '1':
            vig.Run()
        case '2':
            cae.Run()
        case '3':
            print()
        case '4':
            break
        case _:
           print("Invalid option!")