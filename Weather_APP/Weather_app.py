# /---------------------------------------------------------------------------------------------------\
#  This code is a Weather App created in Python language - version 3.12 or higher - with dependencies 
#                         on the "requests", "colorama" and "geopy" libraries.
#         To run it properly, make sure you have these packages in your virtual environment.
#                                    Code Created in ~ 02/19/2024 ~
# \---------------------------------------------------------------------------------------------------/


from models import Coordinates, Weather, dt, ThreadWithReturnValue

import itertools
import json
import os
import time

import requests
import colorama as clr

from geopy.geocoders import Nominatim

from typing import Final, Any
from itertools import cycle
from requests import Response


API_KEY: Final[str] = '79abab032c366e93d4e9f1ca85f06f19'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_coordinates(adress: str, /) -> Coordinates | None:

    # Returns an instance of the Coordinates 
    # class corresponding to the given address.

    geolocator: Nominatim = Nominatim(user_agent='distance-calculator')

    if (location := geolocator.geocode(adress)):
        return Coordinates(latitude=location.latitude, longitude=location.longitude)
    

def get_weather(city_name: str, *, mock: bool = True) -> dict | None:

    """
    
     Returns a dictionary containing information 
    regarding the weather in a location specified 
    by the "city_name" parameter if the "mock" 
    parameter is False. Otherwise, it returns a 
    dictionary with the information present in the 
    last climate analysis, contained in the 
    "dummy_data.json" file.

    :param city_name: String containing the name of a 
     city, region or home address. (e.g.: "Moscow", "New York", etc)
    :param mock: A Boolean value to determine whether 
     the information provided should come from stored 
     data or real-time analytics.

    :return: A dictionary containing information, 
     whether outdated or not, relating to the 
     climate in a given location.
    
    """
    
    if mock and os.path.exists(".\\dummy_data.json"):
        with open('dummy_data.json') as json_file:
            return json.load(json_file)
    
    if (location := get_coordinates(city_name)):

        # Request Live Data :
        payload: dict = {'appid': API_KEY, 'lat': location.latitude, 'lon': location.longitude}
        request: Response = requests.get(url=BASE_URL, params=payload)
        data = request.json()

        with open('dummy_data.json', 'w') as json_file:
            json.dump(data, json_file)
        
        return data


def get_weather_details(weather: dict, /) -> list[Weather]:

    """
    
     Processes weather information provided 
    by the "get_weather()" function.

    :param weather: A dictionary containing 
     climate information.
    
    :return: A list of Weather class objects 
     with all the weather data for the next 
     few days in a given location.
    
    """

    if not (days := weather.get('list')):
        raise Exception(f'Error: Problem with Json: {weather}')
    
    list_of_weather_data: list[Weather] = []

    for day in days:
        current_weather: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                                           weather_details=(details := day.get('main')),
                                           temperature=f"{details.get('temp') - 273.15:.2f}",
                                           weather=(temp_weather := day.get('weather')),
                                           main_weather=temp_weather[0].get('main'),
                                           description=temp_weather[0].get('description'))
        
        list_of_weather_data.append(current_weather)
    
    return list_of_weather_data


def _main(args: Any = None) -> None:
    
    # I'm using Threads and the cyclical animations below for 
    # purely aesthetic purposes, none of these resources are 
    # essential for the code to work, I would just like to test 
    # my programming skills with this simple artistic detail ;)

    bar_animation: cycle = itertools.cycle(['\\', '|', '/', '-'])
    ellipsis_animation: cycle = itertools.cycle(['.', '..', '...'])

    #####################################################################################
    # ! (To get Real Time Data, Just Change "mock_data" Flag Right Below to "False") !  #
    #####################################################################################
    mock_data: bool = True

    location: str = input("• Insert a Valid Adress / Location :\n>>> ").strip().lower() \
                         if not mock_data else 'Tokyo'
    # location: str = 'Tokyo'

    # Getting the Weather Detais :
    current_weather_thread: ThreadWithReturnValue = ThreadWithReturnValue(target=get_weather, args=(location,), kwargs={'mock': mock_data})
    current_weather_thread.start()

    while current_weather_thread.is_alive():
        print(f"{clr.Fore.GREEN}• Getting Details{clr.Style.RESET_ALL}", f"{next(ellipsis_animation):<4}", next(bar_animation), sep='', end='', flush=True)
        time.sleep(0.5)
        print('\r', end='')
    
    print('\r' + ' ' * 22, end='\r')
    
    current_weather: dict | None = current_weather_thread.join()

    if current_weather is not None:

        weather_info: list[Weather] = get_weather_details(current_weather)
        days_group: list[str] = sorted(set(f"{wtr.date:%m/%d/%Y}" for wtr in weather_info))

        for day in days_group:

            weather_grouped: list[Weather] = [wtr for wtr in weather_info if f"{wtr.date:%m/%d/%Y}" == day]

            size_of_weather_message: int = len(max(weather_grouped, key=lambda x: len(x.__str__())).__str__())
            print(f"\n{'/' + f"{day:-^20}" + '\\':^{32 + size_of_weather_message}}")

            for wtr in weather_grouped:
                weather_message: str = f"{location.title()}: {wtr}"
                print(f"{weather_message:^{50 + size_of_weather_message}}")
            
            print(f"{' \\' + '-' * (size_of_weather_message + len(location) - 12) + '/':^{30 + size_of_weather_message}}")


if __name__ == '__main__':
    _main()
