# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 01/28/2024
# \ ----------------------------------------------------------------------------------------- / #

import string
import time
import itertools
import os

from typing import Generator, Callable
from itertools import count


str_has_digits: Callable[[str], bool] = lambda x: bool(set(x).intersection(set(string.digits)))
str_has_symbols: Callable[[str], bool] = lambda x: bool(set(x).intersection(set(string.punctuation)))


def clear() -> None:
    os.system('cls')


def pause(custom_message: str | None = None, /) -> None:
    if custom_message:
        print(custom_message)
    os.system('pause > nul')


def common_guess(unknown_password: str, /) -> int | None:
    
    passwords_generator: Generator[str, None, None] = (pw.removesuffix('\n') for pw in open("Passwords.txt", 'r'))
    counter: count = itertools.count(start=1)

    temp_counter: int

    for pw in passwords_generator:
        temp_counter = next(counter)
        if unknown_password == pw:
            return temp_counter
    
    return None


def crack_password(unknown_password: str, /, time_limit: int | float = 120.0, *, digits: bool = False, symbols: bool = False) -> tuple[bool | None, str, float, int]:

    """

       Guess a password based on its length and a search timeout provided by the user. 
     Searches involving more complex passwords with numerals and symbols can also be requested using the "digits" and "symbols" parameters, respectively.
     I will only consider passwords with lowercase characters to avoid exorbitant search complexity.

     :param password: The password the user would like to crack.
     :param time_limit: Timeout in seconds for password cracking attempts.
     :param digits: Specifies whether the search should include digits in the password search.
     :param symbols: Informs whether the search should also cover special symbols.

     :return: Tuple containing a boolean or 'None' value indicating whether the password has been discovered ('True' if it has been, 'False' otherwise and 'None' if reached time limit without discovering the password),
     a string with the unknown password, a floating point value representing the time taken to crack the password and and the number of attempts made to discover the password.

    """

    if time_limit < 1.0:  # Less than 1 sec
        raise Exception("Very short time to discover the password.")
    
    if not unknown_password.isascii():  # Password contains non ascii characters
        raise Exception("This code only discovers passwords involving ASCII characters.")

    characters_in_search: str = string.ascii_lowercase

    if digits:
        characters_in_search += string.digits
    if symbols:
        characters_in_search += string.punctuation
    
    list_of_characters_in_search: list[str] = list(characters_in_search)

    search_timer: float = time.time()

    # First performing a search for trivial passwords in a database :
    if tries := common_guess(unknown_password):
        return (True, unknown_password, round(time.time() - search_timer, 2), tries)
    
    # Then tries brute force:
    passwords_generator: Generator[str, None, None] = (''.join(pw) for pw in itertools.product(list_of_characters_in_search, repeat=len(unknown_password)))
    counter: count = itertools.count(start=10 ** 7)  # Considering the previous execution of all attempts present in the password database.

    for temp_password in passwords_generator:
        # print(temp_password, end='\r')  # Just uncomment this line for fun purposes, it slows down the code A LOT...
        temp_counter = next(counter)
        if unknown_password == temp_password:
            return (True, temp_password, round(time.time() - search_timer, 2), temp_counter)
        
        if time.time() - search_timer > time_limit:
            return (False, unknown_password, round(time.time() - search_timer, 2), temp_counter)
    
    return (None, unknown_password, round(time.time() - search_timer, 2), temp_counter)


if __name__ == '__main__':

    clear()

    user_given_password: str
    user_given_password_size: int

    while True:

        try:

            user_given_password = input("Enter a password containing between 4 and 40 ascii characters (lower alphabetic cases, digits and symbols): \n>>> ").strip().lower()
            user_given_password_size = len(user_given_password)

            if not 4 <= user_given_password_size <= 40:
                if user_given_password_size < 4:
                    raise Exception("Password too short. Please enter a password of the required length.")
                else:
                    raise Exception("Password too long. Please enter a password of the required length.")

        except Exception as error:
            
            print(error)
            pause("Press Any Key on Your Keyboard to Continue...")
            clear()
        
        else:
            break  # User provided the correct input

    clear()
    
    search_time: int | float

    while True:

        print(f"Enter a password containing between 4 and 40 ascii characters (lower alphabetic cases, digits and symbols): \n>>> {user_given_password}")
        
        try:

            search_time = eval(input("\nWhat should be the time limit (in seconds) to search for the password? \n>>> "))

            if search_time < 1.0:
                raise Exception()
        
        except Exception as error:

            print("\nThe search time must be an positive integer or float number greater than or equal than 1 second.")
            pause("Press Any Key on Your Keyboard to Continue...")
            clear()
        
        else:
            break # User provided the correct input


    clear()

    print("Processing Your Password...\n")

    final_results: tuple[bool | None, str, float, int] = crack_password(user_given_password, search_time,
                                                         digits=str_has_digits(user_given_password), 
                                                         symbols=str_has_symbols(user_given_password))
    
    print("Final Results: \n")
    
    if final_results[0] != None:

        if final_results[0]:

            print("The Password has been Discovered \033[32mSuccessfully\033[0m!")
            print(f"● Password Required: {final_results[1]}")
            print(f"● Time Required to Crack the Password: {final_results[2]} seconds")
            print(f"● Attempts made: {final_results[3]:,}")

        else:  # Reached timeout without discovering password
            
            print("The Password was not Discovered During the Search Time...")
            print(f"● Password Required: {final_results[1]}")
            print(f"● Time Required to Crack the Password: {final_results[2]} seconds")
            print(f"● Attempts made: {final_results[3]:,}")
    
    else:  # The password was not discovered even after all possible attempts
        
        print("Unable to Identify Password Even after all Attempts...")
        print(f"● Password Required: {final_results[1]}")
        print(f"● Time Required to Crack the Password: {final_results[2]} seconds")
        print(f"● Attempts made: {final_results[3]:,}")

    pause("\nPress Any Key to Close the Program...")
    clear()
