# /-----------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Currency Converter created in Python language - version 3.12 or higher - with dependencies on the "requests" library.
#          It was written for personal educational purposes only, which means that it will not work if you try to run it.
#                                           Code Created in ~ 02/12/2024 ~
# \-----------------------------------------------------------------------------------------------------------------------------------/


import json
import os
from typing import Final

import requests
from requests import Request


# Constants :
BASE_URL: Final[str] = r'http://api.exchangeratesapi.io/v1/'
API_KEY: Final[str] = r'********************************'


def _get_rates(mock: bool = False) -> dict:

    # Receives and processes information relating 
    # to currencies at the current time if the "mock" parameter 
    # is False, otherwise it returns values stored in a .json file 
    # containing information relating to the last currency data query.

    if mock and os.path.isfile(r'rates.json'):
        with open('rates.json', 'r') as file:
            return json.load(file)

    payload: dict[str, str] = {'access_key': API_KEY}
    request: Request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    with open('rates.json', 'w') as file:
        json.dump(data, file)

    return data


def get_currency(currency: str, rates: dict) -> float:

    # Get the value of a base currency :

    current_currency: str = currency.upper()

    if current_currency in rates.keys():
        rates.get(current_currency)
    else:
        raise ValueError(f"\"{currency}\" is not a valid currency.")


def convert_currency(amount: int | float, base: str, vs: str, rates: dict) -> float:

    # Converts the value from one base currency to another target currency :
    
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)

    return conversion


if __name__ == '__main__':

    data: dict = _get_rates(mock=True)
    current_rates: dict = data.get('rates')

    convert_currency(100, 'eur', 'jpy', rates=current_rates)
