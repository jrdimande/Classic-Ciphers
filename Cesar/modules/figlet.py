from art import text2art
from colorama import Fore

def art(text, fontstyle='contrast'):
    ascii_art = text2art(text, font=fontstyle)
    print(Fore.BLUE + ascii_art)
