from models import Coordinates, Weather, dt

import requests
import json
import os

from geopy.distance import geodesic
from geopy.geocoders import Nominatim

from typing import Final, Generator
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
    
    if mock and os.path.isfile(".\\dummy_data.json"):
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

    if not (days := weather.get('list')):
        raise Exception(f'Error: Problem with Json: {weather}')
    
    list_of_weather_data: list[Weather] = []

    for day in days:
        current_weather: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                                           weather_details=(details := day.get('main')),
                                           temperature=f"{details.get('temp') - 273.15:.2f}",
                                           weather=(temp_weather := day.get('weather')),
                                           description=temp_weather[0].get('description'))
        
        list_of_weather_data.append(current_weather)
    
    return list_of_weather_data


if __name__ == '__main__':

    # location: str = input("• Insert a Valid Adress / Location :\n>>> ")
    location: str = 'Tokyo'

    # Getting the Weather Detais :
    # (To get Real Time Data, just Change "mock" parameter to "False")
    print("Getting Details...", end='', flush=True)
    current_weather: dict | None = get_weather(location, mock=True)
    print('\r' + ' ' * len("Getting Details..."), end='\r')

    if current_weather:

        weather_info: list[Weather] = get_weather_details(current_weather)

        days_group: list[str] = sorted(set(f"{wtr.date:%m/%d/%Y}" for wtr in weather_info))

        for day in days_group:

            weather_grouped: Generator[Weather, None, None] = (wtr for wtr in weather_info \
                                                            if f"{wtr.date:%m/%d/%Y}" == day)

            print(f"\n{'/' + f"{day:-^20}" + '\\':^{32 + len(location)}}")

            for wtr in weather_grouped:
                print(f"\n{f"{location.title()}: {wtr}":^{50 + len(location)}}", end='')
            
            print(f"\n{'\\' + '-' * (30 + len(location)) + '/':^{30 + len(location)}}")
            