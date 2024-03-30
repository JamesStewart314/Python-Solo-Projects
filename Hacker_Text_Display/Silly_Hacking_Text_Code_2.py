# / -------------------------------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 02/02/2024
#
#                            This is the second version of "Silly Hacking Text Code",
#            where I try to display the text directly in the terminal in a smoother and more fluid way,
#   without oscillations between the time interval during the display of characters and vibrations in the terminal,
#                                         with a box to cover the text.
#
#                   I am aware that the code does not work as expected for very large sentences.
#             This is a problem that I will try to solve in the next version of this naive code idea ^^
# \ -------------------------------------------------------------------------------------------------------------- / #

import itertools
import os
import string
import random
import time

from itertools import count

os.system('cls')  # To Clear the Terminal Before Starting the Program
text = input("Entry Some Text to See Something Nice: \n>>> ")  # Text that will be Displayed in a Very Cool Way ;)

delay_time: int | float = 0.01  # Determining the interval time in seconds between displaying random characters
number_of_characters_drawn: int = 4  # Number of Random Characters Generated Between each Letter
symbols_used: list[str] = list(string.ascii_letters + string.digits + string.punctuation)  # Possible Symbols to be Displayed During the Character Draw

os.system('cls')  # To Clear the Terminal
os.system('color 0A')  # Changing the Text Color to Green

aux_counter: count = itertools.count(start=1)  # Auxiliary Contactor to Determine the Quantity of Upper and Lower Intermediate Lines

word_printed: str = ""  # Word Displayed in Terminal After Each Iteration

for letter in text:
    
    word_printed += letter  # Reconstructing the Original Text

    upperline_quantity: int = next(aux_counter)

    print('╔═', '═' * upperline_quantity, '══╗', sep='')
    print('║ ', end='')

    print(word_printed, end='')

    for _ in range(number_of_characters_drawn):
        print(random.choice(symbols_used), end='\b')
        time.sleep(delay_time)

    print('   ║')
    print('╚═', '═' * upperline_quantity, '═══╝', sep='')

    # This is where the trick lies!
    # The ANSI code "\033[<lines>A" is responsible for backtracking lines in the terminal,
    # making it possible to reformat texts already displayed!!!
    # For example, the command "print('\033[1A', end='')" would go back one line.

    print('\033[3A', end='')

# Cleaning the Last Box Without os.system('cls') :
for _ in range(3):
    print(' ' * (len(text) + 6))

# Displaying the Last Box with the Original Printed Text :
print('\033[3A', end='')
print('╔═', '═' * len(text), '═╗', sep='')
print('║', text, '║')
print('╚═', '═' * len(text), '═╝', sep='')

print("\n\n Press Any Key to End the Program.")
os.system('pause > nul')  # Pauses the Terminal Without Showing any Text
os.system('cls')  # Clears the Terminal Before Finishing
os.system('color 07')  # Restoring the Terminal's Default Aesthetic Settings


# Less efficient workaround :

"""
os.system('cls')
upperline_quantity: int = next(aux_counter)
print('╔═', '═' * upperline_quantity, '═╗', sep='')
print('║ ', end='')
print('t', ' ║', sep='')
print('╚═', '═' * upperline_quantity, '═╝', sep='')
"""
