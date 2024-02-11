# /---------------------------------------------------------------------------------------------------------------------------\
#  This code is a PDF Reader created in Python language - version 3.12 or higher - with dependencies on the "pypdf2" library.
#                  To run it properly, make sure you have this package in your virtual environment.
#                                                Code Created in ~ 02/08/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------/

import collections
import itertools
import os
import re

from collections import Counter
from typing import Tuple

import PyPDF2

from PyPDF2 import PdfReader

type Text_list = list[str]
type Pages = int


def clear() -> None:
    os.system('cls')


def line_spacing(lines: int, /) -> None:
    print('\n' * lines, end='')


def extract_text_pdf(pdf_file: str, /) -> Tuple[Text_list, Pages]:

    r"""
    
     Receives a PDF file path and returns a tuple containing a list
    of strings with the content of the PDF pages and the number of pages
    in the document.

    :param pdf_file: string containing the exact path of the file on disk. 
    ( Example: C:\Users\myUser\Desktop\folder\MyFile.pdf )
    
    :return: Tuple containing a list of strings containing the content
    of the PDF pages and the number of pages in the file, respectively.
    
    """

    with open(pdf_file, 'rb') as pdf:

        reader: PdfReader = PyPDF2.PdfReader(pdf, strict=False)

        pages: Pages = len(reader.pages)
        pdf_text: Text_list = [page.extract_text() for page in reader.pages]

        return (pdf_text, pages)


def count_words(text_list: Text_list, /) -> Tuple[Counter, int, int]:

    """

     It receives as its main parameter a list with strings
    and returns a tuple containing a Counter object of the words present
    in the list's strings, an integer informing the total number of words
    present in the strings and an integer with the number of alphanumeric
    characters in the strings.

    :param text_list: A list containing only strings.
    :return: Tuple containing a Counter object, an integer value (number of words)
    and another integer value (number of characters), respectively.
    
    """

    all_words: list[str] = []

    for text in text_list:
        split_text: Text_list = re.split(r'\s+|[,;?!.-]\s*', text.lower())

        all_words.extend([word for word in split_text if word])
    
    return ((w_num := collections.Counter(all_words)), w_num.total(), collections.Counter(''.join(all_words)).total())


if __name__ == '__main__':

    clear()

    simple_counter = itertools.count(start=1)

    # While Given Path is not a File and doesn't End with Extension ".pdf" :
    while not (os.path.isfile((pdf_input_path := input("Give a PDF Complete Path to Read the File:\n>>> "))) or pdf_input_path.endswith('.pdf')):
        print("Given File Path doesn't Exist or is not a PDF!\nPress Enter to Continue...")
        
        os.system('pause > nul')
        clear()

    clear()

    result: Tuple[Text_list, Pages] = extract_text_pdf(fr"{pdf_input_path}")
    
    words_info: Tuple[Counter, int, int] = count_words(result[0])

    print("File Info:")
    line_spacing(1)
    print(f"• Title: {os.path.basename(pdf_input_path).removesuffix(os.path.splitext(pdf_input_path)[1])} ;")  # Print the File Name Without Extension
    print(f"• Pages: {result[1]} ;")
    print(f"• File Size: {os.stat(pdf_input_path).st_size / (1024 * 1024):,.2f} Mb ;")  # Print the File Size in Megabytes
    print(f"• Words Quantity: {words_info[1]} ;")
    print(f"• Characters Quantity: {words_info[2]}")
    
    line_spacing(2)
    
    print("Most Common Words:")
    line_spacing(1)

    for word, mention in words_info[0].most_common(5):
        print(f"{next(simple_counter)}° {f"\"{word:^10}\""} : {mention} times")

    line_spacing(2)

    for text, current_page in zip(result[0], range(1, result[1] + 1)):
        print(f"/{f"Page {current_page}":-^100}\\")
        line_spacing(1)
        print(text)
        line_spacing(1)
        print("\\", '-' * 100, '/', sep='')
        line_spacing(2)

    # Displays the Closing Divider :
    print("|", '-' * 100, '|', sep='')
    print(f"\n|{"Press Enter to Close the Reading...":^100}|")
    print("\n|", '-' * 100, '|', sep='')

    os.system('pause > nul')
    clear()
