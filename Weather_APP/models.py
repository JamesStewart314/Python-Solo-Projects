from threading import Thread
from datetime import datetime as dt

import colorama as clr

from dataclasses import dataclass
from typing import Any


@dataclass(order=False, frozen=True)
class Coordinates:
    latitude: int | float
    longitude: int | float

    @property
    def coordinates(self) -> tuple[int | float, int | float]:
        return (self.latitude, self.longitude)


@dataclass(order=False, frozen=False)
class Weather:
    date: dt
    temperature: str  # In Celsius
    weather: list[dict]
    weather_details: dict
    main_weather: str
    description: str


    def __str__(self) -> str:

        return_str: str = f"{clr.Fore.LIGHTMAGENTA_EX}[{self.date:%m/%d/%Y} - {self.date:%H:%M}]{clr.Style.RESET_ALL} "

        if float(self.temperature) >= 30:
            return_str += f"{clr.Fore.RED}{self.temperature}{clr.Style.RESET_ALL}°C"
        elif float(self.temperature) >= 20:
            return_str += f"{clr.Fore.YELLOW}{self.temperature}{clr.Style.RESET_ALL}°C"
        elif float(self.temperature) >= 10:
            return_str += f"{clr.Fore.GREEN}{self.temperature}{clr.Style.RESET_ALL}°C"
        else:
            return_str += f"{clr.Fore.BLUE}{self.temperature}{clr.Style.RESET_ALL}°C"
        
        
        match self.main_weather:
            case 'Clear':
                return_str += f" ( {self.main_weather} ☀️ )"
            case 'Clouds':
                return_str += f" ( {self.main_weather} ☁️ )"
            case 'Tornado':
                return_str += f" ( {self.main_weather} 🌪️ )"
            case 'Squall':
                return_str += f" ( {self.main_weather} 🌩️ )"
            case 'Ash':
                return_str += f" ( {self.main_weather} 🌋 )"
            case 'Dust' | 'Sand':
                return_str += f" ( {self.main_weather} ⌛ )"
            case 'Fog' | 'Haze' | 'Mist':
                return_str += f" ( {self.main_weather} 🌁 )"
            case 'Snow':
                return_str += f" ( {self.main_weather} 🌨️ )"
            case 'Rain' | 'Drizzle':
                return_str += f" ( {self.main_weather} 🌧️ )"
            case 'Thunderstorm':
                return_str += f" ( {self.main_weather} ⛈️ )"
            case _:
                return_str += f" ( {self.main_weather} )"

        return return_str


class ThreadWithReturnValue(Thread):
    def __init__(self, group = None, target = None, name = None,
                 args=(), kwargs={}, Verbose = None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    
    def run(self) -> None:
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    
    def join(self, *args) -> Any:
        Thread.join(self, *args)
        return self._return

