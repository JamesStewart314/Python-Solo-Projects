# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 01/09/2024
# \ ----------------------------------------------------------------------------------------- / #

import itertools

from typing import Generator


def check_primality(number: int, /) -> bool:

    """
    
     The function checks if the given number is prime or not.
    
    :param number: An positive integer number.
    :return: Returns a boolean ("True" if the number is prime, "False" if it's not.)

    """
    
    if not isinstance(number, int) or number <= 0:
        raise ValueError("To check primality, the number must be an positive integer.")
    
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
        
    return True


def prime_generator() -> Generator[int, None, None]:

    """
    
     The function creates a generator of sequential prime numbers.

    :return: Returns a generator object to form prime numbers.

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
        
        order_counter: int = 0
        desired_prime: int = 0

        while order_counter < order:
            desired_prime = next(primes_generator)
            order_counter += 1
        
        return desired_prime

    else:

        order_counter: int = 0
        desired_primes: list[int] = []

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
    :return: an integer corresponding to the ordinal position of the prime or "None"
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
