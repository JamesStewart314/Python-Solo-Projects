# /---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Text Sentiment Analysis Bot created in Python language - version 3.12 or higher - with dependencies on the "colorama", "translate" and "textblob" libraries.
#                                     To run it properly, make sure you have these frameworks in your virtual environment.
#
#                       I emphasize that this script was created for Windows, which means that it maybe not work correctly in other operating systems,
#                                                                     Code Created in ~ 02/01/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------------------------------------------------------/


import msvcrt
import os
import random
import string
import time

from dataclasses import dataclass
from typing import Callable


import textblob as tb

from colorama import Fore, Style
from translate import Translator


type Number = int | float

available_languages: tuple[str, ...] = ('en', 'pt')

special_portuguese_characters: str = "áàâãéèêíìîóòôõúùûçÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ"

portuguese_translator: Translator = Translator(to_lang='en', from_lang='pt')


@dataclass
class Mood:
    mood:  str
    emoji: str
    sentiment_polarity: float
    sentiment_subjecticity: float


class StylishWriting:

    used_symbols: tuple[str, ...] = tuple(string.ascii_letters + string.punctuation)
    number_of_letter_draws: int = 2
    
    @staticmethod
    def write(message: str, /, *, writing_delay: Number = 0.02, skip_end_line: bool = True) -> None:
        
        for letter in message:
            for _ in range(StylishWriting.number_of_letter_draws):

                print(random.choice(StylishWriting.used_symbols), end='', flush=True)
                time.sleep(writing_delay)
                print('\b', end='')

            print(letter, end='', flush=True)
        
        if skip_end_line:
            print('', flush=True)
    
    @staticmethod
    def write_loop(message: str, /, waiting_time: Number, *, writing_delay: Number = 0.02, return_delay: Number) -> None:
        for letter in message:
            for _ in range(StylishWriting.number_of_letter_draws):

                print(random.choice(StylishWriting.used_symbols), end='', flush=True)
                time.sleep(writing_delay)
                print('\b', end='')

            print(letter, end='', flush=True)

        time.sleep(waiting_time)

        for _ in range(len(message)):
            print('\b', end='', flush=True)

            for _ in range(StylishWriting.number_of_letter_draws):
                print(random.choice(StylishWriting.used_symbols), end='', flush=True)
                time.sleep(return_delay)
                print('\b', end='')
                
            print(' ', end='\b', flush=True)



# Function to check if a name is not empty, has only alphabetic characters and its length does not exceed 10 characters :
name_checker: Callable[[str], bool] = lambda x: all((bool(x), x.isalpha() and x.isascii(), len(x) <= 15))

# Function to check whether a text has at least 14 characters and only contains valid alphabetic characters
text_checker: Callable[[str], bool] = lambda x: all((len(x) >= 14, all([char in string.ascii_letters + string.punctuation + string.digits + special_portuguese_characters + "' " for char in x])))


def clear() -> None:
    os.system('cls')


def getchar() -> bytes:
    return msvcrt.getch()


def display_header(language: str) -> None:

    print(f"{Style.BRIGHT}", '_' * 93, f"{Style.RESET_ALL}", sep='')
    print("|| Please, select an language to continue ||"
            " Por favor, selecione um idioma para continuar ||")
    print('‾' * 93)
    print(' ' * 24, r'\\',
            f"\033[4m{Fore.BLUE} [en] - English{Style.RESET_ALL} || \033[4m{Fore.GREEN}[pt] - Portuguese {Style.RESET_ALL}//",
            sep='')
    print(' ' * 40, r' \/')

    print(' ' * 38, '| ', end='')

    if language in ('en', 'pt'):
        if language == 'en':
            print(f'{Fore.BLUE}', end='')
        else:
            print(f'{Fore.GREEN}', end='')

    print(f"{language:^4}", end='')
    print(f'{Style.RESET_ALL} |')


def get_mood(input_text: str, language: str) -> Mood:
    
    """
    This function receives a string containing text and analyzes the user's mood based on the vocabulary used.

    :param input_text: A string containing the text that should be analyzed.
    :return: An instance of the data class containing information relating to the result of the mood analysis 
    performed by the Textblob library.
    """

    analysis_result = tb.TextBlob(input_text).sentiment

    polarity: float
    subjectivity: float

    polarity, subjectivity = analysis_result.polarity, analysis_result.subjectivity

    # Establishing the parameters for mood analysis :
    excellent_mood_limit: float = 0.6
    great_mood_limit: float = 0.2
    neutral_mood_limit: float = -0.2
    bad_mood_limit: float = -0.6

    # Analyzing mood :
    if polarity >= excellent_mood_limit:
        if language == 'en':
            return Mood(f"{Style.DIM}{Fore.GREEN}Excellent!{Style.RESET_ALL}", '🥳', polarity, subjectivity)
        elif language == 'pt':
            return Mood(f"{Style.DIM}{Fore.GREEN}Excelente!{Style.RESET_ALL}", '🥳', polarity, subjectivity)
    
    elif polarity >= great_mood_limit:
        if language == 'en':
            return Mood(f"{Style.DIM}{Fore.BLUE}Great!{Style.RESET_ALL}", '😊', polarity, subjectivity)
        elif language == 'pt':
            return Mood(f"{Style.DIM}{Fore.BLUE}Ótimo!{Style.RESET_ALL}", '😊', polarity, subjectivity)
        
    elif polarity >= neutral_mood_limit:
        if language == 'en':
            return Mood(f"{Fore.LIGHTWHITE_EX}Neutral{Style.RESET_ALL}", '😐', polarity, subjectivity)
        elif language == 'pt':
            return Mood(f"{Fore.LIGHTWHITE_EX}Neutro{Style.RESET_ALL}", '😐', polarity, subjectivity)
        
    elif polarity >= bad_mood_limit:
        if language == 'en':
            return Mood(f"{Style.DIM}{Fore.LIGHTMAGENTA_EX}Bad{Style.RESET_ALL}", '🙁', polarity, subjectivity)
        elif language == 'pt':
            return Mood(f"{Style.DIM}{Fore.LIGHTMAGENTA_EX}Ruim{Style.RESET_ALL}", '🙁', polarity, subjectivity)
        
    else:
        if language == 'en':
            return Mood(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Awful{Style.RESET_ALL}", '😠', polarity, subjectivity)
        elif language == 'pt':
            return Mood(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Horrível{Style.RESET_ALL}", '😠', polarity, subjectivity)
    

def run_bot() -> None:

    program_lan = ''

    # --------------------------- Language Selection ----------------------------- #
    while True:

        clear()

        print(f"{Style.BRIGHT}", '_' * 93, f"{Style.RESET_ALL}", sep='')
        print("|| Please, select an language to continue ||"
                " Por favor, selecione um idioma para continuar ||")
        print('‾' * 93)
        print(' ' * 24, r'\\',
                f"\033[4m{Fore.BLUE} [en] - English{Style.RESET_ALL} || \033[4m{Fore.GREEN}[pt] - Portuguese {Style.RESET_ALL}//",
                sep='')
        print(' ' * 40, r' \/')

        print(' ' * 38, '| ', end='')

        if program_lan in available_languages:
            if program_lan == 'en':
                print(f'{Fore.BLUE}', end='')
            else:
                print(f'{Fore.GREEN}', end='')

        print(f"{program_lan:^4}", end='')
        print(f'{Style.RESET_ALL} |')

        user_pressed_key = getchar()
        
        if user_pressed_key == b'\x08' and len(program_lan) > 0:  # User pressed Backspace
            program_lan = program_lan[:-1]

        try:
            if user_pressed_key.decode().lower() in string.ascii_lowercase and len(program_lan) < 2:
                program_lan += user_pressed_key.decode().lower()

        except UnicodeDecodeError as error:
            pass

        if user_pressed_key == b'\x0d':  # User pressed Enter
            if program_lan in available_languages:
                break
            else:
                print("\a")  # Sound alert
    
    # -------------------------------- Start of the Program -------------------------------- #

    user_name: str = ''
    first_meet: bool = True

    greetings_message_text: str = f"● Welcome, user! This program is a simple prototype of a mood analyzer. To get started, type your first name and press Enter:"\
                                  if program_lan == 'en' else\
                                  f"● Bem-vindo, usuário! Este programa é um singelo protótipo de analisador de humor. Para começarmos, digite seu primeiro nome e pressione Enter:"
    
    error_message_text: str = f"⚠️ You can not do that! Please provide a non-empty name with less than or equal to fifteen characters."\
                              if program_lan == 'en' else\
                              f"⚠️ Você não pode fazer isso! Por favor, forneça um nome não vazio com uma quantidade inferior ou igual a quinze caracteres."

    while not name_checker(user_name):
        
        clear()
        display_header(program_lan)

        print()  # Line spacing

        StylishWriting.write(greetings_message_text) if first_meet else StylishWriting.write(greetings_message_text, writing_delay=0.001)
        first_meet = False
        user_name = input("\n>>> ").capitalize()
        
        
        if name_checker(user_name):
            break

        else:
            print()  # Line spacing
            StylishWriting.write_loop(error_message_text, 5, writing_delay=0.005, return_delay=0.002)
    

    first_meet = True

    starting_message: str = f"● Nice to meet you, {user_name}! Please provide a text concisely describing some recent experience so we can assess your mood:"\
                            if program_lan == 'en' else\
                            f"● Prazer em conhecê-lo(a), {user_name}! Por favor, forneça um texto descrevendo concisamente alguma experiência recente para avaliarmos seu humor:"
    
    exit_message: str = "(or type \"exit\" and press enter to end the program)"\
                         if program_lan == 'en' else\
                        "(ou digite \"sair\" e pressione enter para encerrar o programa)"
    
    exit_alert: str = f"Thank you very much for Using this Program! I hope you have a great day, {user_name} (˵ •̀ ᴗ - ˵)"\
                      if program_lan == 'en' else\
                      f"Muito Obrigado por Utilizar este Programa! Espero que tenha um ótimo dia, {user_name} (˵ •̀ ᴗ •̀ ˵)"
    
    incompatible_text_message: str = "⚠️ Invalid Input. Please provide text greater than 14 in size containing only alphabetic characters."\
                                     if program_lan == 'en' else\
                                     "⚠️ Entrada inválida. Por favor, forneça um texto com tamanho superior a 14 contendo apenas caracteres alfabéticos."

    while True:
        
        clear()
        display_header(program_lan)
        print()  # Line spacing

        StylishWriting.write(starting_message) if first_meet else StylishWriting.write(starting_message, writing_delay=0.001)
        StylishWriting.write(exit_message) if first_meet else StylishWriting.write(exit_message, writing_delay=0.001)

        first_meet = False

        text_to_analyze: str = input("\n>>> ")
        
        # Close Command :
        if any((text_to_analyze.lower().strip() == 'exit' and program_lan == 'en', text_to_analyze.lower().strip() == 'sair' and program_lan == 'pt')):
            print()  # Line spacing
            StylishWriting.write(exit_alert, skip_end_line=False)
            
            for i in range(3, -1, -1):
                print(f"({i}...)", end='', flush=True)
                time.sleep(1)
                print('\b' * 6, end='', flush=True)
            
            # Close the Bot :
            clear()
            break
        
        # Invalid Input :
        elif not text_checker(text_to_analyze):
            print()  # Line spacing
            StylishWriting.write_loop(incompatible_text_message, 5, writing_delay=0.005, return_delay=0.002)
            continue

        
        print()  # Line spacing

        StylishWriting.write_loop("Processing Results..." if program_lan == 'en' else "Processando Resultados...", 2, return_delay=0.003)

        # Result from mood analysis :
        result: Mood = get_mood(text_to_analyze, program_lan) if program_lan == 'en' else get_mood(portuguese_translator.translate(text_to_analyze), program_lan)

        # Displaying results in the terminal :
        StylishWriting.write("⭕ Results :" if program_lan == 'en' else "⭕ Resultados :")

        print(f"● Humor Categorized as: {result.mood} {result.emoji}" if program_lan == 'en' else f"● Humor Categorizado Como: {result.mood} {result.emoji}")

        print(f"● Your Mood is Rated at: {round(result.sentiment_polarity * 100, 1)}%;" if program_lan == 'en' else
              f"● Seu Humor está Avaliado em: {round(result.sentiment_polarity * 100, 1)}%;")
        
        print(f"● The Subjectivity Rate Contained in the Text Provided is: {round(result.sentiment_subjecticity * 100, 1)}%." if program_lan == 'en' else
              f"● Taxa de Subjetividade Contida no Texto Fornecido: {round(result.sentiment_subjecticity * 100, 1)}%.")
        
        print()  # Line spacing

        print("Press Any Key to Continue..." if program_lan == 'en' else "Pressione Qualquer Tecla para Prosseguir...")
        getchar()


if __name__ == '__main__':
    run_bot()
