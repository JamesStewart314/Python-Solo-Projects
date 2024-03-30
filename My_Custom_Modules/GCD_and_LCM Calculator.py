# /----------------------------------------------------------------------------------------------------------------------\
#         This code is a custom module created in Python language - version 3.11 or higher - by me, it contains set
#  of tools for calculate the least common multiple and greatest common divisor between an arbitrary quantity of numbers.
#                                              Created in ~ 12/25/2023 ~
# \----------------------------------------------------------------------------------------------------------------------/

import functools

from typing import Iterable


def _GCD_2_numbers(number_1: int, number_2: int, /) -> int:

    """
    
    Calculates the greatest common divisor between two numbers.
    (e.g: GCD(2, 3) => 1 ; GCD(7, 49) => 7 ; etc)

    :param number_1: A positive integer.
    :param number_2: A positive integer.
    
    :return: An integer corresponding to the greatest common divisor of
    the two given numbers.
    
    """

    # Euclid's Algorithm :
    aux_number_1 = max(number_1, number_2)
    aux_number_2 = min(number_1, number_2)

    remainder = aux_number_1 % aux_number_2

    while remainder:  # Remainder != 0
        aux_number_1 = aux_number_2
        aux_number_2 = remainder
        remainder = aux_number_1 % aux_number_2

    return aux_number_2


def _LCM_2_numbers(number_1: int, number_2: int, /) -> int:

    """
    
    Calculates the least common multiple between two numbers.
    (e.g: LCM(2, 3) => 6 ; LCM(7, 49) => 49 ; etc)

    :param number_1: A positive integer.
    :param number_2: A positive integer.
    
    :return: An integer corresponding to the least common multiple of
    the two given numbers.
    
    """

    # The product of the GCD and LCM of two natural numbers
    # is equal to the product of those numbers, so
    # LCM(n1, n2) = n1 * n2 / GCD(n1, n2) :
    
    return number_1 * number_2 // _GCD_2_numbers(number_1, number_2)


def GCD(number_iterator: tuple[int, ...] | list[int], /) -> int:

    """
    
    Calculates the greatest common divisor between two or more numbers present in an Iterable.
    (e.g: GCD((2, 3, 5)) => 1 ; GCD([7, 49, 21]) => 7 ; etc)

    :param number_iterator: An Iterable containing two or more positive integers.
    
    :return: An integer corresponding to the greatest common divisor of
    all numbers present in the Iterable.
    
    """
    
    assert isinstance(number_iterator, Iterable) and len(number_iterator) >= 2,\
            "To calculate the GCD, we need to have at least two "\
            "positive integers in an iterator."
        
    assert all((isinstance((exc := elem), (int, float)) and elem > 0) \
                for elem in number_iterator),\
                "Iterable must only contain non-zero positive integers. "\
                f"(exception caught: \'{exc}\')"

    return functools.reduce(_GCD_2_numbers, number_iterator)



def LCM(number_iterator: tuple[int, ...] | list[int], /) -> int:

    """
    
    Calculates the least common multiple between two or more numbers present in an Iterable.
    (e.g: LCM((2, 3, 5)) => 30 ; LCM([7, 49, 21]) => 147 ; etc)

    :param number_iterator: An Iterable containing two or more positive integers.
    
    :return: An integer corresponding to the least common multiple of
    all numbers present in the Iterable.
    
    """
    
    assert isinstance(number_iterator, Iterable) and len(number_iterator) >= 2,\
            "To calculate the LCM, we need to have at least two "\
            "positive integers in an iterator."
        
    assert all((isinstance((exc := elem), (int, float)) and elem > 0) \
                for elem in number_iterator),\
                "Iterable must only contain non-zero positive integers. "\
                f"(exception caught: \'{exc}\')"

    return functools.reduce(_LCM_2_numbers, number_iterator)


