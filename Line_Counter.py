# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 02/04/2024
# \ ----------------------------------------------------------------------------------------- / #
#
# I created it just to test the uses of Walrus Operator.
# It was designed to count the lines, words and characters contained in a text file and 
# its use is exclusive through the terminal.
#
# The syntax to use it in the terminal is:
# • python -u <path of this file in quotes> <path of the .txt file in quotes> 
#
# Example:
# • python -u "C:\Users\myuser\Downloads\Line_Counter.py" "C:\Users\myuser\Downloads\MyTextFile.txt"
#

import sys
import pathlib

from pathlib import Path


counter: list[int] | None = None

for file_path in sys.argv[1:]:
    current_file: Path = pathlib.Path(file_path)

    # Counts Lines, Words, Characters and Spaces
    counter: list[int] = [
        (lines := (text := current_file.read_text()).count('\n')),
        len(text.split()),
        (len(text) - lines - text.count(' ')),
        text.count(' ')
    ]


if counter:
    print(f"""
Lines: {counter[0]}
Words: {counter[1]}
Characters: {counter[2]}
Spaces: {counter[3]}
""")

    
