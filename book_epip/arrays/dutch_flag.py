"""
Take an arr A and index in A, rearrange the elements so that elements less than A[i] appear first, followed by equal to A[i]
and then greater then the pivot
example:
A = [0,1,2,0,2,1,1]
i = 3 >> A[3] = 0
A = [0,0,1,2,2,1,1]

or if i = 2, A[2] = 2
A = [0,1,0,1,1,2,2] OR A = [0,0,1,1,1,2,2]
"""

# Approach 1 - O(n) space >> have 3 lists those sum of len is = len of input arr
# less, equal and greater
# iterate over input and append elements to 3 lists if they are less, equal and greater

def dutch_flag(arr, pivot_index):
    # base cases
    if not arr:
        return arr
    
    if pivot_index > len(arr) - 1:
        raise ValueError("Invalid Index")

    pivot = arr[pivot_index]
    less = []
    equal = []
    greater = []
    print(less, equal, greater)
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    
    arr = less + equal + greater

    return arr
arr = [0,1,2,0,2,1,1]
pivot_index = 3

print(dutch_flag(arr, pivot_index))
