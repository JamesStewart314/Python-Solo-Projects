# /-----------------------------------------------------------------------------------------------------------------------------------\
#  This code is a File Sorter created in Python language - version 3.12 or higher - with dependencies on the "customtkinter" library.
#                  To run it properly, make sure you have these frameworks in your virtual environment.
#                                                Code Created in ~ 01/30/2024 ~
# \-----------------------------------------------------------------------------------------------------------------------------------/


import os
import shutil

import customtkinter as ctk

ctk.set_appearance_mode('dark')


class FileSorter:

    @staticmethod
    def create_directory(path_root: str, extension: str | None = None, /) -> str:

        directory_name: str = "Files " + extension[1:] if extension else "Files With No Extension"
        directory_path: str = os.path.join(path_root, directory_name)
        
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        return directory_path


    @staticmethod
    def erase_empty_directories(directory_path_to_clean: str, /) -> None:

        for root_path, sub_directories, *_ in os.walk(directory_path_to_clean, topdown=False):
            for current_directory in sub_directories:
                folder_path: str = os.path.join(root_path, current_directory)

                if not os.listdir(folder_path):
                    os.rmdir(folder_path)
    

    @staticmethod
    def make_sort(directory_path_to_sort: str, /) -> None:

        for root_path, *_, filenames in os.walk(directory_path_to_sort):
            for filename in filenames:
                file_path: str = os.path.join(root_path, filename)
                extension: str = os.path.splitext(filename)[1]

                if extension:
                    destiny_folder_path: str = FileSorter.create_directory(root_path, extension)
                    shutil.move(file_path, destiny_folder_path)
                else:
                    destiny_folder_path: str = FileSorter.create_directory(root_path)
                    shutil.move(file_path, destiny_folder_path)
                
        FileSorter.erase_empty_directories(directory_path_to_sort)  # To clean the empty folders.
    

    def __init__(self, window_title: str, width: int, height: int) -> None:
        
        self._width = width
        self._height = height
        
        self._window = ctk.CTk()
        self._window.geometry(f"{self._width}x{self._height}")  # Establishing the dimensions of the window.
        self._window.title(window_title)  # Giving the window a title
        self._window.resizable(False, False)  # Window is not resizable in any direction.

        # Info Label :
        self._window_title = """           ╔═══════════════╗\n           ╠    ▓▒░  FILE SORTER  ░▒▓    ╣\n           ╚═══════╬═══════╝"""
        self._display_window_title = ctk.CTkLabel(self._window, text=self._window_title, text_color='yellow')
        self._display_window_title.place(x=70, y=(self._height // 20))

        self._info_message = "This Program Sorts your Files\nPlease, Provide a Valid Folder Path to Sort Files by their Extension\n(Example: C:\\Users\\MyUser\\MyUnsortedFolder)"
        self._display_info_message = ctk.CTkLabel(self._window, text=self._info_message, text_color='green')
        self._display_info_message.place(x=25, y=70)

        # Path Input Label :
        self._input_entry = ctk.CTkEntry(self._window, width=400)
        self._input_entry.place(x=15, y=130)

        self._sort_button = ctk.CTkButton(self._window, text='sort now', corner_radius=200, text_color='green', fg_color=('black', 'black'), command=self.sort_files)
        self._sort_button.place(x=145, y=200)
    
    
    def sort_files(self) -> None:

        self._temp_message = ctk.CTkLabel(self._window, text_color='red')
        self._temp_message.place(x=60, y=250)
        
        root_path: str = self._input_entry.get().strip()

        if os.path.exists(root_path):
            self._temp_message.place(x=0, y=250)
            self._temp_message.configure(text=f"{(t := "          Processing Your Files, Please Wait..."):^100}", text_color='yellow')
            FileSorter.make_sort(self._input_entry.get())
            self._temp_message.configure(text=f"{(t := "   Done !"):^130}", text_color='white')

        else:
            self._temp_message.configure(text="Invalid Path!\n Please, Check if the Given Path is Correct and it Exists")
    

    def run(self) -> None:
        self._window.mainloop()


if __name__ == '__main__':
    mysorter = FileSorter("File Sorter +", 430, 300)
    mysorter.run()
