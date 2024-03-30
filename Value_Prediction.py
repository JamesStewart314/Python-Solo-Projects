# /---------------------------------------------------------------------------------------------------\
#        This is a Value Prediction code created in Python language - version 3.12 or higher
#  library dependencies: "scikit-learn" ; "pandas" ; "numpy" ; "pyarrow" ; "matplotlib" ; "colorama"
#         To run it properly, make sure you have these packages in your virtual environment.
#                                    Code Created in ~ 02/22/2024 ~
# \---------------------------------------------------------------------------------------------------/


import dataclasses

import colorama as cr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from typing import Final, Any
from numpy import ndarray
from pandas import DataFrame


type Numeric = int | float
type DataValues = tuple[Numeric, ...] | list[Numeric]

reset_cr: str = cr.Style.RESET_ALL
yellow_cr: str = cr.Fore.LIGHTYELLOW_EX
red_cr: str = cr.Fore.LIGHTRED_EX


@dataclasses.dataclass
class Prediction:
    value: float
    r2_score: float
    slope: float
    intercept: float
    mean_absolute_error: float

    def __str__(self) -> str:
        return f"{self.value:,.2f}"


def display_plot(input_values: DataValues, output_values: DataValues, Y_line) -> None:

    # Displays a Plot of the Data Provided using Matplotlib.
    
    size: Final[int] = 12

    plt.scatter(input_values, output_values, s=size)
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')
    plt.plot(input_values, Y_line, color='y')
    plt.show()


def make_linear_prediction(input_data: DataValues, output_data: DataValues, 
                           input_value: Numeric, show_plot: bool = False) -> Prediction:
    
    """
    
     Makes a prediction of a value based on a linear regression model 
    built from the data provided in the "input_data" and "output_data" parameters.

    :param input_data: A list or tuple of numeric values that will be 
     the sample inputs of the linear regression model.
    :type input_data: DataValues. ('list[int | float]' or 'tuple[int | float, ...]')

    :param output_data: A list or tuple of numeric values that correspond 
     to the outputs of each input contained in the input values.
    :type output_data: DataValues. ('list[int | float]' or 'tuple[int | float, ...]')

    :param input_value: The value you want to make the prediction.
    :type input_value: Numeric. ('int' or 'float')

    :param show_plot: A Flag indicating if a graph should be displayed 
    based on the data provided. (default is 'False')
    :type show_plot: bool.

    :returns: An instance of the 'Prediction' class containing the prediction results.
    :rtype: Predciction.
    
    """
    

    # /---------------------- Preventative Check ----------------------\
    #
    # I performed these checks just to exercise my knowledge in Python 
    # when validating the types of parameters provided in function calls.
    #

    # Asserts whether "input_data" and "output_data" parametes 
    # are of type tuple/list:
    assert isinstance(input_data, (tuple, list)) and\
          isinstance(output_data, (tuple, list)),\
          f"{yellow_cr}\"input_data\" and \"output_data\" Parameters Must be "\
          f"of type \'DataValues\'. "\
          f"(\'tuple[int | float, ...]\' or \'list[int | float]\'){reset_cr}"
    
    # Asserts Whether the "input_value" Parameter is of Type int/float:
    assert isinstance(input_value, (int, float)),\
        f"{yellow_cr}\"input_value\" Parameter Must be of Type \'Numeric\'. "\
        f"(\'int\' or \'float\'){reset_cr}"
    
    # Asserts if the "show_plot" Parameter is of Boolean Type:
    assert isinstance(show_plot, bool), \
    f"{yellow_cr}\"display_plot\" Parameter Must be of Type Boolean.{reset_cr}"

    # Asserts Whether the Amount of input and output data are Equivalent:
    assert (input_size := len(input_data)) == (output_size := len(output_data)),\
    f"{red_cr}Mismatch in Quantity of Input and Output Values! "\
    f"(Inputs Quant.: {input_size}) != Outputs Quant.: {output_size}){reset_cr}"

    # Asserts whether there is input and output data:
    assert input_size > 0 and output_size > 0,\
    f"{yellow_cr}Quantity of Inputs and "\
    f"Output Values must be Greater than Zero! "\
    f"(Inputs Quant.: {input_size} // Outputs Quant.: {output_size}){reset_cr}"

    # Check that all elements contained in the 
    # "input_data" parameter correspond to the correct type:
    assert all(isinstance((exc := elem), (int, float)) for elem in input_data),\
    f"{yellow_cr}All Elements in \"input_data\" parameter must be "\
    f"of type \'Numeric\'. (\'int\' or \'float\') "\
    f"{red_cr}\n• Exception Caught: \'{exc}\'{reset_cr}"

    # Check that all elements contained in the 
    # "output_data" parameter correspond to the correct type:
    assert all(isinstance((exc := elem), (int, float)) for elem in output_data),\
    f"{yellow_cr}All Elements in \"output_data\" parameter must be "\
    f"of type \'Numeric\'. (\'int\' or \'float\') "\
    f"{red_cr}\n• Exception Caught: \'{exc}\'{reset_cr}"

    # \----------------------------------------------------------------/

    # Create a dataframe for our input data :
    data_frame: DataFrame = pd.DataFrame({'inputs': input_data,
                                           'outputs': output_data})
    
    # Reshaping the data using Numpy (x: Inputs, y: Outputs) :
    ArrX: ndarray = np.array(data_frame.get('inputs')).reshape(-1, 1)
    ArrY: ndarray = np.array(data_frame.get('outputs')).reshape(-1, 1)

    # Split the Data into Training Data to Test our Model :
    train_X, test_X, train_Y, test_Y = train_test_split(ArrX, ArrY,
                                                        random_state=0,
                                                        test_size=.20)
    
    # Initialize the Model and Test It :
    model: LinearRegression = LinearRegression()
    model.fit(train_X, train_Y)

    # Prediction :
    Y_prediction: ndarray = model.predict([[input_value]])
    Y_line: ndarray = model.predict(ArrX)

    # Testing for Accuracy :
    Y_test_prediction: ndarray = model.predict(test_X)


    # Plot Graph :
    if show_plot:
        display_plot(input_values=ArrX, output_values=ArrY, Y_line=Y_line)
    
    return Prediction(value=Y_prediction[0][0],
                      r2_score=r2_score(test_Y, Y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_Y, Y_test_prediction))


def _main(args: Any = None) -> None:

    years: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    earnings: list[int] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3000, 5000, 4800]
    
    my_input: int = 20

    extra_values: tuple[int, ...] = (40, 45, 50, 70, 90)

    print(f"{yellow_cr}• Processing...{reset_cr}", end='')

    temp_prediction: Prediction = make_linear_prediction(years, earnings,
                                                         my_input, show_plot=True)
    print('\r' + ' ' * 20, end='\r')
    print(f"{cr.Fore.GREEN}Done!{reset_cr} See the Results Below :"\
          f"\n└> The Value Prediction is:", temp_prediction)
    
    print(" │")
    print(f" │ • Predictions Accuracy: ({temp_prediction.r2_score * 100:.2f}%)")
    print(f" │ • Mean Absolute Error: ~ {temp_prediction.mean_absolute_error:,.2f}")
    print(" │")
    print(f" └─> {yellow_cr}Another Extra Predictions{reset_cr} :\n   │", end='')

    for value in extra_values:
        print((last_line := f"\n   ├ Prediction at the Value \'{value:,}\':  "\
                            f"{temp_prediction.slope * value:,.2f}"), end='')
    
    print('\b' * (len(last_line) - 4) + '└')


if __name__ == '__main__':
    _main()
