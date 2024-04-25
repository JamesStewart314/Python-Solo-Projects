# /---------------------------------------------------------------------------------------------------------------------\
#        This code is a custom module created in Python language - version 3.12 or higher - by me, it contains set
#                       of tools for determining, producing, locating and working with prime numbers.
#                                                Created in ~ 01/09/2024 ~
# \---------------------------------------------------------------------------------------------------------------------/

import itertools
import math

from typing import Callable, Generator


def check_primality(number: int, /) -> bool:

    """
    
     The function checks if the given number is prime.
    
    :param number: A positive integer number.
    :return: Returns a boolean ("True" if the number is prime, "False" if it's not)

    """
    
    if not isinstance(number, int) or number <= 0:
        raise ValueError("To check primality, the number must be a non-zero positive integer.")
    
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** (1 / 2)) + 1, 2):
        if not number % i:
            return False
        
    return True


def prime_generator() -> Generator[int, None, None]:

    """
    
     The function creates and returns a generator of sequential prime numbers.

    :return: Returns a generator object to form infinite sequential prime numbers.

    """
    
    return (number for number in itertools.count(start=2) if check_primality(number))


def first_n_primes(quantity: int, /) -> list[int]:

    """

      The function returns a list containing the first
     prime numbers in a quantity specified by the "quantity" parameter.

     :param quantity: A positive integer representing the desired quantity of prime numbers.
     :return: Returns a list with the specified quantity of prime numbers.

     """

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("The \"quantity\" parameter must be a positive integer.")

    primes: list[int] = []
    size: int = 0

    primes_generator: Generator[int, None, None] = prime_generator()

    while size < quantity:
        primes.append(next(primes_generator))
        size += 1

    return primes


def get_n_prime(order: int, /, *, quantity: int = 1) -> int | list[int]:

    """

     The function returns the nth prime number or a integer list of prime numbers,
    where the ordinal position of the first prime number is specified by the "order" parameter.

    :param order: Represents the nth desired prime number.
    :param quantity: Expresses the number of prime numbers desired from the position specified
     by the "order" parameter.

    :return: Returns the prime number corresponding to the position specified by the "order"
    parameter or a list containing the quantity of prime numbers requested by the "quantity" parameter.

    """

    if not (isinstance(order, int) and isinstance(quantity, int)):
        raise TypeError("The \"order\" and \"quantity\" parameters must be of integer type.")
    
    if order <= 0 or quantity <= 0:
        raise ValueError("It is not possible to provide a zero/negative ordinal position\
                          or quantity of prime numbers.")

    primes_generator: Generator[int, None, None] = prime_generator()

    if quantity == 1:
        
        desired_prime: int = next(primes_generator)
        order_counter: int = 1

        while order_counter < order:
            desired_prime = next(primes_generator)
            order_counter += 1
        
        return desired_prime

    else:

        desired_primes: list[int] = []
        order_counter: int = 0

        while order_counter < order - 1:
            next(primes_generator)
            order_counter += 1
        
        for _ in range(quantity):
            desired_primes.append(next(primes_generator))
        
        return desired_primes


def get_prime_ordinal_pos(prime_number: int, /) -> int | None:

    """
    
     Takes an integer and returns "None" if the value is not prime,
    or returns the ordinal position of the corresponding prime number.
    (e.g.: 2 ~> 1 ; 3 ~> 2 ; 4 ~> None ; 5 ~> 3 ... etc)

    :param prime_number: Prime integer whose ordinal position wants to be calculated.
    :return: An integer corresponding to the ordinal position of the prime or "None"
    if the given integer is not a prime number.
    
    """

    if not isinstance(prime_number, int):
        raise TypeError("The \"prime_number\" parameter must be a integer type.")
    
    if prime_number <= 0:
        raise ValueError("It is not possible to provide a zero/negative number.")
    
    primes_generator: Generator[int, None, None] = prime_generator()

    temp_prime: int = next(primes_generator)
    temp_ordinal_pos: int = 1

    while temp_prime < prime_number:
        temp_prime = next(primes_generator)
        temp_ordinal_pos += 1
    
    if temp_prime == prime_number:
        return temp_ordinal_pos
    else:
        return None


def _willans_prime_formula(order: int, /) -> int:

    """

     Returns the nth prime number, where the ordinal position of 
    the prime number is specified by the "order" parameter.

     This function was designed for self personal educational purposes only,
    I emphasize that its practical use in any program is totally discouraged, 
    in view of its discrepant inefficiency and inaccuracy in the results from
    the seventh prime number onwards, based on my personal tests.

     For clarification purposes, the function was created based on formulas
    provided by C. P. Willans in 1964. 
    
    Read for more information:

     • 'https://www.jstor.org/stable/3611701' ;
     • 'https://mathworld.wolfram.com/WillansFormula.html' ;
     • 'https://en.wikipedia.org/wiki/Formula_for_primes' ;
     • 'https://www.theoremoftheday.org/NumberTheory/Willans/TotDWillans.pdf'

    :param order: Represents the nth desired prime number.
    :return: Returns the prime number corresponding to the position specified by the "order" parameter.

    """

    # First, let's define Willans_Coef(x) - which returns 1 if "x = 1" or "x" is prime and 0 otherwise - as :
    Willans_Coef: Callable[[int], int] = lambda x: math.floor(pow(math.cos(math.pi * ((math.factorial(x - 1) + 1) / x)), 2))

    # Then, lets define the prime counting function as "Prime_Count(x)" :
    Prime_Count: Callable[[int], int] = lambda x: sum(Willans_Coef(j + 1) for j in range(0, x))

    # Therefore, we finally define the formula that returns prime numbers ordinally :
    Prime: Callable[[int], int] = lambda x: 1 + sum(math.floor(pow(x / Prime_Count(j + 1), 1 / x)) for j in range(0, pow(2, x)))

    return Prime(order)
