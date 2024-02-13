# /----------------------------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a simple Habit Tracker created in Python language - version 3.12 or higher - with dependencies on the "pandas", "pyarrow" and "tabulate" libraries.
#                                      To run it properly, make sure you have these frameworks in your virtual environment.
#                                                              ~ Code Created in 02/10/2024 ~
# \----------------------------------------------------------------------------------------------------------------------------------------------------------------/

import os
import datetime as dt

from dataclasses import dataclass, field
from datetime import datetime

import pandas as pd
import tabulate


@dataclass(order=True, frozen=False)
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str

    sort_index: str = field(init=False, repr=False)

    def __post_init__(self):
        self.sort_index = self.name


def track_habit(habit_name: str, when_started: datetime, /, *, cost_per_day: float, minutes_per_day: float) -> Habit:

    """
    
     Creates and returns an instance of the Habit data class containing 
    information about the data provided in the function parameters.

    :param habit_name: String with the Name of the Respective Habit.
    :param when_started: An Instance of the Datetime Class Informing the Day on Which the Habit was Given Up.
    :param cost_per_day: A Float with Daily Spend from the Corresponding Habit.
    :param minutes_per_day: A Float Containing the Daily Time in Minutes Spent on the Abandoned Habit.

    :return: An Instance of the Habit Class with the Provided Data Processed.
    
    """

    base_days_goal: int = 60
    hourly_wage: int = 10

    # Convert Timestamp into Hours / Days :
    time_elapsed: float = (dt.datetime.now() - when_started).total_seconds()
    hours_elapsed: float = round(time_elapsed / (60 * 60), 2)
    days_elapsed: float = round(hours_elapsed / 24, 2)

    # Bonus Details :
    money_saved: float = cost_per_day * days_elapsed
    minutes_used: float = round(minutes_per_day * days_elapsed)
    total_money_saved: str = f"$ {money_saved + (minutes_used / 60 * hourly_wage):,.2f}"

    # Amount of Days Remaining Until you Break a Habit :
    days_to_reach_goal: float | str = round(base_days_goal - days_elapsed)

    # Displayable Info :
    remaining_days: str = 'Cleared!' if days_to_reach_goal <= 0 else f'{days_to_reach_goal:,.2f}'
    time_since: str = f'{days_elapsed} Days' if hours_elapsed > 72 else f'{hours_elapsed} Hours'


    return Habit(name=habit_name,
                 time_since=time_since,
                 remaining_days=remaining_days,
                 minutes_saved=minutes_used,
                 money_saved=total_money_saved)


if __name__ == '__main__':

    os.system('cls')  # Clean the Terminal
    
    # Hypothetical Habits Test
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2024, 1, 7, 8), cost_per_day=1, minutes_per_day=5),
        track_habit('Wasting Time', datetime(2023, 11, 19, 14), cost_per_day=10, minutes_per_day=60 * 3),
        track_habit('Alcohol', datetime(2023, 12, 25, 22), cost_per_day=12, minutes_per_day=20),
        track_habit('Sugar Drinks', datetime(2024, 2, 9, 12), cost_per_day=1, minutes_per_day=3)
    ]

    habits.sort(key=lambda x: x.name)  # Sorts the List Based on Lexicographic Criteria

    habits_data_frame = pd.DataFrame(habits)
    habits_data_frame.index += 1  # To Reformat the Counting Index from 0 to 1

    print(tabulate.tabulate(habits_data_frame, headers='keys', tablefmt='psql'))


    print("\nPress Enter to Close...")
    os.system('pause > nul'); os.system('cls')  # Pause the Program and Close it Cleaning the Terminal
