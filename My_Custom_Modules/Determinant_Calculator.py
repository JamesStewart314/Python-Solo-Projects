# /---------------------------------------------------------------------------------------------------------------------\
#         This code is a custom module created in Python language - version 3.12 or higher - by me, it contains a set
#                                      of tools for calculate the determinant of a Matrix.
#                                                Created in ~ 01/19/2024 ~
# \---------------------------------------------------------------------------------------------------------------------/


type OptionalNumber = int | float | None
type MatrixType = list[list[int | float]]


def determinant(matrix: MatrixType, /) -> OptionalNumber:
    if matrix:  # if the Matrix is not empty
        if len(matrix) > 1:

            order: int = len(matrix[0])
            for row in matrix:
                if len(row) != order:
                    if __name__ == '__main__':
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
                    
                    # Getting the Horizontal Line with More Zeros :
                    line: list[int] = max(matrix, key=lambda x: x.count(0))
                    indexes: list[tuple[int, int]] = [(matrix.index(line), i) for i in range(len(line))]

                    # Auxiliary Variables to Check Vertical Lines on the Matrix to apply Laplace's Theorem :
                    aux_vertical_line: list[int] = []
                    temp_indexes: list[tuple[int, int]] = []

                    order: int = len(matrix)

                    for idx_1 in range(order):
                        for idx_2 in range(order):
                            # Traversing the Vertical Lines of the Matrix :
                            aux_vertical_line.append(matrix[idx_2][idx_1])
                            temp_indexes.append((idx_2, idx_1))

                        result: list[int] = max(aux_vertical_line.copy(), line, key=lambda x: x.count(0))

                        if result != line:
                            indexes = temp_indexes.copy()
                            line = result
                        aux_vertical_line.clear()
                        temp_indexes.clear()

                    final_results: list[int] = []  # Variable to Store the Result of Minor Determinants.

                    for index in indexes:
                        new_temp_matrix: MatrixType = []

                        for idx_1 in range(order):
                            temp_line: list[int] = []

                            for idx_2 in range(order):

                                if idx_1 != index[0] and idx_2 != index[1]:
                                    temp_line.append(matrix[idx_1][idx_2])

                            if temp_line:  # If the temp_line is not empty.
                                new_temp_matrix.append(temp_line)

                        if matrix[index[0]][index[1]]:
                            final_results.append(
                                (-1) ** (sum(index)) * matrix[index[0]][index[1]] * determinant(new_temp_matrix))

                    return sum(final_results)

            else:
                if __name__ == '__main__':
                    print("Cannot evaluate a determinant of a matrix", len(matrix), "x", len(matrix[0]))

        else:

            if len(matrix[0]) == 1:
                return matrix[0][0]
            else:
                order = len(matrix[0])

                for row in matrix:

                    if len(row) != order:
                        if __name__ == '__main__':
                            print("This is not an Matrix.")
                        return None

                if __name__ == '__main__':
                    print("Cannot evaluate a determinant of a matrix", len(matrix), "x", len(matrix[0]))
