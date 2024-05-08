# /----------------------------------------------------------------------------------------------\
#      This code is a Image Resizer created in Python language - version 3.12 or higher
#                          library dependencies: "pillow" ; "tqdm"
#       To run it properly, make sure you have this package in your virtual environment.
#                               Code Created in ~ 03/29/2024 ~
# \----------------------------------------------------------------------------------------------/


from models import istarmap

import itertools
import multiprocessing
import os
import shutil
import time

import tqdm
from PIL import Image as IMG

from itertools import count
from PIL.Image import Image
from typing import Any, Final, Generator

type ImageGen = Generator[tuple[str, tuple[int, int], str], None, None]


# Supported Image File Extensions :
supported_extensions: Final[set[str]] = {".jpg", ".jpeg", ".png"}


def pause_term(message: str | None = None, /) -> None:
    # function to pause the terminal
    if message:
        print(message)

    os.system('pause > nul' if os.name == 'nt' else 'read -n 1 -s -r -p ""')


def clear_term() -> None:
    # function to clean the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def _custom_clear() -> None:

    #
    #      Using ANSI codes to do respectively :
    #
    #  • return the cursor to beginning of line ;
    #  • clear everything in front of the cursor on the same line ;
    #  • move the cursor one line up ;
    #  • clear everything in front of the cursor on the same line ;
    #  • move the cursor two lines up ;
    #  • clear everything in front of the cursor on the same line ;
    #  • move the cursor three lines up.
    #
    # 
    # Although I recognize that this approach is unconventional and 
    # may make future maintenance difficult, I chose to apply it on this 
    # occasion to explore the practical use of ANSI codes. It is important 
    # to highlight that this practice is strongly discouraged in production 
    # and enterprise collaboration environments.
    #

    print('\r\033[K\033[1A\033[K\033[2A\033[K\033[3A', flush=True)


def display_ending_message(message: str = "", /) -> None:
    print(message, end='')
    
    for i in range(3, 0, -1):
        print(i, end='', flush=True)
        time.sleep(1)
        print('\b', end='')

    print('\r\033[K')


def move_image(image_path: str, destiny_folder: str, /) -> None:
    # function to move an image to a specific directory
    shutil.move(image_path, destiny_folder)


def resize_image(image_path: str, new_dimensions: tuple[int, int], 
                 destiny_folder: str | None = None, /) -> str:

    """
     As the name of the function suggests, it resizes the width and
    height of an image file and saves the new copy of the resized image
    in the same directory where the code is contained if the "destiny_folder" 
    parameter is not provided. Otherwise, the image will be stored in the path 
    corresponding to the parameter in question.

    :param image_path: The path corresponding to the 
     image file contained on your computer.
    :type image_path: string

    :param new_dimensions: The new dimensions - width and height, respectively - 
     in which the image will be resized.
    :type new_dimensions: tuple[int, int]

    :param destiny_folder: This parameter refers to the final directory 
     path that should contain the duplicate of the resized image. 
     If a path is not explicitly specified, the folder that will contain 
     the copy of the resized image will be the one where this 
     code file is located. 
    :type destiny_folder: string | None

    :return: A string containing the full name of the new resized image.
    :rtype: string
    """
    
    if not isinstance(image_path, str):
        raise TypeError("\'image_path\' parameter must be \'str\' type.")
    
    if not isinstance(new_dimensions, tuple):
        raise TypeError("\'new_dimensions\' parameter must be of type \'tuple\'")

    if destiny_folder and not (isinstance(destiny_folder, str) and os.path.isdir(destiny_folder)):
        
        # Checking that the "destiny_folder" parameter is not None and 
        # indicates a valid directory path on the computer.

        raise ValueError("The \'destiny_folder\' variable must be of type str "\
                         "and must reference a valid directory path on your computer.")
    
    if not (len(new_dimensions) == 2 and\
           all((isinstance(number, int) and number > 0)\
           for number in new_dimensions)):
        
        # Checking if the 'new_dimensions' parameter corresponds 
        # to a tuple containing two non-zero positive integers.

        raise ValueError("\'new_dimensions\' parameter must be a tuple that "\
                        "contains only two non-zero positive integers.")
    
    if not os.path.isfile(image_path):
        raise FileNotFoundError("The image path provided is invalid or does not exist.")

    image_base_info: tuple[str, str] = os.path.splitext(image_path)

    if not (extension := image_base_info[-1]) in supported_extensions:
        raise ValueError(f"File extension \'{extension}\' is not supported. "\
                        f"Available extensions: {supported_extensions}")
    
    with IMG.open(image_path) as image_object:

        new_image: Image = image_object.resize(new_dimensions)
        new_name: str = image_base_info[0] + '-new_copy' + extension
        
        # Saving the Image :
        new_image.save(os.path.join(destiny_folder, os.path.basename(new_name)) \
                       if destiny_folder else new_name)

        return new_name


def resize_multiple_images(folder_path: str, new_dimensions: tuple[int, int], 
                           number_of_images: int, /) -> None:

    """
     The purpose of this function is to create resized copies of multiple 
    images present in the same directory, grouping them in a new subfolder 
    whose nomenclature is derived from the dimensions of the resized images.
    
    :param folder_path: The path corresponding to the directory whose 
     images should be resized.
    :type folder_path: string

    :param new_dimensions: The new dimensions - width and height, respectively - 
     in which the image will be resized.
    :type new_dimensions: tuple[int, int]

    :return: None
    :rtype: None
    """

    if not isinstance(folder_path, str):
        raise TypeError("\'folder_path\' parameter must be \'str\' type.")

    if not os.path.isdir(folder_path):
        raise ValueError("The given folder path is invalid or does not exist.")

    # Making sure that the name chosen for the new folder that will 
    # contain the resized images does not exist :
    aux_counter: count = itertools.count(start=0)
    while os.path.exists((new_folder_name := os.path.join(folder_path,
                        f"resized_images ({new_dimensions[0]}x{new_dimensions[1]})"\
                        f" - {str(next(aux_counter)).zfill(3)}"))): pass
    
    os.mkdir(new_folder_name)

    # The use of generators was prioritized over lists to minimize 
    # excessive memory expenditure at the expense of a small 
    # portion of performance :
    image_files: ImageGen = ((os.path.join(folder_path, image_name), new_dimensions, new_folder_name) for \
                             image_name in filter(lambda x: os.path.splitext(x)[-1] in \
                             supported_extensions, os.listdir(folder_path)))
    
    with multiprocessing.Pool() as pool:
        
        # Progress Bar Possible Styles:
        # 1°: " ▏▎▍▌▋▊▉█"
        # 2°: " >═"
        # 3°: " ░▒▓"

        for _ in tqdm.tqdm(pool.istarmap(resize_image, image_files), 
                                  total=number_of_images,
                                  desc=f"\033[3m\033[1m• Loading\033[0m\033[31m."\
                                       "\033[33m.\033[34m.\033[0m",
                                 ncols=100,
                                 ascii=" ░▒▓",
                                 bar_format="{desc} ~{percentage:3.0f}% - [{bar}] - {n_fmt}/{total_fmt}"\
                                            " | Time Elapsed: {elapsed} ~ ETA: {remaining}",
                                 smoothing=0.8,
                                 colour='green'): pass
                                     
    return None


def _main(args: Any = None) -> None:
    
    clear_term()

    while not os.path.exists(input_path := input("Provide the Path of a Folder"\
                                                 " or Image to Resize them:\n>>> ")):
        
        print("\n\033[33mInvalid Path! Please, check that the input provided"\
              "matches a valid path and try again.\033[0m")
        
        print("\n\033[32m• e.g.: \"C:\\Users\\myUser\\hypothetical_folder_path\"," \
              f"\"C:\\Users\\myUser\\hypothetical_image.png\", ...\033[0m")
        
        print("(press any key to continue...)", end='')

        # Pausing and subsequently cleaning the terminal :
        pause_term() ; clear_term()
    
    clear_term()

    message: str = "Great! "

    file_base_name: str = os.path.basename(input_path)

    if (is_file := os.path.isfile(input_path)):
        message += f"You chose to resize a single image file. "\
                   f"(file name: {file_base_name})\n"

    else:
        folder_content: list[str] = os.listdir(input_path)

        message += f"You have chosen to resize the multiple images present "\
                   f"in the \"{file_base_name}\" folder.\n"
        
    message += "Now enter the new dimensions to resize the selected images"\
               " (e.g.: \"200x400\", \"480x480\", ...)\n>>> "
    
    print("• Images Being Resized:\n│", end='')

    if is_file:
        print(f"\n└> \" {file_base_name} \"")

    else:
        for file_name in folder_content:
            if os.path.splitext(file_name)[-1] in supported_extensions:
                print(f"\n└> \" {(base_name := os.path.basename(file_name)):<{(size := min(len(base_name), 80))}.{size}} \" ;", end='', flush=True)

        print('\b \n')
    print()

    while True:

        try:
            input_dimensions: tuple[int, ...] = tuple(map(int, input(message).split('x')))

            if len(input_dimensions) != 2:
                raise Exception("Invalid resize format. Please try to enter two "\
                                "non-zero positive integer values as guided in "\
                                "the examples provided above.")
            
            if not all(number > 0 for number in input_dimensions):
                raise ValueError(f"\nValue Error: Please, try to enter two non-zero "\
                  "positive integer values as guided in the examples provided.")
            
            # All entries are formatted correctly, 
            # the loop can be terminated :
            break

        except ValueError as error:
            print("\nInvalid image format! Enter a valid format as "\
                  "per the examples provided above.")
            print("(press any key to continue...)", end='')
            # Pausing and subsequently cleaning the last two lines :
            pause_term() ; _custom_clear()

        except Exception as error:
            print(f"\nError: {error}")
            print("(press any key to continue...)", end='')
            # Pausing and subsequently cleaning the last two lines :
            pause_term() ; _custom_clear()

    if is_file:
        resize_image(input_path, input_dimensions, os.path.abspath(os.path.dirname(input_path)))
    else:
        resize_multiple_images(input_path, input_dimensions, 
           sum(1 for _ in filter(lambda x: os.path.splitext(x)[-1] in \
                                 supported_extensions, folder_content)))

    pause_term("\n• Done! Press any key to close... ")

    display_ending_message("\n~ Thanks for Using this Program! Closing in... ")
    clear_term()


if __name__ == '__main__':
    _main()
