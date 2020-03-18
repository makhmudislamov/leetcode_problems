"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

def rotate(matrix: [[int]]):
    """
    Do not return anything, modify matrix in-place instead.
    """

    # keep len of matrix in a variable for looping
    # when looping the first time swam elemets diagonally, 4 and 2, 6 and 8 etc
    # then during the second loop
    # swap first and last element in each row

    mat_len = len(matrix)

    for row in range(mat_len):
        for col in range(row, mat_len):
            temporary = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temporary
        
        # this gives us: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    
    for row in range(mat_len):
        for col in range(mat_len // 2):
            temporary = matrix[row][col]
            print(matrix[row][mat_len - 1 - col])
            matrix[row][col] = matrix[row][mat_len - 1 - col]
            matrix[row][mat_len - 1 - col] = temporary

        # this gives us: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(matrix)


