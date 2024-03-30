# /--------------------------------------------------------------------------------------------------------\
#  This code is an interactive Rock Paper Scissors game created in Python language - version 3.12 or higher
#
#                          I emphasize that this script was created for Windows,
#              which means it won't work properly on other operating systems like Linux and MacOS
#                                       Code Created in ~ 01/18/2024 ~
# \--------------------------------------------------------------------------------------------------------/ #

import msvcrt
import time
import os
import random


def getchar() -> bytes:
    return msvcrt.getch()


def clear() -> None:
    os.system('cls')


def play_the_game() -> None:

    clear()
    
    print(' ' * 30, "!!! Lets Play Rock, Paper and Scissors !!!\n")

    user_name: str = input("What's your Name?  >>> ").strip().lower().capitalize()[:9]  # Name of 10 characters

    while not user_name.isalpha():
        clear()
        print(' ' * 30, "!!! Lets Play Rock, Paper and Scissors !!!\n")
        print("Invalid Name! Please, input a name just of letters.")
        user_name: str = input("What's your Name?  >>> ").strip().lower().capitalize()[:9]  # Name of 10 characters


    def rock_paper_scissors() -> None:
        
        nonlocal user_name

        option_change_cooldown_time: float = 0.5
        ai_play_cooldown: float = 2.0

        draw_text: str = "DRAW"
        win_text: str = "YOU WON"
        lost_text: str = "YOU LOST"

        options_to_play: tuple[str, str, str] = ("Rock", "Paper", "Scissors")
        
        options_index: int = 0
        current_option: str = random.choice(options_to_play)
        option_change_time: float = time.time()

        ai_current_option: str = ""

        players_played: list[bool] = [False, False]

        option_change: bytes

        while True:

            clear()

            print(' ' * 30, "!!! Lets Play Rock, Paper and Scissors !!!\n")

            print(f"Nice to meet you, {user_name}!")

            print("Navigate between the options pressing \"a\" or \"d\" and choose pressing \"ENTRER\" in your keyboard.",
                "To close the game, just press \"ESC\"...\n")

            # -------------------------------------------- USER INTERFACE -------------------------------------------- #

            print(' ' * 10, '<<< ', end='')

            match current_option:
                case "Rock":
                    print('\033[32m', end='')
                case "Paper":
                    print('\033[33m', end='')
                case "Scissors":
                    print('\033[34m', end='')
                case _:
                    print('\033[0m', end='')

            print(f"{current_option:^20}\033[0m >>>", end='')

            # --------------------------------------------- AI INTERFACE --------------------------------------------- #

            if players_played[0] and not players_played[1]:
                ai_current_option = random.choice(options_to_play)

            print(' ' * 15, end='')

            print('<<<', end='')

            match ai_current_option:
                case "Rock":
                    print('\033[32m', end='')
                case "Paper":
                    print('\033[33m', end='')
                case "Scissors":
                    print('\033[34m', end='')
                case _:
                    print('\033[0m', end='')
            
            print(f"{ai_current_option:^20}\033[0m >>> ")

            # ------------------------------------------- NAMES OF THE PLAYERS ------------------------------------------- #

            print(' ' * 16, r'\\', f"{user_name:^10}", '//', ' ' * 22, r'\\', "Polaris (my AI)", '//')

            if not players_played[0]:
                option_change = getchar()
            else:
                if time.time() - ai_play_cooldown < 5:
                    time.sleep(0.2)
                else:
                    players_played[1] = True

            try:

                if option_change.decode().lower() == 'd' and (time.time() - option_change_time) >= option_change_cooldown_time and not players_played[0]:
                    option_change_time = time.time()
                    options_index = (options_index + 1) % 3
                    current_option = options_to_play[options_index]
                
                elif option_change.decode().lower() == 'a' and (time.time() - option_change_time) >= option_change_cooldown_time and not players_played[0]:
                    option_change_time = time.time()
                    options_index = (options_index - 1) % 3
                    current_option = options_to_play[options_index]
                
                elif option_change == b'\x1b' and (time.time() - option_change_time) >= option_change_cooldown_time:

                    print()
                    
                    for i in range(3, -1, -1):
                        print("Thanks for playing!!! Closing in", i, '...', end='\r')
                        time.sleep(1)

                    clear()
                    return None

                elif option_change == b'\x0d' and current_option in options_to_play and not players_played[0]:
                    players_played[0] = True
                    ai_play_cooldown = time.time()

            except UnicodeDecodeError as error:
                pass
            
            if players_played[0] and players_played[1]:
                game_result: tuple[str, str] = (current_option, ai_current_option)

                print(" " * 37, end='')

                if game_result[0] == game_result[1]:
                    print(f"!!! {draw_text:^11} !!!")
                elif (game_result[0] == "Paper" and game_result[1] == "Rock") or (game_result[0] == "Rock" and game_result[1] == "Scissors") or (game_result[0] == "Scissors" and game_result[1] == "Paper"):
                    print(f"!!! {win_text:^11} !!!")
                elif (game_result[0] == "Paper" and game_result[1] == "Scissors") or (game_result[0] == "Rock" and game_result[1] == "Paper") or (game_result[0] == "Scissors" and game_result[1] == "Rock"):
                    print(f"!!! {lost_text:^11} !!!")
                
                print("\nDo you wanna play again? ;) [Y]es // [N]o")

                option_change = b'\x0d'

                try:

                    while option_change.decode().lower() not in ("y", "n"):
                        option_change = getchar()

                    match option_change.decode().lower():
                        case "y":
                            return rock_paper_scissors()
                        case "n":

                            print()
                    
                            for i in range(3, -1, -1):
                                print("Thanks for playing!!! Closing in", i, '...', end='\r')
                                time.sleep(1)

                            clear()
                            return None
                
                except UnicodeDecodeError as error:
                    pass

    return rock_paper_scissors()



if __name__ == "__main__":
    play_the_game()
