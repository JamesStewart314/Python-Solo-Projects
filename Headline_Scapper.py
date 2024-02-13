# /--------------------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Headline Scapper created in Python language - version 3.12 or higher - with dependencies on the "requests" and "beautifulsoup4" libraries.
#                                    To run it correctly, make sure you have these packages in your virtual environment.
#                                                                 Code Created in ~ 02/12/2024 ~
# \--------------------------------------------------------------------------------------------------------------------------------------------------------/


import os

import bs4
import requests

from bs4 import BeautifulSoup


def get_soup() -> BeautifulSoup:
    
    my_headers: dict = {'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    request = requests.get('https://www.bbc.com/news', headers=my_headers)
    html: bytes = request.content

    # Create Soup :
    my_soup = bs4.BeautifulSoup(html, 'html.parser')

    return my_soup


def get_headlines(soup: BeautifulSoup, /) -> list[str]:

    headlines_set: set = set()

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        headline: str = h.contents[0].lower()
        headlines_set.add(headline)
    
    return sorted(headlines_set)


def check_headlines(headlines: list[str], term_to_search: str):
    terms_list: list[str] = []
    terms_found: int = 0

    for idx, headline in enumerate(headlines, start=1):
        if term_to_search.lower() in headline:
            terms_list.append(headline)
            terms_found += 1
            
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



if __name__ == '__main__':

    os.system('cls')
    
    temp_soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(temp_soup)

    tearm_to_search: str = 'Biden'

    check_headlines(headlines, tearm_to_search)
