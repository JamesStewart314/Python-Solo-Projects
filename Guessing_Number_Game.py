# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 or higher - 01/17/2024
# \ ----------------------------------------------------------------------------------------- / #


import random
import os
import time

from typing import Literal

type YesOrNo = Literal['Y', 'N']
type Colors = Literal['Yellow', 'Blue', 'Red', 'Green', 'Normal']

colors_dict: dict[str, str] = dict(Yellow='\033[33m', Blue='\033[34m', Red='\033[31m', Green='\033[32m',
                                   White='\033[37m', Normal='\033[0m')


def clean() -> None:
    os.system('cls')


def pause() -> None:
    os.system('pause')


def presentation() -> None:
    clean()
    print('\t' * 2 + "            Welcome to the")
    print('\t' * 2 + "      \\_______________________/")
    print('\t' * 2 + "    ~ | \033[3m\033[01mGuessing Number Game\033[0m | ~")
    print('\t' * 2 + "      /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\\\n")

    print("Please, insert two different integer numbers to be the"
          " \033[01mupper\033[0m and \033[01mlower\033[0m bound of the game,\nin any order that you prefer:\n")


def get_user_input(input_text: str, input_color: Colors) -> str:
    return input(f"● \033[4m{colors_dict.get(input_color, colors_dict['Normal'])}{input_text}{colors_dict['Normal']} Number >>> ").strip()


def get_yes_or_no(optional_message: str | None = None, /) -> YesOrNo:

    user_answer: str = input('>>> ').strip().upper()

    while user_answer not in ('Y', 'N'):
        clean()
        print("Invalid Answer! Select between \"Y\" or \"N\".")

        if optional_message:
            print(optional_message)

        user_answer = input('>>> ').strip().upper()

    return user_answer


def get_user_integer_number(input_text: str = '', input_color: Colors = 'Normal', clean_screen: bool = True, /) -> int:

    new_number: str = get_user_input(input_text, input_color)

    while not (new_number.isnumeric() or (new_number[0] == '-' and new_number[1:].isnumeric())):
        if clean_screen:
            clean()
        print("\nNope, invalid choice, try some integer number. (Ex.: \"-23\", \"89\", ...)\n")
        pause()
        print()
        new_number = get_user_input(input_text, input_color)

    if int(new_number) < 0:
        new_number: int = int(new_number)
        new_number: str = '(' + str(new_number) + ')'

    print(f"\nYour selected number is {colors_dict.get(input_color, colors_dict['Normal'])}{new_number}{colors_dict.get('Normal')}."
          f" Are you sure about that? [Y]es / [N]o\n")

    if new_number[0] == '(':
        new_number = new_number[1:-1]

    user_answer: YesOrNo = get_yes_or_no(f"\nYour selected number is "
                                         f"{colors_dict.get(input_color)}{new_number}{colors_dict.get('Normal')}."
                                         f" Are you sure about that? [Y]es / [N]o\n")

    if user_answer == 'N':
        print()
        return get_user_integer_number(input_text, input_color)

    return int(new_number)


def number_guess() -> int:

    new_number: str = input("● \033[3mChoose an Integer Number\033[0m >>> ").strip()

    while not (new_number.isnumeric() or (new_number[0] == '-' and new_number[1:].isnumeric())):
        print("\nNope, invalid choice, try some integer number. (Ex.: \"-23\", \"89\", ...)\n")
        pause()
        print()
        new_number = input("● \033[3mChoose an Integer Number\033[0m >>> ").strip()

    return int(new_number)


def game() -> None:

    presentation()

    first_number: int = get_user_integer_number("First", 'Yellow')

    print("\nNice! Now please insert another integer to get the number guessing game boundary:\n")

    second_number: int = get_user_integer_number("Second", 'Blue')

    boundary: int = abs(max(first_number, second_number) - min(first_number, second_number))

    clean()

    user_answer: YesOrNo = 'N'

    while boundary > 1000 and user_answer == 'N':

        minimum_number: int = min(first_number, second_number)
        maximum_number: int = max(first_number, second_number)

        aux_number_1: str = str(minimum_number) if minimum_number >= 0 else '(' + str(minimum_number) + ')'
        aux_number_2: str = str(maximum_number) if maximum_number >= 0 else '(' + str(maximum_number) + ')'

        print(f"Your Boundary "
              f"({colors_dict['Green']}{aux_number_1} -> {aux_number_2}{colors_dict['Normal']})"
              f" is \033[1mtoo big\033[0m ({colors_dict['Red']}over 1000{colors_dict['Normal']})."
              f"\nAre you sure you want to play with these limits? [Y]es / [N]o\n")

        user_answer = get_yes_or_no()

        if user_answer == 'N':
            print(f"What number you want to change?"
                  f" {colors_dict['Yellow']}[F]irst Number{colors_dict['Normal']} /"
                  f" {colors_dict['Blue']}[S]econd Number{colors_dict['Normal']}")

            user_answer: str = input(">>> ").strip().upper()

            while user_answer not in ('F', 'S'):

                print("Invalid Choice! Please select between \"F\" of \"S\":")

                user_answer: str = input(">>> ").strip().upper()

            match user_answer:
                case 'F':
                    first_number = int(get_user_integer_number("First", 'Yellow'))
                case 'S':
                    second_number = int(get_user_integer_number("Second", 'Blue'))

    # __________________________________________________ THE GAME __________________________________________________ #

    drawn_number: int = random.randint(min(first_number, second_number), max(first_number, second_number))

    guessed_number: int = drawn_number - 100

    minimum_number = min(first_number, second_number)
    maximum_number = max(first_number, second_number)

    aux_number_1 = str(minimum_number) if minimum_number >= 0 else '(' + str(minimum_number) + ')'
    aux_number_2 = str(maximum_number) if maximum_number >= 0 else '(' + str(maximum_number) + ')'

    last_guess: int | None = None

    while guessed_number != drawn_number:

        clean()

        print(f"Guessing Limit: {aux_number_1} <---> {aux_number_2}", end='')

        if last_guess:
            print("\t(Last Guess: ", last_guess, ")", sep='')
        else:
            print()

        print("Try to guess what is the drawn number: ", end='')

        if abs(drawn_number - guessed_number) <= 10:
            print("(C'mon, you're close!)\n")
        else:
            print('\n')

        guessed_number = number_guess()

        if guessed_number != drawn_number:
            estimate: str = "\033[1mGreater\033[0m" if drawn_number > guessed_number else "\033[1mLower\033[0m"
            print("\nWrong Guess! The unknown number is", estimate, "than your guess...")
            pause()

        last_guess = guessed_number

    print(f"\n\033[1mYou {colors_dict['Yellow']}W{colors_dict['Blue']}o{colors_dict['Red']}n{colors_dict['Normal']}!!!"
          f"\n\nThe unknown number was {drawn_number}. Wanna play again? [Y]es / [N]o")

    user_answer = get_yes_or_no()

    if user_answer == "Y":
        game()

    for i in range(3, -1, -1):
        print("Thanks for Coming!!! Closing in", i, '...', end='\r')
        time.sleep(1)

    clean()

    return None


if __name__ == "__main__":
  game()
