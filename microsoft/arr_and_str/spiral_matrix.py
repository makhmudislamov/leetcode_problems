"""
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

quetsions to ask:
1) duplicates?
2) sorted?

"""


def spiralOrder(matrix: [[int]]):
    # declare output arr
    # keep matrix height and width as variables
    # while iterating the matrix
    # change direction in turning points and make sure you dont visit already visited cells

    output_arr = []
    # height = len(matrix)
    # width = len(matrix[0])
    
    # for row in range(1):
    #     for col in range(width):
    #         cell_item = matrix[row][col]
    #         output_arr.append(cell_item)
    #         # if matrix[row][col] == matrix[0][len(matrix[0])-1]: # turning point
    #         #     break
    # last_item = len(matrix[0])-1
    # for row in range(1, height):
    #     output_arr.append(matrix[row][last_item])
    #     # print("here", matrix[row][last_item])
    
    # for cell in matrix[height-1]:
    #     print("rev", matrix[cell])

    # print(output_arr)

    row_start = 0
    row_end = len(matrix) - 1
    col_start = 0
    col_end = len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:

        for i in range(col_start, col_end + 1):
            # print("cur item", matrix[row_start][i])
            output_arr.append(matrix[row_start][i])
        
        row_start += 1

        for i in range(row_start, row_end + 1):
            # print("cur item", matrix[i][col_end])
            output_arr.append(matrix[i][col_end])

        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                # print("cur item", matrix[row_end][i])
                output_arr.append(matrix[row_end][i])
        
        row_end -= 1

    
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                # print("cur item", matrix[i][col_start])
                output_arr.append(matrix[i][col_start])
        
        col_start += 1
        

    return output_arr

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

matrix = [

    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
    
    ]

print(spiralOrder(matrix))
