"""
Given [int] array, reorder the array so that even ints appear first, O(1) space

input: [3,5,4,6,1]
output: [4,6,3,5,1]

Questions to ask:
should it be sorted? - assume no
"""

# Approach 1 - O(n) time and space
# init empty array
# loop over the input
# if item is even append to output array
# loop again if item is zero or odd append

def reorder(arr):
    # base case
    if not arr:
        return arr

    if len(arr) == 1:
        return arr
    
    res = []

    for num in arr:
        if num != 0 and num % 2 == 0:
            res.append(num)

    if not res:
        return arr

    for num in arr:
        if num == 0 or num % 2 != 0:
            res.append(num)

    return res


arr = [3, 5, 5, 0, 7, 1]
print(reorder(arr))
