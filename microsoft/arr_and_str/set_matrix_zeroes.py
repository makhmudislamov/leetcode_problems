"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
Output: 
[
    [1,0,1],
    [0,0,0],
    [1,0,1]
]

Example 2:
Input: 
[
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
Output: 
[
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Youtube solution: https://www.youtube.com/watch?v=6_KMkeh5kEc
"""

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # declaring height and width variables for iteration
    # initialize boolean (false)to mark if the first row should be filled with 0s
    height = len(matrix)
    width = len(matrix[0])
    first_row_zero = False

    # iterate over the first row 
    # if it has 0 change the boolean to true
    for cell in range(width):
        if matrix[0][cell] == 0:       
            first_row_zero = True
        

    # iterate over each cell
    # if the cell contains 0
    # mark the corresponding index of first row as zero >> denotes the whole column as 0
    for row in range(height):
        for col in range(width):        
            if matrix[row][col] == 0:
                matrix[0][col] = 0 # denotes: whole column as 0s
            


    # iterate each cell starting second row
    # declare boolean (false) if the cell is 0
    # once  a cell with 0 is reached change the boolean, break the loop
    for row in range(1, height):
        cell_has_zero = False
        for col in range(width):
            if matrix[row][col] == 0:
                cell_has_zero = True
                break

        # iterate over the columns
        # if the cell has 0 or (boolean above) or corresponding index of first row is 0
        # change this cell to 0
        for col in range(width):
            if cell_has_zero or matrix[0][col] == 0:
                matrix[row][col] = 0
            


    # if the first row has 0 (boolean above)
    #   iterate over the first row and change each cell to 0

    if first_row_zero:
        for cell in range(width):
            matrix[0][cell] = 0

    return matrix
  

matrix = [
    [0, 1, 2, 0], 
    [3, 4, 5, 2], 
    [1, 3, 1, 5]
    ]

print(setZeroes(matrix))
