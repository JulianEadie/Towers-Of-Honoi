from colorama import Fore
import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def your_fault():
    print(Fore.RED + 'SO I GUESS OUR RULES WERENT GOOD ENOUGH?')
    clear_screen()
    print(Fore.RED + 'WELL THATS TOO BAD YOU CANT GO BACK NOW')
    clear_screen()
    for i in range(10):
       print(Fore.RED + 'Virus detected in your computer')
    clear_screen()
    print(Fore.RED + 'NEXT TIME CHOOSE YES')
