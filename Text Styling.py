import colorama as clr, os, itertools, time

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
    print(f"\n{clr.Fore.LIGHTBLUE_EX}Obrigado por utilizar este Programa !!!{reset_c}"
          f"\n\n{clr.Fore.YELLOW}Até logo, saindo . . .{reset_c}")
    for x in range(3, 0, -1):
        print(x, end="\r", flush=True)
        time.sleep(1.5)
    exit()


def op_cores():
    print(f"● {clr.Fore.YELLOW}Amarelo{reset_c} : \'a\' + \'ENTER\'")
    print(f"● {clr.Fore.BLUE}Azul{reset_c} : \'b\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTBLUE_EX}Azul Claro{reset_c} : \'lb\' + \'ENTER\'")
    print(f"● {clr.Fore.WHITE}Branco{reset_c} : \'w\' + \'ENTER\'")
    print(f"● {clr.Fore.CYAN}Ciano{reset_c} : \'c\' + \'ENTER\'")
    print(f"● {clr.Fore.GREEN}Verde{reset_c} : \'g\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTGREEN_EX}Verde Claro{reset_c} : \'lg\' + \'ENTER\'")
    print(f"● {clr.Fore.RED}Vermelho{reset_c} : \'r\' + \'ENTER\'")
    print(f"● {clr.Fore.MAGENTA}Magenta{reset_c} : \'m\' + \'ENTER\'")
    print(f"● {clr.Fore.LIGHTBLACK_EX}Preto{reset_c} : \'bl\' + \'ENTER\'")
    print(f"● {clr.Fore.RED}R{reset_c}{clr.Fore.GREEN}G{clr.Fore.BLUE}B{reset_c} . . . ? : \'rgb\' + \'ENTER\'")
    print(f"\n● {clr.Back.WHITE}{clr.Fore.BLACK}Voltar{reset_c}{clr.Back.RESET} : \'back\' + \'ENTER\'")
    print(f"● {clr.Back.WHITE}{clr.Fore.BLACK}Sair{reset_c}{clr.Back.RESET} : \'sair\' + \'ENTER\'")


def imprimir_texto_personalizado(frase, codigo_cor):
    rainbow_text = itertools.cycle(cores)
    print("\t", end="")
    for letra in "SEU TEXTO ESTILIZADO FICOU ASSIM":
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
        print("\n\n\tPressione \'s\' + \'ENTER\' para sair ou apenas \'ENTER\' para personalizar outra frase.")
        op_temp = input("  >>>\t").lower().strip()

        if op_temp == 's':
            encerramento()
        elif op_temp == '':
            limpar()
            main()
        else:
            input("\tOpção Inválida, escolha uma das alternativas disponíveis !!! (tecle \'ENTER\')")
            limpar()
            imprimir_texto_personalizado(frase, codigo_cor)


def imprimir_texto_rgb(frase):
    rainbow_text = itertools.cycle(cores)
    print("\t", end="")
    for letra in "SEU TEXTO ESTILIZADO FICOU ASSIM":
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
        print("\n\nPressione \'s\' + \'ENTER\' para sair ou apenas \'ENTER\' para personalizar outra frase.\n")
        op_temp = input("  >>>\t").lower().strip()

        if op_temp == 's':
            encerramento()
        elif op_temp == '':
            limpar()
            main()
        else:
            print("\nOpção Inválida, escolha uma das alternativas disponíveis !!! (tecle \'ENTER\')")
            input()
            limpar()
            imprimir_texto_rgb(frase)


def main():
    global frase
    while True:

        print("\t" * 4 + f"{clr.Back.BLUE}{clr.Fore.LIGHTYELLOW_EX}~~~ !!! SEJA MUITO BEM-VINDO(A) !!! ~~~"
                         f"{reset_c}{clr.Back.RESET}\n\n\n")

        print(f"Este programa {clr.Style.BRIGHT}{clr.Fore.RED}estiliza{reset_c}{clr.Style.RESET_ALL} sua frase "
              f"utilizando {clr.Fore.BLUE}cores{reset_c} e {clr.Style.BRIGHT}{clr.Fore.GREEN}asteríscos{reset_c}"
              f" {clr.Style.RESET_ALL} !!!\n")

        try:
            frase = input(f"{clr.Fore.MAGENTA}●{reset_c} {clr.Fore.WHITE}"
                          f" D i g i t e  u m a  F r a s e :{reset_c} ").lower().strip()
            for caracter in frase:
                if caracter not in dicionario_letras.keys():
                    raise Exception("Ainda não é possível utilizar símbolos (',', '.', '!' e etc.),"
                                    " numerais ou textos vazios, perdão...")
            if frase.isspace() or frase == "":
                limpar()
                raise NameError("Não é possível estilizar uma frase vazia.")
            else:
                break
        except Exception as e:
            limpar()
            print(e)
            error_inp = input("\nPressione \'Enter\' para tentar novamente ou digite \"sair\" e pressione \'Enter\'"
                              " para encerrar o programa . . .\n  >>>>\t").lower()
            if error_inp == "sair":
                encerramento()
            limpar()

    limpar()

    while True:
        print("\t / " + "-" * 41 + f"\\\n\t| {clr.Fore.YELLOW}Informe como deseja"
                                           f" personalizar seu texto{reset_c} |\n\t \\ " + "-" * 41 + "/\n\n")

        op_cores()
        opcao = input("\n >>>\t").lower().strip()
        match opcao:
            case 'a':
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
            case 'sair':
                limpar()
                encerramento()
            case _:
                limpar()
                op_temp = input("\tOpção Inválida, tecle \'Enter\' para selecionar uma opção ou digite"
                                " \'sair\' e pressione \'ENTER\' para encerrar o programa.").lower().strip()
                limpar()
                if op_temp == "sair":
                    limpar()
                    encerramento()


main()
limpar()


# 'a' alternativo: ["      ***", "    *  **", "   ******", "  *    **", " *     **", "*      **"]
