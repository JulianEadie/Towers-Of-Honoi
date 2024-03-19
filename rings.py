import os
from colorama import Fore
from enum import Enum

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def starting_menu():
    print("Welcome to:")
    clear_screen()
    print(Fore.RED + 'Tower of Honoi')
    clear_screen()

class RINGS(Enum):
    ONE_RING = 1
    TWO_RING = 2
    THREE_RING = 3

def get_user_choice():
    print("How many rings would you like?: ")
    for rings in RINGS:
         print(f"{rings.value}. {rings.name.replace('_', ' ').title()}")

    if get_user_choice > 3:
        print("Please choose a number thats less than 3")

def more_interactive():
    print(f"You chose to have {rings.value}" )
    clear_screen()
    print(Fore.RED + 'processing your choice')
    clear_screen()
    print(Fore.RED + 'Almost done')
    clear_screen()

n = get_user_choice

def equation():
    2 * n - 1

def lowest_possible_moves():
    equation()
    return equation()

def find_lowest_amount_of_moves():
    elif get_user_choice == RINGS.ONE_RING:
    more_interactive()
    lowest_possible_moves()
    else:
    get_user_choice == RINGS.TWO_RING:
    more_interactive()
    lowest_possible_moves()
    else get_user_choice == RINGS.THREE_RING:
    more_interactive()
    lowest_possible_moves()



