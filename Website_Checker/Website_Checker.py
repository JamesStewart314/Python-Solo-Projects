# /---------------------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Website Checker created in Python language - version 3.12 or higher - with dependencies on the "requests" and "fake_useragent" libraries.
#                                       To run it properly, make sure you have this package in your virtual environment.
#                                                               Code Created in ~ 01/23/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------------------------------------/

import csv
import http
import os

import requests
import fake_useragent

from fake_useragent import UserAgent


def clean() -> None:

    # function to clean the terminal.

    os.system('cls')


def get_websites(csv_path: str) -> list[str]:

    #   This function takes as a parameter a string containing the path of a csv file
    # and returns a list of strings containing the name of the websites obtained from the file.

    websites_list: list[str] = []

    with open(csv_path, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        
        for _, website in csv_reader:
            websites_list.append(website) if website.startswith('https://') \
                else  websites_list.append(f"https://{website}")
    
    return websites_list


def get_user_agent() -> str:
    
    user_agent: UserAgent = fake_useragent.UserAgent()
    
    return user_agent.chrome


def get_status_description(status_code: int) -> str:

    for value in http.HTTPStatus:
        if value == status_code:
            description: str = f"Description: ({value} - {value.name}) - \033[32m{value.description}\033[0m"

            return description
            
    return "Description: (???) Unknown Status Code..."


def check_website(website: str, user_agent: UserAgent) -> None:

    # Checks the status of a given website.

    try:
        code: int = requests.get(website, headers={'User-Agent': user_agent}).status_code

        message: str = f"✅ \"{website}\" - {get_status_description(code)}"        
        print(message, end='\n' * 2)

    except Exception as error:
        error_message: str = f"❌ Could not get information for the website: \"{website}\" due to an error: \"\033[31m{error}\033[0m\""
        print(error_message, end='\n' * 2)


if __name__ == '__main__':
    
    clean()  # To clean the terminal before the code starts.

    sites: list[str] = get_websites("websites.csv")
    user_agent: str = get_user_agent()
    
    for index, site in enumerate(sites, start=1):
        print(index, '°', sep='', end=' ')
        check_website(site, user_agent)
