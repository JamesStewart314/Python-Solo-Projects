# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 01/19/2024
# \ ----------------------------------------------------------------------------------------- / #

import string
import secrets
import os

from typing import Callable


def generate_password(length: int, /, *, symbols: bool = False, uppercase: bool = False) -> str:
    
    """
    The function create a password with symbols, numbers, upper and lower alphabetic characters.

    :param length: Number that informs the desired length of the password.
    :param symbols: Boolean value to specify whether the password must contain special characters,
            such as "\\", ">", "?" etc.
    :param uppercase: Boolean value to indicate whether the password must have uppercase letters.
    :return: The function return a string containing the password based on the criteria specified by the parameters provided in the
             function call.
    """

    if not isinstance(length, int) or length <= 0:
        raise Exception("\"length\" parameter must be an integer positive number greater than zero.")
    if not (isinstance(uppercase, bool) and isinstance(symbols, bool)):
        raise TypeError("\"symbols\" and \"uppercase\" parameters must be boolean type. (\"true\" or \"false\")")

    password_characters: list[str] = list(string.ascii_lowercase + string.digits)

    if symbols:
        password_characters.extend(list(string.punctuation))
    if uppercase:
        password_characters.extend(list(string.ascii_uppercase))
    
    check_uppercase: Callable[[str], bool] = lambda x: any(character in string.ascii_uppercase for character in x)
    check_symbols: Callable[[str], bool] = lambda x: any(character in string.punctuation for character in x)
    
    password_characters_size: int = len(password_characters)

    string_len: int = 0
    new_password: str = ""

    while string_len < length:
        new_password += password_characters[secrets.randbelow(password_characters_size)]
        string_len += 1

    return new_password if ((check_symbols(new_password), check_uppercase(new_password)) == (symbols, uppercase) or length == 1) else\
          generate_password(length, symbols=symbols, uppercase=uppercase)


if __name__ == '__main__':

    import random

    quantity: int = int(input("How many passwords do you want to create? >> "))
    passwords_len = int(input("and what size should they be? >> "))

    check_uppercase: Callable[[str], bool] = lambda x: any(character in string.ascii_uppercase for character in x)
    check_symbols: Callable[[str], bool] = lambda x: any(character in string.punctuation for character in x)

    os.system('cls')
    print("Passwords Generated:\n")

    for order in range(1, quantity + 1):
        password_generated: str = generate_password(passwords_len, symbols=random.choice((True, False)),
                                                    uppercase=random.choice((True, False)))
        print(f"{order}° -> {password_generated} || (Upper: {check_uppercase(password_generated)},"
              f" Sym: {check_symbols(password_generated)})")

    print("\nPress any key to close the program.")
    os.system('pause >nul')
    os.system('cls')
    exit()
