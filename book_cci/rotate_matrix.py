"""
Chpater 1, page 90

Given an image rep by NxN matrix, where each pixel is 4 bytes. rotate the image by 90 degrees. in place
"""

# Questions to ask:
# acceptable and optimal time and space reqs
# rotate clockwise or counter clockwise? - assumption: clockwise

# no memory approach will take O(n) time since we have to touch all n elements
# swapping diagonally (tansposing) and then using two pointers to swap elemets in each row
# this method works with NxN matrix

def rotate_matrix(matrix):
    matrix_len = len(matrix)

    # standard looping throughh 2D arr
    for row in range(matrix_len):
        for col in range(row, matrix_len): # go along with row so not range(0, len)
            # transposing - swapping diagonally
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # swapping elements from two ends
    for row in range(matrix_len):
        for col in range(matrix_len // 2): # looping until we reach the half of each col
            matrix[row][col], matrix[row][matrix_len - 1 -
                                          col] = matrix[row][matrix_len - 1 - col], matrix[row][col]
    
    print(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]
rotate_matrix(matrix)

