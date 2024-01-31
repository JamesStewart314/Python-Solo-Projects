# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 01/30/2024
# \ ----------------------------------------------------------------------------------------- / #

import os
import shutil


def create_folder(path: str, extension: str, /) -> str:

    """Creates a folder that is named with "files" and the extension of the file passed in."""

    folder_name: str = "files " + extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path


def sort_files(source_path: str) -> None:

    """Sorts files based on a given path."""

    for root_directory, *_, filenames in os.walk(source_path):
        for filename in filenames:
            
            file_path: str = os.path.join(root_directory, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


def remove_empty_folders(source_path: str) -> None:
    
    """Removes all empty folders"""

    for root_directory, sub_directory, _ in os.walk(source_path, topdown=False):
        for current_directory in sub_directory:
            folder_path: str = os.path.join(root_directory, current_directory)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main() -> None:

    input_source_path: str = input("Please, provide a file path to sort: ")

    if os.path.exists(path=input_source_path):
        sort_files(input_source_path)
        remove_empty_folders(input_source_path)
    
    else:
        print("Invalid Path. Please, provide a valid file path.")
        os.system('pause > nul')
        os.system('cls')

        return main()

    return None


if __name__ == '__main__':
    os.system('cls')
    main()
