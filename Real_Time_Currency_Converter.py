# /---------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Real Time Currency Converter created in Python language - version 3.12 or higher - with dependencies on the "requests" library.
#                          To run it properly, make sure you have this package in your virtual environment.
#                                                      Code Created in ~ 02/11/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------------------------/


import json
from typing import Final

import requests
from requests import Response


class Currency_Converter:
    
    @staticmethod
    def currency_converter(value: int | float, /, *, base: str, destiny: str):

        """
        
        Returns the value corresponding to the monetary conversion
        between a base currency and a target currency.

        :param value: A positive numeric value corresponding to the money to be converted.
        :param base: The base currency in which the provided value is located.
        :param destiny: The currency intended to convert the value.

        :return: A floating point value rounded to two decimal places containing the conversion
        value from the base currency to the target currency.
        
        """

        # API link to get the exchange data :
        url: Final[str] = f'https://api.exchangerate-api.com/v4/latest/{base}'

        API_response: Response = requests.get(url).json()

        exchange_rate: float = float(API_response.get('rates').get(destiny))

        return round(value * exchange_rate, 2)
    

    @staticmethod
    def get_available_currencies() -> str:
        return f"""\n• Available Currencies:\n\n{list(requests.get('https://api.exchangerate-api.com/v4/latest/USD').json().get('rates').keys())}"""

if __name__ == '__main__':
    
    # Usage Examples :
    usd_to_jpy: int | float = Currency_Converter.currency_converter(2718, base='USD', destiny='JPY')
    eur_to_brl: int | float = Currency_Converter.currency_converter(1618, base='EUR', destiny='BRL')
    chf_to_gbp: int | float = Currency_Converter.currency_converter(3141, base='CHF', destiny='GBP')

    print("\n\033[32mResults\033[0m :\n")
    print(f"  • 2718.00 (USD) is: {usd_to_jpy:,} (JPY) ;")
    print(f"  • 1618.00 (EUR) is: {eur_to_brl:,} (BRL) ;")
    print(f"  • 3141.00 (CHF) is: {chf_to_gbp:,} (GBP) ;")
