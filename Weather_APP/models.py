import colorama as clr

from datetime import datetime as dt
from dataclasses import dataclass


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
        
        return return_str
