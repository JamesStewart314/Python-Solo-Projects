# / -------------------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language and works in versions 3.12 and higher - 01/27/2024
# \ -------------------------------------------------------------------------------------------------- / #

import os
import time

from typing import Generator


passwords_file_name: str = "Passwords.txt"


def clear() -> None:
    os.system('cls')


def pause(custom_message: str | None = None, /) -> None:
    if custom_message:
        print(custom_message)
    os.system('pause > nul')


def check_passwords_compatibility(password_1: str, password_2: str, /) -> int:
    
    counter: int = 0

    for char_1, char_2 in zip(password_1, password_2):
        if char_1 == char_2:
            counter += 1
    
    return counter


def check_password_strength(user_password: str, /) -> tuple[str | None, int, int]:
    
    closest_password: str | None
    best_compatibility: int
    return_counter: int
    counter: int = 0

    closest_password, best_compatibility, return_counter = None, 0, 0

    passwords_generator: Generator[str, None, None] = (pw for pw in open(passwords_file_name, 'r'))
    
    for pw in passwords_generator:
        counter += 1
        comparison_result: int = check_passwords_compatibility(user_password, pw.removesuffix('\n'))

        if comparison_result > best_compatibility:
            closest_password, best_compatibility, return_counter = pw.removesuffix('\n'), comparison_result, counter
    
    
    return (closest_password, best_compatibility, return_counter)


if __name__ == '__main__':

    clear()

    user_given_password: str
    user_given_password_size: int

    while True:
        user_given_password = input("Enter a password containing between 4 and 40 characters: \n>>> ").strip().lower()
        user_given_password_size = len(user_given_password)

        if 4 <= user_given_password_size <= 40:
            break
        else:
            if user_given_password_size < 4:
                print("Password too short. Please enter a password of the required length.")
            else:
                print("Password too long. Please enter a password of the required length.")
            
            pause("Press Any Key on Your Keyboard to Continue...")
            clear()


    results: tuple[str | None, int, int] = check_password_strength(user_given_password)

    clear()
    
    if results[0]:

        compatibility_rate: float = results[1] / max(len(results[0]), len(user_given_password))

        # password compatibility below 50% and is not inside another password:
        if compatibility_rate < 0.5 and results[0].find(user_given_password) == (-1):

            print("✅ !!! Your Password is \033[32mStrong\033[0m !!! ✅\n")
            print("\033[3mResults obtained during Analysis with the Database\033[0m: ")

            print(f"● Password Provided: {user_given_password}")
            print(f"● Nearest Password Found: {results[0]} (Position: #{results[2]})")
            print(f"● Maximum Compatibility Rate: {str(compatibility_rate * 100)[:5]}%")
            print(f"\nYou Made a Great Password! 😄")
        
        # password compatibility below 75%:
        elif compatibility_rate < 0.75:

            print("⚠️ !!! Your Password is \033[33mAverage\033[0m !!! ⚠️\n")
            print("\033[3mResults obtained during Analysis with the Database\033[0m: ")

            print(f"● Password Provided: {user_given_password}")
            print(f"● Nearest Password Found: {results[0]} (Position: #{results[2]})", end=' ')

            if results[0].find(user_given_password) != (-1) and user_given_password != results[0]:
                print("(Your Password is Inside Another!)")
            else:
                print()

            print(f"● Maximum Compatibility Rate: {str(compatibility_rate * 100)[:5]}%")
            print(f"\nYou Made a Nice Password! But be Careful... 🤔")
        
        # password compatibility above 75%:
        else:

            print("❌ !!! Your Password is \033[31mBad\033[0m !!! ❌\n")
            print("\033[3mResults obtained during Analysis with the Database\033[0m: ")

            print(f"● Password Provided: {user_given_password}")
            print(f"● Nearest Password Found: {results[0]} (Position: #{results[2]})", end=' ')

            if results[0].find(user_given_password) != (-1) and user_given_password != results[0]:
                print("(Your Password is Inside Another!)")
            else:
                print()

            print(f"● Maximum Compatibility Rate: {str(compatibility_rate * 100)[:5]}%")
            print(f"\nFor Your Security, I Recommend That You Try Creating a New Password... 😥")
    
    else:
        # unique password
        print("⚜️⚜️⚜️ !!! Your Password is \033[35mUnique\033[0m !!! ⚜️⚜️⚜️\n")
        print("\033[3mResults obtained during Analysis with the Database\033[0m: ")

        print(f"● Password Provided: {user_given_password}")
        print(f"● Nearest Password Found: {results[0]}")
        print(f"● Maximum Compatibility Rate: \033[1mNo Password Came Even Close!\033[0m")
        print(f"\nYou Made a Wonderful Password, I'm Even Surprised!!! 🥳")


    pause("\nPress Any Key on Your Keyboard to End the program. Thanks for Using!!!")
    
    for i in range(3, 0, -1):
        print(f"Closing in {i}...", end='\r')
        time.sleep(1)
    clear()
