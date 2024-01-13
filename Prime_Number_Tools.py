from typing import Generator


def check_primality(number: int, /) -> bool:
    
        if not isinstance(number, int) or number <= 0:
        raise ValueError('To check primality, the number must be an positive integer.')
    elif number == 1:
        return False
    elif number == 2:
        return True

    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
    return True


def prime_generator() -> Generator[int, None, None]:
    counter: int = 2

    while True:
        if check_primality(counter):
            yield counter
        counter += 1


def first_n_primes(quantity: int, /) -> list[int]:

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError('Quantity must be an positive integer.')

    primes: list[int] = []
    size: int = 0

    primes_generator: Generator[int, None, None] = prime_generator()

    while size < quantity:
        primes.append(next(primes_generator))
        size += 1

    return primes
