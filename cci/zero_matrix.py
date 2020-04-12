"""
Chapter 1, page 90

Given NxM matrix, if an element in the matrix is 0, set entire column and row to 0
"""

# questions to ask:
# acceptable and optimal time and space req

# approach with O(n) space and O(n**2) time
# when iterating no need to flag the exact location but the row and col as 
# we'll set the whole row and col to zero


def zero_matrix(matrix):
    # base case
    if not matrix:
        return matrix

    zero_row = []
    zero_col = []
    # after first iteartion if both arr are empty return the input

    row_len = len(matrix[0])
    col_len = len(matrix)
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 0:
                zero_row.append(row)
                zero_col.append(col)

    # if there are no zeros return the input
    if len(zero_col) == len(zero_row) == 0:
        return matrix
    # filling the zeros
    for row in range(row_len):
        if row in zero_row:
            matrix[row] = [0] * len(matrix[row])
        for col in range(col_len):
            if col in zero_col:
                matrix[row][col] = 0
    
    return matrix


matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]
# matrix = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]

print(zero_matrix(matrix))
