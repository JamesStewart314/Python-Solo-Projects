# /----------------------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Headline Scapper created in Python language - version 3.12 or higher - with dependencies on the "requests" and "beautifulsoup4" libraries.
#                                    To run it correctly, make sure you have these packages in your virtual environment.
#
# It is possible that some specific scoring combinations could cause inaccuracies in the results, but I chose not to address these cases just for convenience.
#           The solutions to these problems are completely feasible, but they represent minute details that are superfluous to the final result of a
#                                                         code prototype whose sole purpose is learning.
#
#         Furthermore, for the code to work correctly, you need to replace the "< Enter your User Agent Here >" field with your User Agent 
#                                                     (open your default browser and search for "My User Agent")
#
#                                                                 Code Created in ~ 02/12/2024 ~
# \----------------------------------------------------------------------------------------------------------------------------------------------------------/


import os

import bs4
import requests

from bs4 import BeautifulSoup


def get_soup() -> BeautifulSoup:

    # Returns an instance of the BeautifulSoup class 
    # containing information relating to news headers from the BBC News website.
    
    my_headers: dict = {'User-Agent': '< Enter your User Agent Here >'}

    request = requests.get('https://www.bbc.com/news', headers=my_headers)
    html: bytes = request.content

    # Create Soup :
    my_soup = bs4.BeautifulSoup(html, 'html.parser')

    return my_soup


def get_headlines(soup: BeautifulSoup, /) -> list[str]:

    # Receives and processes the instance of the BeautifulSoup class 
    # containing news headers and returns a list of strings with the 
    # contents of the headers.

    headlines_set: set = set()

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        headline: str = h.contents[0].lower()
        headlines_set.add(headline)
    
    return sorted(headlines_set)


def check_headlines(headlines: list[str], term_to_search: str) -> None:

    # checks matches for a given word within a list of strings 
    # storing the contents of the Headers.

    terms_list: list[str] = []
    terms_found: int = 0
    word_found: bool

    quotes: set[str] = {"\'", "\""}

    for idx, headline in enumerate(headlines, start=1):
        word_found = False

        for word in set(headline.split()):
            if tearm_to_search in word:
                
                try:
                    if len(word) == len(tearm_to_search):
                        
                        terms_list.append(headline)
                        terms_found += 1
                        word_found = True
                        
                        break
                    
                    elif bool({word[0], word[-1], word[-2]}.intersection(quotes)) and ((len(word) == len(tearm_to_search) + 1) or (len(word) == len(tearm_to_search) + 2)):
                        terms_list.append(headline)
                        terms_found += 1
                        word_found = True

                        break

                except IndexError as error:
                    word_found = False

        if word_found:
            print(f"[{idx}]: {headline.capitalize()} <----------------------< \033[32mTerm Found!\033[0m")
        else:
            print(f"[{idx}]: {headline.capitalize()}")
    

    print('\n|', f"{" END OF SEARCH ":-^81}", '|\n', sep='')

    if terms_list:
        print(f"\t• \"{term_to_search}\" was mentioned {terms_found} times.\n")
        print('|', '-' * 81, '|\n\n', sep='')

        for idx, headline in enumerate(terms_list, start=1):
            print("Headers with Mention:\n")
            print(f"[{idx}]: {headline.capitalize()}")
    
    else:
        print(f"\tNo matches found for term \"{term_to_search}\".\n")
        print('|', '-' * 81, '|', sep='')
    
    return None



if __name__ == '__main__':

    os.system('cls')
    
    temp_soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(temp_soup)

    tearm_to_search: str = input("What term would you like to check for in BBC News headers? >> ")

    check_headlines(headlines, tearm_to_search)
