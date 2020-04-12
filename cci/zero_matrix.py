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

    # after first iteartion if both arr are empty return the input

    row_len = len(matrix[0])
    col_len = len(matrix)
    # we'll need this if we have to mark the first row zero
    first_row_zero = False

    # check if the first row has zero and change the boolean
    for cell in matrix[0]:
        if cell == 0:
            first_row_zero = True

    # if the cell is zero denote the whole column as zero
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
    print("setting cols to zero up to this row", matrix)
    # iterate each cell starting second row
    # declare boolean (false) if the cell is 0
    # once  a cell with 0 is reached change the boolean, break the loop
    for row in range(1, row_len):
        cell_is_zero = False
        for col in range(col_len):
            if matrix[row][col] == 0:
                cell_is_zero = True
                break
    
    # iterate over the columns
    # if the cell has 0 or (boolean above) or corresponding index of first row is 0
    # change this cell to 0
        for col in range(col_len):
            if matrix[0][col] == 0 or cell_is_zero == True:
                matrix[row][col] = 0
    print("setting zeros", matrix)
    # if the first row has 0 (boolean above)
    #   iterate over the first row and change each cell to 0
    if first_row_zero:
        for cell in matrix[0]:
            matrix[0][cell] = 0

    print(matrix)

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
