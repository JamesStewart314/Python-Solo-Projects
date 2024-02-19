# /-----------------------------------------------------------------------------------------------------------------------------------\
#  This code is a URL Shortener created in Python language - version 3.12 or higher - with dependencies on the "requests" library.
#          It was written for personal educational purposes only, which means that it will not work if you try to run it.
#                                                    Code Created in ~ 02/08/2024 ~
# \-----------------------------------------------------------------------------------------------------------------------------------/


import os
from typing import Final

import requests
from requests import Response


API_KEY: Final[str] = "*************************************"

BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str) -> str | None:

    """
    
    It takes as input a valid link and returns a shortened version of the same link.

    :param full_link: A string containing the link to be shortened.
    :return: A string containing the given link in its shortened version.
    
    """

    payload: dict[str, str] = {'key': API_KEY, 'short': full_link}
    request: Response = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    print()  # Line Spacing

    if (url_data := data.get('url')):

        match url_data['status']:

            case 1:
                print("The Link has Already been Shortened!")
            
            case 2:
                print("The Entered Link is Not a Link...")
            
            case 3:
                print("The Preferred Link Name is Already Taken!")
            
            case 4:
                print("Invalid API Key!")
            
            case 5:
                print("The Link has not Passed the Validation. Includes Invalid Characters.")
            
            case 6:
                print("The Link Provided is from a Blocked Domain!")

            case 7:
                short_link: str = url_data['shortLink']
                
                return short_link

            case 8:
                print("Reached Monthly Link Limit. Please, Try Again Later...")
            
            case _:
                return None




if __name__ == '__main__':

    os.system('cls')
    
    input_link: str = input("Type a Link You Want to Short:\n>>> ")

    if (result_link := shorten_link(input_link)):
        print(f"Your Shortened Link is:\n• {result_link}")
