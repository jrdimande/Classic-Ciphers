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

    if option =='1':
        vig.Run()
    elif option == '2':
        cae.Run()
    elif option == '3':
        print()
    elif option == 4:
        break
    else:
        if option == '4':
            break