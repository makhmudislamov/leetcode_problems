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
"""

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    for row_inx, row_list in enumerate(matrix):
        if 0 in row_list:
   
            # all_zero_row = matrix[row_inx]
            zero_found_row = matrix[row_inx]
            print("this" , zero_found_row)
            set_to_zero = row_list.index(0)
            for row_list in matrix:
                row_list[set_to_zero] = 0
    
            zero_found_row = [0] * len(zero_found_row)

    print("this again", zero_found_row)
    
    return matrix





matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(setZeroes(matrix))
# print(display_matrix(matrix))
