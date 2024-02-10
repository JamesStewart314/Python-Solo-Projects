# /---------------------------------------------------------------------------------------------------------------------------\
#  This code is a File Sorter created in Python language - version 3.12 or higher - with dependencies on the "flask" library.
#                  To run it properly, make sure you have this package in your virtual environment.
#                                                Code Created in ~ 02/09/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------/

import datetime as dt
import random as rdm

from datetime import datetime

import flask
from flask import Flask

#
#  Some Tests: 
# • <link>/api/random?number=90&text=hello
# • <link>/api/random?number=potato
#

APP: Flask = flask.Flask(__name__)

@APP.route('/')
def index() -> dict[str, str | datetime]:
    phrases: list[str] = ["Welcome to this Page!", "You\'re Looking Great Today!", "The Weather is Great!"]
    
    return {'phrase': rdm.choice(phrases), 'Date': dt.datetime.now()}


@APP.route('/api/random')
def random():

    number_input: int | None = flask.request.args.get('number', type=int)
    text_input: str = flask.request.args.get('text', type=str, default="default_text")

    if isinstance(number_input, int):

        return {'input': number_input,
                'random': rdm.randint(0, number_input),
                'text': text_input,
                'date': dt.datetime.now()}
    else:
        return {'Error': 'Please, Only Enter Numbers.'}


if __name__ == '__main__':
    APP.run()
