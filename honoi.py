from rings import *
from the_forgotten import *
from colorama import Fore
import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def pegs():
    print(Fore.RED + 'THE NUMBER OF PEGS WILL NEVER CHANGE!')
    clear_screen()
    print(Fore.RED + 'THE NUMBER OF PEGS WILL ALWAYS BE THREE PEGS')
    clear_screen()
    print(Fore.RED + 'THE ONLY THING THAT WILL CHANGE IS THE NUMBER OF RINGS')
    clear_screen()
    rules = input(Fore.RED + 'DO YOU UNDERSTAND THESE CONDITIONS? (y/n): ')
    if rules.lower() != "y":
       print(Fore.GREEN + 'Thank you for accepting our conditions!')
       clear_screen()
       rings()
    else:
       the_forgotten()




