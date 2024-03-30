# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.10 and higher - 07/15/2023
#          This is an old project that I intend to reformulate and organize later on.
# \ ----------------------------------------------------------------------------------------- / #

import os
import itertools
import time

import colorama as clr

clr.init(autoreset=True)

dicionario_letras = {'a': ["  ****  ", "**    **", "********", "**    **", "**    **", "**    **"],
                     'b': ["******  ", "**     *", "******  ", "**     *", "**     *", "******  "],
                     'c': ["  *****   ", "**      **", "**        ", "**        ", "**      **", "  *****   "],
                     'd': ["****    ", "**    * ", "**     *", "**     *", "**    * ", "****    "],
                     'e': ["*********", "**       ", "*****    ", "**       ", "**       ", "*********"],
                     'f': ["*********", "**       ", "*******  ", "**       ", "**       ", "**       "],
                     'g': ["  *****  ", "**     **", "**       ", "**   ****", "**     **", " ******  "],
                     'h': ["**     **", "**     **", "*********", "**     **", "**     **", "**     **"],
                     'i': ["******", "  **  ", "  **  ", "  **  ", "  **  ", "******"],
                     'j': ["   ********", "       **  ", "       **  ", "       **  ", "**     **  ",
                           "  ******   "],
                     'k': ["**      *", "**     * ", "**  ***  ", "**   *   ", "**     * ", "**      *"],
                     'l': [" **      ", "  **     ", "  **     ", "  **     ", " **      ", "*********"],
                     'm': ["***       ***", "** *     * **", "**  *   *  **", "**    *    **", "**         **",
                           "**         **"],
                     'n': ["**      **", "** *    **", "**  *   **", "**   *  **", "**    * **", "**      **"],
                     'o': ["  ******  ", "**      **", "**      **", "**      **", "**      **", "  ******  "],
                     'p': ["*******  ", "**     **", "**     **", "*******  ", "**       ", "**       "],
                     'q': ["  ******     ", "**      **   ", "**      **   ", "**      **   ", "**   *  **  *",
                           "  *****  **  "],
                     'r': ["******   ", "**    ** ", "******   ", "**    ** ", "**     **", "**     **"],
                     's': ["   *****   ", "**       **", "  ****     ", "      ***  ", "**       **",
                           "   *****   "],
                     't': ["  **     ", "*********", "  **     ", "  **     ", "  **     ", "   ****  "],
                     'u': ["**     **", "**     **", "**     **", "**     **", "**     **", " ******* "],
                     'v': ["**     **", "**     **", "**     **", " **   ** ", "  ** **  ", "    *    "],
                     'w': [" **          ** ", "**            **", "**     **     **", " **   *  *   ** ",
                           "  ** *    * **  ", "   ***    ***   "],
                     'x': ["**        **", "  **    **  ", "     **     ", "  **    **  ", " **      ** ",
                           "**        **"],
                     'y': ["**      **", " *     ** ", "  ******  ", "     **   ", "   **     ", " **       "],
                     'z': ["*********** ", "      ****  ", "    ***     ", "  ***       ", "****        ",
                           "*********** "],
                     ' ': ["    ", "    ", "    ", "    ", "    ", "    "]}

reset_c = f"{clr.Fore.RESET}"

cores = [f"{clr.Fore.RED}", f"{clr.Fore.LIGHTYELLOW_EX}", f"{clr.Fore.YELLOW}", f"{clr.Fore.GREEN}", f"{clr.Fore.BLUE}",
         f"{clr.Fore.CYAN}", f"{clr.Fore.MAGENTA}"]


def limpar():
    os.system("cls")


def encerramento():
    print(f"\n{clr.Fore.LIGHTBLUE_EX}Thank you for using this Program !!!{reset_c}"
          f"\n\n{clr.Fore.YELLOW}See you later, leaving . . .{reset_c}")
    for x in range(3, 0, -1):
        print(x, end="\r", flush=True)
        time.sleep(1.5)
    limpar()
    exit()


def op_cores():
    print(f"● {clr.Fore.YELLOW}Yellow{reset_c} : \'y\' + \'ENTER\'")
    print(f"● {clr.Fore.BLUE}Blue{reset_c} : \'b\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTBLUE_EX}Light Blue{reset_c} : \'lb\' + \'ENTER\'")
    print(f"● {clr.Fore.WHITE}White{reset_c} : \'w\' + \'ENTER\'")
    print(f"● {clr.Fore.CYAN}Cyan{reset_c} : \'c\' + \'ENTER\'")
    print(f"● {clr.Fore.GREEN}Green{reset_c} : \'g\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTGREEN_EX}Light Green{reset_c} : \'lg\' + \'ENTER\'")
    print(f"● {clr.Fore.RED}Red{reset_c} : \'r\' + \'ENTER\'")
    print(f"● {clr.Fore.MAGENTA}Magenta{reset_c} : \'m\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTBLACK_EX}Black{reset_c} : \'bl\' + \'ENTER\'")
    print(f"● {clr.Fore.RED}R{reset_c}{clr.Fore.GREEN}G{clr.Fore.BLUE}B{reset_c} . . . ? : \'rgb\' + \'ENTER\'")
    print(f"\n● {clr.Back.WHITE}{clr.Fore.BLACK}Back{reset_c}{clr.Back.RESET} : \'back\' + \'ENTER\'")
    print(f"● {clr.Back.WHITE}{clr.Fore.BLACK}Exit{reset_c}{clr.Back.RESET} : \'exit\' + \'ENTER\'")


def imprimir_texto_personalizado(frase, codigo_cor):
    rainbow_text = itertools.cycle(cores)
    print("\t", end="")
    for letra in "YOUR STYLIZED TEXT LOOKS LIKE THIS":
        if letra == " ":
            print(" ", end="")
        else:
            cor = next(rainbow_text)
            print(f"{cor}{letra}{reset_c}", end="")
    print(" :\n\n")

    tamanho_linha = 3

    for letra in frase:
        if letra.isspace():
            tamanho_linha += 7
        else:
            tamanho_linha += len(f"{dicionario_letras.__getitem__(letra)[0]}   ")

    print('  ' + "_" * (tamanho_linha - 3) + '\n/' + " " * (tamanho_linha - 2) + ' \\')

    for indice in range(6):
        primeita_tabulacao_lateral = True
        for letra in frase:
            if primeita_tabulacao_lateral is False:
                print(codigo_cor + dicionario_letras.__getitem__(letra)[indice] + reset_c, end="   ")
            else:
                print("| " + codigo_cor + dicionario_letras.__getitem__(letra)[indice] + reset_c, end="   ")
                primeita_tabulacao_lateral = False
        print(" |")

    print('\\' + "_" * (tamanho_linha - 2) + '/')

    while True:
        print("\n\n\tPress \'s\' + \'ENTER\' to exit or just \'ENTER\' to customize another phrase.")
        op_temp = input("  >>>\t").lower().strip()

        if op_temp == 's':
            encerramento()
        elif op_temp == '':
            limpar()
            main()
        else:
            input("\tInvalid option, choose one of the available alternatives !!! (press \'ENTER\')")
            limpar()
            imprimir_texto_personalizado(frase, codigo_cor)


def imprimir_texto_rgb(frase):
    rainbow_text = itertools.cycle(cores)
    print("\t", end="")
    for letra in "YOUR STYLIZED TEXT LOOKS LIKE THIS":
        if letra == " ":
            print(" ", end="")
        else:
            cor = next(rainbow_text)
            print(f"{cor}{letra}{reset_c}", end="")
    print(" :\n\n")

    tamanho_linha = 3

    for letra in frase:
        if letra.isspace():
            tamanho_linha += 7
        else:
            tamanho_linha += len(f"{dicionario_letras.__getitem__(letra)[0]}   ")

    print('  ' + "_" * (tamanho_linha - 3) + '\n/' + " " * (tamanho_linha - 2) + ' \\')

    for indice in range(6):
        rainbow_text_temp = itertools.cycle(cores)
        primeita_tabulacao_lateral = True
        for letra in frase:
            if not letra == ' ':
                cor_temp = next(rainbow_text_temp)
                if primeita_tabulacao_lateral is False:
                    print(cor_temp + dicionario_letras.__getitem__(letra)[indice] + reset_c, end="   ")
                else:
                    print("| " + cor_temp + dicionario_letras.__getitem__(letra)[indice] + reset_c, end="   ")
                    primeita_tabulacao_lateral = False
            else:
                if primeita_tabulacao_lateral is False:
                    print(dicionario_letras.__getitem__(letra)[indice], end="   ")
                else:
                    print("| " + dicionario_letras.__getitem__(letra)[indice], end="   ")
                    primeita_tabulacao_lateral = False
        print(" |")

    print('\\' + "_" * (tamanho_linha - 2) + '/')

    while True:
        print("\n\n\tPress \'s\' + \'ENTER\' to exit or just \'ENTER\' to customize another phrase.")
        op_temp = input("  >>>\t").lower().strip()

        if op_temp == 's':
            encerramento()
        elif op_temp == '':
            limpar()
            main()
        else:
            print("\nInvalid option, choose one of the available alternatives !!! (press \'ENTER\')")
            input()
            limpar()
            imprimir_texto_rgb(frase)


def main():

    global frase

    while True:

        print("\t" * 4 + f"{clr.Back.LIGHTWHITE_EX}{clr.Fore.RED}~~~ !!! YOU ARE VERY WELCOME !!! ~~~"
                         f"{reset_c}{clr.Back.RESET}\n\n\n")

        print(f"This program {clr.Style.BRIGHT}{clr.Fore.RED}style{reset_c}{clr.Style.RESET_ALL} your phrase "
              f"using {clr.Fore.BLUE}colors{reset_c} and {clr.Style.BRIGHT}{clr.Fore.GREEN}asterisks{reset_c}"
              f" {clr.Style.RESET_ALL} !!!\n")

        try:
            frase = input(f"{clr.Fore.MAGENTA}●{reset_c} {clr.Fore.WHITE}"
                          f" E n t e r  a  P h r a s e :{reset_c} ").lower().strip()
            for caracter in frase:
                if caracter not in dicionario_letras.keys():
                    raise Exception("It is not yet possible to use symbols (',', '.', '!' and etc.),"
                                    " numerals or empty texts, sorry...")
            if frase.isspace() or frase == "":
                limpar()
                raise NameError("You cannot style an empty sentence.")
            else:
                break
        except Exception as e:
            limpar()
            print(e)
            error_inp = input("\nPress \'Enter\' to try again or type \"exit\" and press \'Enter\'"
                              " to close the program . . .\n  >>>>\t").lower()
            if error_inp == "close":
                encerramento()
            limpar()

    limpar()

    while True:
        print("\t / " + "-" * 44 + f"\\\n\t| {clr.Fore.YELLOW}Tell us how you want"
                                           f" to personalize your text{reset_c} |\n\t \\ " + "-" * 44 + "/\n\n")

        op_cores()
        opcao = input("\n >>>\t").lower().strip()
        match opcao:
            case 'y':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.YELLOW)
            case 'b':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.BLUE)
            case 'lb':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.LIGHTBLUE_EX)
            case 'w':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.WHITE)
            case 'c':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.CYAN)
            case 'g':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.GREEN)
            case 'lg':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.LIGHTGREEN_EX)
            case 'r':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.RED)
            case 'm':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.MAGENTA)
            case 'bl':
                limpar()
                imprimir_texto_personalizado(frase, clr.Fore.LIGHTBLACK_EX)
            case 'rgb':
                limpar()
                imprimir_texto_rgb(frase)
            case 'back':
                limpar()
                main()
            case 'exit':
                limpar()
                encerramento()
            case _:
                limpar()
                op_temp = input("\tInvalid Option, press \'Enter\' to select an option or type"
                                " \'close\' and press \'ENTER\' to close the program.").lower().strip()
                limpar()
                if op_temp == "close":
                    limpar()
                    encerramento()


main()
limpar()
