# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 01/12/2024
# \ ----------------------------------------------------------------------------------------- / #

import os
import string
import time

symbols: set[str] = set(string.ascii_letters + string.digits + string.punctuation + string.whitespace)

os.system('color a')
os.system('cls')

word: str = input("What Message do You Want to Write? \n>>> ")
os.system('cls')

current_word: str = ''
letter_index: int = 0

while current_word != word:

    for symbol in symbols:
        current_word += symbol
        os.system('cls')
        print(current_word, end='\r')

        if current_word[letter_index] != word[letter_index]:
            current_word: str = current_word[:-1]
            continue
        else:
            letter_index += 1
            break

time.sleep(5)
