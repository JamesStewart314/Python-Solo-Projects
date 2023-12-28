import time

from typing import List


def determinant(matrix: List[List[int | float]]) -> int | float | None:

    if matrix:  # if the Matrix is not empty
        if len(matrix) > 1:

            order = len(matrix[0])
            for row in matrix:
                if len(row) != order:
                    print("This is not an Matrix.")
                    return None

            if len(matrix) == len(matrix[0]):
                if len(matrix) == 2:
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                elif len(matrix) == 3:
                    principal_diagonal_1 = matrix[0][0] * matrix[1][1] * matrix[2][2]
                    principal_diagonal_2 = matrix[1][0] * matrix[2][1] * matrix[0][2]
                    principal_diagonal_3 = matrix[0][1] * matrix[1][2] * matrix[2][0]

                    secondary_diagonal_1 = matrix[0][2] * matrix[1][1] * matrix[2][0]
                    secondary_diagonal_2 = matrix[0][1] * matrix[1][0] * matrix[2][2]
                    secondary_diagonal_3 = matrix[1][2] * matrix[2][1] * matrix[0][0]

                    first_sum = principal_diagonal_1 + principal_diagonal_2 + principal_diagonal_3
                    second_sum = secondary_diagonal_1 + secondary_diagonal_2 + secondary_diagonal_3

                    return first_sum - second_sum
                else:
                    # Laplace's Theorem :

                    line = max(matrix, key=lambda x: x.count(0))

                    aux_vertical_line = []
                    indexes = None
                    temp_indexes = []

                    order = len(matrix)

                    for idx_1 in range(order):
                        for idx_2 in range(order):
                            aux_vertical_line.append(matrix[idx_2][idx_1])
                            temp_indexes.append((idx_2, idx_1))
                        result = max(aux_vertical_line.copy(), line, key=lambda x: x.count(0))
                        if result != line:
                            indexes = temp_indexes.copy()
                            line = result
                        aux_vertical_line.clear()
                        temp_indexes.clear()

                    if indexes:
                        final_results = []

                        for index in indexes:
                            new_temp_matrix = []
                            for idx_1 in range(order):
                                temp_line = []
                                for idx_2 in range(order):
                                    if idx_1 != index[0] and idx_2 != index[1]:
                                        temp_line.append(matrix[idx_1][idx_2])
                                if temp_line:
                                    new_temp_matrix.append(temp_line)

                            if matrix[index[0]][index[1]]:
                                final_results.append((-1) ** (sum(index)) * matrix[index[0]][index[1]] * determinant(new_temp_matrix))
                        return sum(final_results)
            else:
                print("Cannot evaluate a determinant of a matrix", len(matrix), "x", len(matrix[0]))
        else:
            if len(matrix[0]) == 1:
                return matrix[0]
            else:
                order = len(matrix[0])

                for row in matrix:
                    print(row, order)
                    if len(row) != order:
                        print("This is not an Matrix.")
                        return None

                print("Cannot evaluate a determinant of a matrix", len(matrix), "x", len(matrix[0]))
                return None

start = time.time()

a = determinant([
    [33, -44, 12, -25, 8, 20, 37, -15, -30, 40, 10, 5],
    [-18, 22, 48, -5, 10, -40, 15, -7, 32, -28, 18, -45],
    [-3, 27, 13, -50, 4, 14, -23, 30, 42, -35, 6, 17],
    [-22, -10, 8, -48, -13, 19, -37, 45, 26, 9, -14, 36],
    [44, -2, -46, 25, 3, -11, 50, -20, 7, -33, 16, -27],
    [16, -18, 38, 11, -32, -4, 7, -19, 50, -14, 23, -10],
    [35, 9, 47, -38, 5, -30, -8, 15, 21, -44, 12, -46],
    [-33, 26, -49, -1, 3, 0, -24, 50, 4, -21, 8, -17],
    [46, 38, -33, 12, -15, 19, -10, -40, 27, 28, 15, -42],
    [9, 36, -23, -48, -14, 5, 30, -7, -38, 16, -1, -44],
    [18, 41, -48, 4, 19, -45, -11, 37, 14, -40, 6, 23],
    [-28, 32, 17, -5, 10, -36, 30, -2, -7, 48, -13, -25]
])

end = time.time()

if a:
    print("Determinant :", a, "\nTime Spent :", end - start)
