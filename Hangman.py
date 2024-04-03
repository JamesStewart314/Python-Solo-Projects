# /---------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Hangman game created in Python language - version 3.12 or higher - with dependencies on the "faker" and "translate" libraries.
#                           To run it properly, make sure you have these libraries in your virtual environment.
#
#  I emphasize that this script was created for Windows, meaning it may not work correctly on other operating systems such as Linux or MacOS.
#
#                               Also, make sure you run this program in a terminal that supports cleaning. 
#                                                  (e.g.: cmd.exe, VSCode terminal, etc.)
#                         Terminals in IDEs like Pycharm will probably not be able to run this script correctly.
#
#                                                     Code Created in ~ 02/01/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------------------------/

import os
import msvcrt
import string
import time

import faker
from translate import Translator

portuguese_translator: Translator = Translator(to_lang='pt')

lower_characters: set[str] = set(string.ascii_lowercase)

en_numbers_translate_dict: dict[int, str] = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
pt_numbers_translate_dict: dict[int, str] = {0: "zero", 1: "uma", 2: "duas", 3: "três", 4: "quatro", 5: "cinco",
                                             6: "seis"}

head: str = '◯'
left_arm: str = '/'
right_arm: str = '\\'
torso: str = '|'
left_leg: str = left_arm
right_leg: str = right_arm


def getchar() -> bytes:
    return msvcrt.getch()


def play_hangman() -> None:
    
    game_lan: str = ''
    
    attempts: int = 6

    letters_guessed: list[str] = []

    user_answer: str = ''
    
    while True:
    
        os.system('cls')
    
        print('\033[1m', '_' * 114, '\033[0m', sep='')
        print("|| Please, select an language to play the Hangman ||"
              " Por favor, selecione um idioma para jogar o Jogo da Forca  ||")
        print('‾' * 114)
        print(' ' * 40, r'\\',
              "\033[4m\033[34m [en] - English\033[37m\033[0m || \033[4m\033[32m[pt] - Portuguese \033[37m\033[0m//",
              sep='')
        print(' ' * 56, ' \\/')
    
        print(' ' * 54, '| ', end='')
    
        if game_lan in ('en', 'pt'):
            if game_lan == 'en':
                print('\033[34m', end='')
            else:
                print('\033[32m', end='')
    
        print(f"{game_lan:^4}", end='')
        print('\033[0m |')  # or "print('\033[0m |', end='\b' * 4)" is better ... ? idk...
    
        user_pressed_key = getchar()
    
        if user_pressed_key == b'\x08' and len(game_lan) > 0:  # User pressed Backspace
            game_lan = game_lan[:-1]
        try:
            if user_pressed_key.decode().lower() in lower_characters and len(game_lan) < 2:
                game_lan += user_pressed_key.decode().lower()
        except UnicodeDecodeError as error:
            pass
    
        if user_pressed_key == b'\x0d':  # User pressed Enter
            if game_lan in ('en', 'pt'):
                break
            else:
                print("\a")  # Sound alert
    
    # ----------------------------------------------------THE GAME---------------------------------------------------- #
    
    drawn_word: str = faker.Faker().word() if game_lan == 'en' else portuguese_translator.translate(faker.Faker().word())

    while len(drawn_word.split()) > 1 or not set(drawn_word).issubset(
            lower_characters):  # to guarantee the draw of just one word
        drawn_word: str = faker.Faker().word() if game_lan == 'en' else portuguese_translator.translate(
            faker.Faker().word())
    
    word_str: str = "Word: " if game_lan == 'en' else "Palavra: "

    number_of_letters: str = f"the word was {len(drawn_word)} letters..." if game_lan == 'en' else f"a palavra possui {len(drawn_word)} letras..."

    already_used_letters_text: str = "Already used letters: " if game_lan == 'en' else "Letras já usadas: "
    
    presentation_message_1: str = "!!! \033[1mWelcome\033[0m to the \033[1mHangman Game\033[0m !!!" if game_lan == 'en' else \
        "!!! \033[1mBem-Vindo\033[0m ao \033[1mJogo da Forca\033[0m !!!"
    
    victory_message: str = "\033[1mCongratulations!\033[0m You have correctly guessed the hidden word." if game_lan == 'en' else\
                           "\033[1mMeus Parabéns!\033[0m Você adivinhou corretamente a palavra oculta."
    
    while True:
    
        os.system('cls')
    
        print('\033[1m', '_' * 114, '\033[0m', sep='')
        print("|| Please, select an language to play the Hangman ||"
              " Por favor, selecione um idioma para jogar o Jogo da Forca  ||")
        print('‾' * 114)
        print(' ' * 40, r'\\',
              "\033[4m\033[34m [en] - English\033[37m\033[0m || \033[4m\033[32m[pt] - Portuguese \033[37m\033[0m//",
              sep='')
        print(' ' * 56, ' \\/')
    
        print(' ' * 54, '| ', end='')
    
        if game_lan in ('en', 'pt'):
            if game_lan == 'en':
                print('\033[34m', end='')
            else:
                print('\033[32m', end='')
    
        print(f"{game_lan:^4}", end='')
        print('\033[0m |')
    
        print(f"{presentation_message_1:^138}")
    
        number_of_attempts: str = en_numbers_translate_dict.get(
            attempts) if game_lan == 'en' else pt_numbers_translate_dict.get(attempts)
    
        if attempts in (5, 6, 7):
            number_of_attempts = '\033[32m' + number_of_attempts + '\033[0m'
        elif attempts in (4, 3, 2):
            number_of_attempts = '\033[33m' + number_of_attempts + '\033[0m'
        else:  # attempts == 1 or 0
            number_of_attempts = '\033[31m' + number_of_attempts + '\033[0m'
    
        game_start_message: str = f"\n● try to guess the word before the gallow is completed, you have {number_of_attempts} attempts:" if game_lan == 'en' else \
            f"\n● tente adivinhar a palavra antes que a forca seja concluída, você tem {number_of_attempts} tentativa(s):"
    
        print(game_start_message)

        match attempts:

            case 6:

                print(
                """        ______|
       /    ||
       |     
       |   
       |   
       |
      / \\
     /___\\
                """)
            
            case 5:

                print("""        ______|
       /    ||
       |    ◯ 
       |   
       |   
       |
      / \\
     /___\\
    """)

            case 4:

                print("""        ______|
       /    ||
       |    ◯ 
       |   /
       |   
       |
      / \\
     /___\\
    """)
            case 3:

                print("""        ______|
       /    ||
       |    ◯ 
       |   /|
       |   
       |
      / \\
     /___\\
    """)
            case 2:

                print("""        ______|
       /    ||
       |    ◯ 
       |   /|\\
       |   
       |
      / \\
     /___\\
    """)
            case 1:

                print("""        ______|
       /    ||
       |    ◯ 
       |   /|\\
       |   /
       |
      / \\
     /___\\
    """)
                
            case 0:
            
                while True:
                    
                    os.system('cls')
        
                    print('\033[1m', '_' * 114, '\033[0m', sep='')
                    print("|| Please, select an language to play the Hangman ||"
                        " Por favor, selecione um idioma para jogar o Jogo da Forca  ||")
                    print('‾' * 114)
                    print(' ' * 40, r'\\',
                "\033[4m\033[34m [en] - English\033[37m\033[0m || \033[4m\033[32m[pt] - Portuguese \033[37m\033[0m//",
                sep='')
                    print(' ' * 56, ' \\/')
        
                    print(' ' * 54, '| ', end='')
        
                    if game_lan in ('en', 'pt'):
                        if game_lan == 'en':
                            print('\033[34m', end='')
                        else:
                            print('\033[32m', end='')
        
                    print(f"{game_lan:^4}", end='')
                    print('\033[0m |')
        
                    print(f"{presentation_message_1:^138}")
        
                    number_of_attempts: str = en_numbers_translate_dict.get(
                        attempts) if game_lan == 'en' else pt_numbers_translate_dict.get(attempts)
        
                    if attempts in (5, 6, 7):
                        number_of_attempts = '\033[32m' + number_of_attempts + '\033[0m'
                    elif attempts in (4, 3, 2):
                        number_of_attempts = '\033[33m' + number_of_attempts + '\033[0m'
                    else:  # attempts == 1 or 0
                        number_of_attempts = '\033[31m' + number_of_attempts + '\033[0m'
        
                    game_start_message: str = f"\n● try to guess the word before the gallow is completed, you have {number_of_attempts} attempts:" if game_lan == 'en' else \
                        f"\n● tente adivinhar a palavra antes que a forca seja concluída, você tem {number_of_attempts} tentativa(s):"
        
                    print(game_start_message)
                    
                    print("""        ______|
       /     ||
       |     ◯ 
       |    /|\\
       |    / \\
       |
      / \\
     /___\\
            """)
            
                    lose_message: str = f"You Lost... The hidden word was {drawn_word}. Wanna play again? ;)" if game_lan == 'en' else \
                        f"Você perdeu... A palavra oculta era {drawn_word}. Deseja jogar novamente? ;)"
            
                    print(lose_message)
            
                    if game_lan == 'en':
                        print("[v] - \033[32mYes\033[0m // [x] - \033[31mNo\033[0m")
                    if game_lan == 'pt':
                        print("[v] - \033[32mSim\033[0m // [x] - \033[31mNão\033[0m")
            
                    print(">>> ", end='')

                    match user_answer:
                        case 'x':
                            print('\033[31m', end='')
                        case 'v':
                            print('\033[32m', end='')
                        case _:
                            print('\033[0m', end='')

                    print(user_answer, '\033[0m', sep='')
                
                    
                    temp_user_answer: bytes = getchar()

                    try:
                        if temp_user_answer.decode().lower() in lower_characters:
                            user_answer = temp_user_answer.decode().lower()
                    except UnicodeDecodeError as error:
                        pass
                    
                    if user_answer in ('v', 'x') and temp_user_answer == b'\x0d':
                        match user_answer:
                            case 'v':
                                return play_hangman()
                            case 'x':
                                print()
                                if game_lan == 'en':
                                    for i in range(3, -1, -1):
                                        print("Thanks for Playing!!! Closing in", i, '...', end='\r')
                                        time.sleep(1)
                                else:  # game_lan == 'pt'
                                    for i in range(3, -1, -1):
                                        print("Obrigado por Jogar!!! Fechando em", i, '...', end='\r')
                                        time.sleep(1)
                                os.system('cls')
                                return None
                        
        if not set(drawn_word).issubset(letters_guessed):  # User still Playing

            print(already_used_letters_text, end='')
            print(*letters_guessed, sep=', ', end='')
            if letters_guessed:  # If len(letters_guessed) != 0
                print('.')
            else:
                print()

            print(f"{word_str}", end='')

            for letter in drawn_word:
                print(letter if letter in letters_guessed else '_', end='')
            print(f" ({number_of_letters})")
            

            print(">>> \033[1m", user_answer, '\033[0m', sep='')
        
            temp_user_answer: bytes = getchar()
            
            try:
                if temp_user_answer.decode().lower() in lower_characters:
                    user_answer = temp_user_answer.decode().lower()
            except UnicodeDecodeError as error:
                pass
            
            if user_answer in lower_characters and temp_user_answer == b'\x0d' and user_answer not in letters_guessed:
                letters_guessed.append(user_answer)
                if user_answer not in drawn_word:
                    attempts -= 1


        else:  # Player has guessed the word :

            print(already_used_letters_text, end='')
            print(*letters_guessed, sep=', ', end='')

            if letters_guessed:  # If len(letters_guessed) != 0
                print('.')
            else:
                print()

            print(f"{word_str}", end='')

            for letter in drawn_word:
                print(letter if letter in letters_guessed else '_', end='')
            print('\n')

            print(victory_message, end='')

            if attempts == 1:
                print("(that was close!)" if game_lan == 'en' else "(foi por pouco!)")
            else:
                print()

            print("Wanna play again? ;)" if game_lan == 'en' else "Deseja jogar novamente? ;)")

            if game_lan == 'en':
                    print("[v] - \033[32mYes\033[0m // [x] - \033[31mNo\033[0m")
            if game_lan == 'pt':
                print("[v] - \033[32mSim\033[0m // [x] - \033[31mNão\033[0m")
            
            print(">>> ", end='')
            
            match user_answer:
                case 'x':
                    print('\033[31m', end='')
                case 'v':
                    print('\033[32m', end='')
                case _:
                    print('\033[0m', end='')

            print(user_answer, '\033[0m', sep='')
            
            temp_user_answer: bytes = getchar()

            try:
                if temp_user_answer.decode().lower() in lower_characters:
                    user_answer = temp_user_answer.decode().lower()
                  
            except UnicodeDecodeError as error:
                pass
                
            if user_answer in ('v', 'x') and temp_user_answer == b'\x0d':
                match user_answer:
                    case 'v':
                        return play_hangman()
                      
                    case 'x':
                        print()
                        if game_lan == 'en':
                            for i in range(3, -1, -1):
                                print("Thanks for Playing!!! Closing in", i, '...', end='\r')
                                time.sleep(1)
                              
                        else:  # game_lan == 'pt'
                            for i in range(3, -1, -1):
                                print("Obrigado por Jogar!!! Fechando em", i, '...', end='\r')
                                time.sleep(1)
                              
                        os.system('cls')
                        return None
    

if __name__ == '__main__':
    play_hangman()
