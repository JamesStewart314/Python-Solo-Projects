# /----------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Distance Calculator created in Python language - version 3.12 or higher - with dependencies on the "geopy" library.
#                         To run it properly, make sure you have this framework in your virtual environment.
#                                                   Code Created in ~ 02/13/2024 ~
# \----------------------------------------------------------------------------------------------------------------------------------/

import os

from dataclasses import dataclass
from typing import Literal

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

type Numeric = int | float
type distance_units = Literal['km', 'm', 'mi', 'ft', 'nm']


@dataclass(order=False, frozen=True)
class Coordinates:
    latitude: Numeric
    longitude: Numeric

    @property
    def coordinates(self) -> tuple[Numeric , Numeric]:
        return (self.latitude, self.longitude)


def get_coordinates(adress: str, /) -> Coordinates | None:

    # Returns an instance of the Coordinates class corresponding to the given address.

    geolocator: Nominatim = Nominatim(user_agent='distance_calculator')
    location = geolocator.geocode(adress)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance(base_adress: str, destiny_adress: str, /, *, unit_of_measurement: distance_units) -> float | None:

    # Calculates and returns the distance between two addresses
    # in a unit of measurement specified by the "unit_of_measurement" parameter.
    
    Cbase_adress: Coordinates | None = get_coordinates(base_adress)
    Cdestiny_adress: Coordinates | None = get_coordinates(destiny_adress)
    
    if Cbase_adress and Cdestiny_adress:
        if (geodesic_distance := geodesic(Cbase_adress.coordinates, Cdestiny_adress.coordinates)):

            match  unit_of_measurement:
                case 'km':
                    distance: float = geodesic_distance.km
                case 'mi':
                    distance: float = geodesic_distance.mi
                case 'ft':
                    distance: float = geodesic_distance.ft
                case 'm':
                    distance: float = geodesic_distance.m
                case 'nm':
                    distance: float = geodesic_distance.nm
                case _:
                    distance: float = geodesic_distance.km
                
            if __name__ == '__main__':
                print(f"\033[33m{base_adress.title()}\033[0m >--->> \033[32m{destiny_adress.title()}\033[0m :\n")
                print(f"• Distance: ~ {distance:,.2f} {unit_of_measurement} (apx)")


            return round(distance, 2)
        
        else:
            if __name__ == '__main__':
                print(f"Failed to Calculate Distance.")

            return None
    

if __name__ == '__main__':

    os.system('cls')
    
    initial_adress: str = 'Rio de Janeiro 314, Rio de Janeiro, Brazil'
    target_adress: str = input('Enter an Adress: ')
    print("Calculating...\n")

    print(calculate_distance(initial_adress, target_adress, unit_of_measurement='km'))
