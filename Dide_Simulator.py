# / ------------------------------------------------------------------------------------ \ #
#   This code was created using the Python language and works in versions 3.12 and higher
# \ ------------------------------------------------------------------------------------ / #


import random
import os

from typing import Literal

type DiceType = Literal['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

dices_available: tuple[str, ...] = ('d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100')


def get_rolls(dice_faces: DiceType, quantity: int = 1, /) -> int | tuple[int, ...]:
    return tuple(random.randint(1, int(dice_faces[1:])) for _ in range(quantity)) if quantity != 1 else\
        random.randint(1, int(dice_faces[1:]))


if __name__ == '__main__':
    
    while True:

        print("Enter the number of times the dice will be rotated and the type of dice desired,"
              " separated by a space. (Ex.: \"5 d20\", \"2 d4\", \"d10\", etc ...)\n")
        print("Types of Dices Available: (d4, d6, d8, d10, d12, d20, d100)")
        print("Type \"exit\" to close the program.\n")

        dice_and_rolls: str = input(">>> ").strip().lower()

        if dice_and_rolls == "exit":
            os.system('cls')
            break

        try:
            if not (dice_and_rolls.split()[1] in dices_available) or int(dice_and_rolls.split()[0]) < 0:
                print("\nInvalid Input!"
                      " Please provide an entry corresponding to the model present in the examples provided.")
                os.system('pause')
                os.system('cls')
                continue

        except (ValueError, IndexError) as error:
            if dice_and_rolls in dices_available:
                dice: DiceType = dice_and_rolls
                print('\n', "Result: ", get_rolls(dice), '\n', sep='')
                os.system('pause')
                os.system('cls')

            else:
                print("\nInvalid Input!"
                      " Please provide an entry corresponding to the model present in the examples provided.")

                os.system('pause')
                os.system('cls')
                continue
                
        else:
            dice: DiceType
            rolls: int
            dice, rolls = dice_and_rolls.split()[1], int(dice_and_rolls.split()[0])

            print('\n', "Result: ", get_rolls(dice, rolls), '\n', sep='')
            os.system('pause')
            os.system('cls')
