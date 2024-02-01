# / ----------------------------------------------------------------------------------------- \ #
#   This code was created using the Python language in version 3.12 and higher - 11/30/2023
# \ ----------------------------------------------------------------------------------------- / #

import functools


def GDC(iterable: tuple[int, ...] | list[int], /) -> int | None:
    if len(iterable) >= 2:
        for element in iterable:
            if isinstance(element, int):
                if element <= 0:
                    if __name__ == "__main__":
                        print("Iterable must only contain non-zero positive integers.")
                    return None
            else:
                if __name__ == "__main__":
                    print("Iterable must only contain non-zero positive integers.")
                return None

        # Euclid's Algorithm :
        def GDC_2_numbers(number_1: int, number_2: int, /) -> int:

            aux_number_1 = max(number_1, number_2)
            aux_number_2 = min(number_1, number_2)

            remainder = aux_number_1 % aux_number_2

            while remainder:  # Remainder != 0
                aux_number_1 = aux_number_2
                aux_number_2 = remainder
                remainder = aux_number_1 % aux_number_2

            return aux_number_2

        return functools.reduce(GDC_2_numbers, iterable)

    else:
        if __name__ == "__main__":
            print("To calculate GDC, we need to have at least two numbers.")
        return None


def LCM(iterable: tuple[int, ...] | list[int], /) -> int | None:
    if len(iterable) >= 2:
        for element in iterable:
            if isinstance(element, int):
                if element <= 0:
                    if __name__ == "__main__":
                        print("Iterable must only contain non-zero positive integers.")
                    return None
            else:
                if __name__ == "__main__":
                    print("Iterable must only contain non-zero positive integers.")
                return None

        def LCM_2_numbers(number_1: int, number_2: int, /) -> int:

            return number_1 * number_2 // GDC((number_1, number_2))

        return functools.reduce(LCM_2_numbers, iterable)

    else:
        if __name__ == "__main__":
            print("To calculate LCM, we need to have at least two numbers.")
        return None
