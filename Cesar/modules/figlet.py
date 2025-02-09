from art import text2art
from colorama import Fore

def art(text):
    ascii_art = text2art(text, font='big')
    print(Fore.BLUE + ascii_art)