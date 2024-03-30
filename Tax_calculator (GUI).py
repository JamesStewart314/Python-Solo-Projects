# /----------------------------------------------------------------------------------------------------------------------------------------------\
#  This code is a Tax Calculator with GUI, created in Python language - version 3.12 or higher - with dependencies on the "customtkinter" library.
#                                       To run it properly, make sure you have this package in your virtual environment.
#                                                                  Code Created in ~ 01/29/2024 ~
# \----------------------------------------------------------------------------------------------------------------------------------------------/

import customtkinter as ctk


class TaxCalculator:

    def __init__(self) -> None:

        self.window = ctk.CTk()
        self.window.title("Tax Calculator")  # Window name
        self.window.geometry('240x240')  # Window width and height
        self.window.resizable(False, False)  # User cannot resize the window

        # Initialize the Window :
        self.padding: dict[str, int] = {'padx': 10, 'pady': 10}

        # Income Label and Entry :
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax Label and Entry :
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        # Result Label and Entry :
        self.result_label = ctk.CTkLabel(self.window, text='Result:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.grid(row=2, column=1, **self.padding)
        self.result_entry.insert(0, f'{(ellps := '...'):^35}')

        # Calculate Button :
        self.calculate_button = ctk.CTkButton(self.window, text="Calculate", fg_color='black', command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    
    def update_result(self, text: str) -> None:
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, f"{text:^30}")

    
    def calculate_tax(self) -> None:
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())

            self.update_result(f"$ {income * tax_rate / 100:,.2f}")
        
        except ValueError as error:
            self.update_result("Invalid Entry")

    
    def run(self) -> None:
        self.window.mainloop()


if __name__ == '__main__':
    tc: TaxCalculator = TaxCalculator()
    tc.run()
