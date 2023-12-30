import functools


def GDC(iterable: tuple[int, ...] | list[int]) -> None | int:
    if len(iterable) >= 2:
        for element in iterable:
            if isinstance(element, int):
                if not element:  # If number is != 0
                    print("Iterable must  only contain non-zero positive integers.")
                    return None
            else:
                print("Iterable must  only contain non-zero positive integers.")
                return None

            # Euclid Algorithm :
            def GDC_2_numbers(number_1: int, number_2: int) -> int:

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
        print("To calculate GDC, we need to have at least two numbers.")
        return None


def LCM(iterable: tuple[int, ...] | list[int]) -> None | int:
    if len(iterable) >= 2:
        for element in iterable:
            if isinstance(element, int):
                if not element:  # If number is != 0
                    print("Iterable must  only contain non-zero positive integers.")
                    return None
            else:
                print("Iterable must  only contain non-zero positive integers.")
                return None

            # Euclid Algorithm :
            def LCM_2_numbers(number_1: int, number_2: int) -> int:

                return number_1 * number_2 // GDC((number_1, number_2))

            return functools.reduce(LCM_2_numbers, iterable)

    else:
        print("To calculate GDC, we need to have at least two numbers.")
        return None


