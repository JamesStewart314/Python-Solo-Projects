# /---------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Image Downloader created in Python language - version 3.12 or higher - with dependencies on the "requests" library.
#                        To run it properly, make sure you have this package in your virtual environment.
#                                                   Code Created in ~ 01/29/2024 ~
# \---------------------------------------------------------------------------------------------------------------------------------/

import os
import itertools

import requests


def get_extension(image_url: str, /) -> str | None:
    
    extensions_type: tuple[str, ...] = ('.png', '.jpg', '.jpeg', '.gif', '.svg')
    
    for extension in extensions_type:
        if extension in image_url:
            return extension
    
    return None


def download_image(image_url: str, name: str, /, folder: str | None = None) -> None:

    if extension := get_extension(image_url):
        image_name: str = f"{folder}/{name}{extension}" if folder else f"{name}{extension}"

    else:
        raise Exception("Image Extension Could not be Located.")

    temp_counter = itertools.count(start=1)
    while os.path.isfile(image_name):  # If file name already exists :
        image_name = f"{folder}/{name}({next(temp_counter)}){extension}"
    
    # Download image :
    try:
        image_content: bytes = requests.get(image_url).content

        with open(image_name, 'wb') as handler:
            handler.write(image_content)
        
    except Exception as error:
        print(f"Error: {error}")
    
    else:
        if __name__ == '__main__':
            print(f"Your Image has Downloaded \033[32mSucessfuly\033[0m! (\"{image_name}\")")
    
    finally:
        if __name__ == '__main__':
            print("The Program has Finished.")


if __name__ == '__main__':
    
    input_url: str = input("Enter an image URL: \n>>> ").strip()
    input_name: str = input("What would you like to name it? : \n>>> ").strip()

    print("Downloading...")
    download_image(input_url, input_name, folder='images')

