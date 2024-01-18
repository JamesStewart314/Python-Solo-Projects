from typing import Generator


def check_primality(number: int, /) -> bool:

    """
    The function checks if the given number is prime or not.
    
    :param number: An positive integer number.
    :return: Returns a boolean ("True" if the number is prime, "False" if it's not.)
    """
    
    if not isinstance(number, int) or number <= 0:
        raise ValueError('To check primality, the number must be an positive integer.')
    elif number == 1:
        return False
    elif number == 2:
        return True

    if number % 2 == 0:
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
    
    counter: int = 2

    while True:
        if check_primality(counter):
            yield counter
        counter += 1


def first_n_primes(quantity: int, /) -> list[int]:

    """
     The function returns a list containing the first prime numbers in a quantity specified by the "quantity" parameter.

     :param quantity: A positive integer representing the desired quantityof prime numbers.
     :return: Returns a list with the specified quantity of prime numbers.
     """

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError('Quantity must be an positive integer.')

    primes: list[int] = []
    size: int = 0

    primes_generator: Generator[int, None, None] = prime_generator()

    while size < quantity:
        primes.append(next(primes_generator))
        size += 1

    return primes
