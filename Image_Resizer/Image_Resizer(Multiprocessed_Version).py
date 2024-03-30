# /----------------------------------------------------------------------------------------------\
#      This code is a Image Resizer created in Python language - version 3.12 or higher
#                              library dependencies: "pillow"
#       To run it properly, make sure you have this package in your virtual environment.
#                                  Code Created in ~ 03/22/2024 ~
# \----------------------------------------------------------------------------------------------/


import itertools
import multiprocessing
import os
import shutil
import time

from PIL import Image as IMG

from itertools import count
from PIL.Image import Image

from typing import Any, Final, Generator

type ImageGen = Generator[tuple[str, tuple[int, int]], None, None]


# Supported Image File Extensions :
supported_extensions: Final[set[str]] = {".jpg", ".jpeg", ".png"}


def move_image(image: str, destiny_folder: str, /) -> None:
    shutil.move(image, destiny_folder)


def resize_image(image_path: str, new_dimensions: tuple[int, int], /) -> str:

    """
     As the name of the function suggests, it resizes the width and 
    height of an image file.

    :param image_path: The path corresponding to the 
     image file contained on your computer.
    :type image_path: string

    :param new_dimensions: The new dimensions - width and height, respectively - 
     in which the image will be resized.
    :type new_dimensions: tuple[int, int]

    :return: A string containing the full name of the new resized image.
    :rtype: string
    """
    
    if not isinstance(image_path, str):
        raise TypeError("\'image_path\' parameter must be \'str\' type.")
    
    if not isinstance(new_dimensions, tuple):
        raise TypeError("\'new_dimensions\' parameter must be of type \'tuple\'")
    
    if not (len(new_dimensions) == 2 and\
           all((isinstance(number, int) and number > 0)\
           for number in new_dimensions)):
        
        # checking if the 'new_dimensions' parameter corresponds 
        # to a tuple containing two non-zero positive integers.

        raise ValueError("\'new_dimensions\' parameter must be a tuple that "\
                        "contains only two non-zero positive integers.")
    
    if not os.path.isfile(image_path):
        raise FileNotFoundError("The image path provided is invalid or does not exist.")

    if not (extension := os.path.splitext(image_path)[-1]) in supported_extensions:
        raise ValueError(f"File extension \'{extension}\' is not supported. "\
                        f"Available extensions: {supported_extensions}")
    
    with IMG.open(image_path) as image_object:

        new_image: Image = image_object.resize(new_dimensions)
        base_name: str = (bs_name := os.path.basename(image_path))[:bs_name.rindex('.')]
        aux_counter: count = itertools.count(start=0)

        while os.path.isfile((new_name := base_name + '_copy-' +\
                            str(next(aux_counter)).zfill(3) + extension)): pass
        
        new_image.save(new_name)

        return new_name


def resize_multiple_images(folder_path: str, new_dimensions: tuple[int, int]) -> None:

    """
     Function used to resize multiple images present in the same directory.
    
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
    

    # The use of generators was prioritized over lists to minimize 
    # excessive memory expenditure at the expense of a small 
    # portion of performance :
    image_files: ImageGen = ((os.path.join(folder_path, image_name), new_dimensions) for \
                             image_name in filter(lambda x: os.path.splitext(x)[-1] in \
                             supported_extensions, os.listdir(folder_path)))
    

    # Making sure that the name chosen for the new folder that will 
    # contain the resized images does not exist :
    aux_counter: count = itertools.count(start=0)
    while os.path.exists((new_folder_name := os.path.join(folder_path,
                        f"resized_images ({new_dimensions[0]}x{new_dimensions[1]})"\
                        f" - {str(next(aux_counter)).zfill(3)}"))): pass
    
    os.mkdir(new_folder_name)
    
    with multiprocessing.Pool() as pool:
        results: Generator[str, None, None] = (img_name for img_name in pool.starmap(resize_image, image_files))
        pool.starmap(move_image, ((new_image, new_folder_name) for new_image in results))

    return None


def _main(args: Any = None) -> None:
    
    os.system('cls')

    while not os.path.exists(input_path := input("Provide the Path of a Folder"\
                                                 " or Image to Resize them:\n>>> ")):
        
        print("\n\033[33mInvalid Path! Please, check that the input provided"\
              "matches a valid path and try again.\033[0m")
        
        print("\n\033[32m• e.g.: \"C:\\Users\\myUser\\hypothetical_folder_path\"," \
              f"\"C:\\Users\\myUser\\hypothetical_image.png\", ...\033[0m")
        
        print("(press any key to continue...)", end='')

        os.system('pause > nul & cls')
    
    os.system('cls')

    while True:
        try:
            message: str = "Great! "

            file_base_name: str = os.path.basename(input_path)

            if (is_file := os.path.isfile(input_path)):
                message += f"You chose to resize a single image file. "\
                        f"(file name: {file_base_name})\n"
            else:
                message += f"You have chosen to resize the multiple images present "\
                        f"in the \"{file_base_name}\" folder.\n"
            
            print("• Images Being Resized:\n│", end='')

            if is_file:
                print(f"\n└> \" {file_base_name} \"")

            else:
                for file_name in os.listdir(input_path):
                    if os.path.splitext(file_name)[-1] in supported_extensions:
                        print(f"\n└> \" {(base_name := os.path.basename(file_name)):<{(size := min(len(base_name), 80))}.{size}} \" ;", end='', flush=True)

                print('\b \n')
            print()
            
            message += "Now enter the new dimensions to resize the selected images"\
                    " (e.g.: \"200x400\", \"480x480\", ...)\n>>> "
                
            input_dimensions: tuple[int, ...] = tuple(map(int, input(message).split('x')))

            if len(input_dimensions) != 2:
                raise Exception("Invalid resize format. Please try to enter two "\
                                "non-zero positive integer values as guided in "\
                                "the examples provided.")
            
            if not all(number > 0 for number in input_dimensions):
                raise ValueError(f"\nValue Error: Please, try to enter two non-zero "\
                  "positive integer values as guided in the examples provided.")
            
            # All entries are formatted correctly, 
            # the loop can be terminated :
            break
        
        except ValueError as error:
            print(error)
            print("(press any key to continue...)", end='')
            os.system('pause > nul & cls')

        except Exception as error:
            print(f"\nError: {error}")
            print("(press any key to continue...)", end='')
            os.system('pause > nul & cls')

    print("\nDoing the Process. Please, wait...", end='')

    if is_file:
        move_image(resize_image(input_path, input_dimensions),\
                     os.path.abspath(os.path.dirname(input_path)))
    else:
        resize_multiple_images(input_path, input_dimensions)

    print("\b \r• Done! Press any key to close... ", end='')

    os.system('pause > nul')

    print("\n~ Thanks for Using this Program! Closing in... ", end='')
    for i in range(3, 0, -1):
        print(i, end='', flush=True)
        time.sleep(1)
        print('\b', end='')
    
    os.system('cls')


if __name__ == '__main__':
    _main()
