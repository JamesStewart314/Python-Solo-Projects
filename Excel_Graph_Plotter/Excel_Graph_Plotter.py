# /---------------------------------------------------------------------------------------------------\
#        This is a Excel Graph Plotter code created in Python language - version 3.12 or higher
#             library dependencies: "numpy" ; "matplotlib" ; "customtkinter" ; "pillow"
#         To run it properly, make sure you have these packages in your virtual environment.
#                                    Code Created in ~ 02/24/2024 ~
# \---------------------------------------------------------------------------------------------------/


import os
import datetime as dt

import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from typing import Final, Generator, Any
from customtkinter import CTkFont
from numpy import ndarray


ctk.set_appearance_mode("dark")

HERE_PATH: Final[str] = os.path.abspath(os.path.dirname(__file__))
FILE_PATH: Final[str] = os.path.abspath(os.path.join(HERE_PATH, "INFO.csv"))


def make_gen_from_csv(file_path: str, /) -> Generator[dict[str, Any], None, None]:

    file_lines: Generator[Any, None, None] = (info for info in open(file_path))
    # Gets Column Titles from '.csv' File :
    header_line: list[str] = next(file_lines).removesuffix('\n').split(',')

    # Creates a dictionary generator that iterates through the 
    # lines of the file, associating the contents of each line 
    # with its respective column. The dictionary keys are the 
    # column titles and the values are the content referring to 
    # the read line :
    file_line_information: Generator[dict[str, Any], None, None] = \
    ({key: value for key, value in \
    zip(header_line, line_values.removesuffix('\n').split(','))} \
        for line_values in file_lines)
    
    return file_line_information


class GraphPlotCTK:

    """
     A class used to display Excel plots through matplotlib with the help 
    of a visual interface built in the customtkinter library.

    Attributes:
    ----------
    • All attributes of this class are designated for internal use and 
    should be considered private.
    
    Methods:
    -------
    run() -> None
        Initializes the customtkinter window.

    _plot_graph() -> None
        Displays the graph of funds raised by a given company 
        over a period of time.
    
    _open_csv_file() -> None
        Processes the data present in the '.csv' file and 
        opens a new window displaying the available options for modeling 
        the corresponding graph.
    
    Note:
    ------
    Methods that begin with an underscore (_) indicate their private nature, 
    which implies that they should not be accessed outside the class.
    """

    def __init__(self, window_title: str, window_width: int, 
                 window_height: int) -> None:

        # Preventative Check :
        assert all((isinstance(window_title, str), isinstance(window_height, int), 
                    isinstance(window_height, int)))

        self._window_title = window_title
        self._window_width = window_width
        self._window_height = window_height

        self._toplevel_window = None

        # Creating the CTK Window :
        self._ctkwindow = ctk.CTk()
        # Defining Available Fonts :
        self._fonts: dict[str, CTkFont] = {"Helvetica": ctk.CTkFont(family='Helvetica', size=12),
                                 "Bauhaus 93": ctk.CTkFont(family="Bauhaus 93", size=16)}
        # Setting the Window Title :
        self._ctkwindow.title(self._window_title)
        # Resizing the Window :
        self._ctkwindow.geometry(f"{self._window_width}x{self._window_height}")
        # User can't Resize the Window in Any Direction :
        self._ctkwindow.resizable(False, False)

        # Title Label :
        title_str: str = '╔══════════════╗\n' + f'¤╣{"Graph Plotter":^46}╠¤'\
                       + '\n╚══════════════╝'
        self._title_label = ctk.CTkLabel(self._ctkwindow, text=title_str)
        self._title_label.configure(text_color='#A020F0', font=self._fonts.get('Bauhaus 93'))
        self._title_label.place(x=90, y=15)

        # Placing Icons :
        Image_1 = Image.open(os.path.join(HERE_PATH, "Symbol_1.png"))
        self._image_1 = ctk.CTkImage(light_image=Image_1,
                                          dark_image=Image_1, size=(64, 64))
        self._image_1_Label = ctk.CTkLabel(self._ctkwindow, text='', 
                                                image=self._image_1)
        self._image_1_Label.place(x=380, y=8)

        Image_2 = Image.open(os.path.join(HERE_PATH, "Symbol_2.png"))
        self._image_2 = ctk.CTkImage(light_image=Image_2,
                                          dark_image=Image_2, size=(90, 90))
        self._image_2_Label = ctk.CTkLabel(self._ctkwindow, text='', 
                                                image=self._image_2)
        self._image_2_Label.place(x=0, y=2)
        

        # Info Text Label :
        self._info_text_label = ctk.CTkLabel(self._ctkwindow, 
         text="This program opens a file with \'.csv\' extension and "\
         "displays it in a graph.\n\nPlease, provide a valid \'.csv\' file path to "\
         "display it graphically:\n(e.g.: C:\\Users\\MyUser\\Myfolder\\MyFile.csv)")
        self._info_text_label.configure(font=self._fonts.get('Helvetica'), text_color='#FFFF00')
        self._info_text_label.place(x=40, y=80)

        # Entry Label for File Path :
        self._entry_label = ctk.CTkEntry(self._ctkwindow, width=self._window_width-20)
        self._entry_label.configure(border_width=2, border_color='#A020F0', text_color='#449E48')
        self._entry_label.place(x=10, y=150)

        # Button Label to Open the File :
        self._entry_button = ctk.CTkButton(self._ctkwindow, text="Open File", 
                                           command=self._open_csv_file)
        self._entry_button.configure(fg_color='#A020F0', border_color='#000000',
                                     corner_radius=20, border_width=3, 
                                     hover_color='#301934', text_color='#FFFF00')
        self._entry_button.place(x=(self._window_width//2 - 65), y=200)

    
    def run(self) -> None:

        # Starts and Displays the customtkinter Window :

        self._ctkwindow.mainloop()

    
    def _plot_graph(self) -> None:

        # Model a graph correlating the dates with 
        # the company's respective revenues.

        Inputs_and_Outputs: list[tuple[Any, Any]] = [(dct.get('fundedDate'), dct.get('raisedAmt')) 
                                                     for dct in make_gen_from_csv(FILE_PATH) if\
                                                     dct.get('company') == self._options_menu.get()]
        # Arranges data in ascending order by date :
        Inputs_and_Outputs.sort(key=lambda x: dt.datetime.strptime(x[0], "%d-%b-%y").date())

        # Getting Dates :
        X_Axis: ndarray = np.array([dt.datetime.strptime(elem[0], "%d-%b-%y").date() for elem in Inputs_and_Outputs])
        Y_Axis: ndarray = np.array([float(elem[1]) for elem in Inputs_and_Outputs])

        plt.plot(X_Axis, Y_Axis)
        plt.show()

                

    def _open_csv_file(self) -> None:

        # Processes the data contained in a '.csv' file and compiles 
        # the information to provide options to the user.

        # Capture the Text in the Input Label :
        provided_path: str = self._entry_label.get().strip()

        self._empty_error_text: str = ""
        self._error_text_label = ctk.CTkLabel(self._ctkwindow, 
                                              text="")
        self._error_text_label.place(x=95, y=250)

        # If the Given Path is not Valid :
        if not (os.path.isfile(provided_path) and \
                os.path.splitext(provided_path)[1] == '.csv'):
            # Displaying Error Message :
            self._error_text_label.configure(text="Error!\nGiven Input is "\
                                     "not a Valid Path or \'.csv\' File Path.",
                                     text_color="#FF6242")
            
            return None
        
        # Clean the Error Message :
        self._error_text_label.configure(text=" " * 7 + "\n" + " " * 90)

        if self._toplevel_window is None or not self._toplevel_window.winfo_exists():
            
            # Creating the new Toplevel Window :
            self._toplevel_window = ctk.CTkToplevel(self._ctkwindow)
            self._toplevel_window.geometry(f"{self._window_width}x200")
            self._toplevel_window.resizable(False, False)
            self._toplevel_window.title("Settings...")

            # Graph Selection Label Text :
            self._selection_text_label = ctk.CTkLabel(self._toplevel_window, 
                                                      text="Select an Option :")
            self._selection_text_label.configure(text_color="#FFFF00")
            self._selection_text_label.place(x=(self._toplevel_window.winfo_width()//2 - 100),\
                                             y=20)
            

            # Option Selection Menu :

            # Creates a generator that provides the 
            # content of the lines in the '.csv' file :
            file_info: Generator[dict[str, Any], None, None] = make_gen_from_csv(FILE_PATH)

            # Capturing the name of each company present in the file and 
            # displaying them in the options section :
            company_names = [elem.get('company') for elem in file_info]
            filtered_company_names = filter(lambda x: 10 >= company_names.count(x) >= 2, 
                                            company_names)
            company_names = sorted(set(filtered_company_names))

            self._options_menu = ctk.CTkOptionMenu(self._toplevel_window,\
             values=company_names)
            self._options_menu.place(x=160, y=50)
            self._options_menu.configure(fg_color="#000000")


            # Confirm Button :
            self._confirm_button = ctk.CTkButton(self._toplevel_window, 
                                                 text='Confirm', 
                                                 command=self._plot_graph)
            self._confirm_button.configure(fg_color="#000000", 
                                           text_color="#FFFFFF",
                                           corner_radius=20,
                                           hover_color="#141414",
                                           font=self._fonts.get("Helvetica"))
            self._confirm_button.place(x=160, y=100)

            # Positioning Side Icons :
            # |-> Left Icon :
            Image_3 = Image.open(os.path.join(HERE_PATH, "Symbol_3.png"))
            self._image_3 = ctk.CTkImage(light_image=Image_3,
                                       dark_image=Image_3, size=(40, 90))
            self._image_3_Label = ctk.CTkLabel(self._toplevel_window, text='', 
                                                image=self._image_3)
            self._image_3_Label.place(x=90, y=20)

            # |-> Right Icon :
            Image_4 = Image.open(os.path.join(HERE_PATH, "Symbol_3(inverted).png"))
            self._image_4 = ctk.CTkImage(light_image=Image_4,
                                       dark_image=Image_4, size=(40, 90))
            self._image_4_Label = ctk.CTkLabel(self._toplevel_window, text='', 
                                                image=self._image_4)
            self._image_4_Label.place(x=325, y=20)


def _main(agrs: Any = None) -> None:
    print("\nFor testing purposes, use this file path: \n>>> \'\033[33m",\
          FILE_PATH, '\033[0m\'')
    print("(a new tab will open, look for it)")
    mygraph: GraphPlotCTK = GraphPlotCTK("Graph Plot +", 450, 300)
    mygraph.run()


if __name__ == '__main__':
    _main()
