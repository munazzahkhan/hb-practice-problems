"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    # find the 0s
    coords = locate_zeros(matrix)

    # loop over coords of 0s
    for row_x, col_y in coords:
        zero_out_row(matrix, row_x)
        zero_out_col(matrix, col_y)

    return matrix


def zero_out_row(matrix, row_x):
    for y in range(len(matrix[0])):
        matrix[row_x][y] = 0


def zero_out_col(matrix, col_y):
    for row in matrix:
        row[col_y] = 0


def locate_zeros(matrix):
    coords = []

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                coords.append((i,j))

    return coords


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
