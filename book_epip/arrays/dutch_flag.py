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

# Approach 2 - O(n**2) time and O(1) space
# 2 stage iteration
# 1st stage  - in each iteration increase the startin point (first 0 then 1 etc)
# in each itration we seek an element smaller than the pivot
# when found we move the smaller element to start of A via exchange

# 2nd stage iteration - we start from the end and move elements greater than 
# pivot to the end of the array
def dutch_flag(arr, pivot_index):
    # base cases
    if not arr:
        return arr

    if pivot_index > len(arr) - 1:
        raise ValueError("Invalid Index")
    
    pivot = arr[pivot_index]
    print("input", arr)
    # 1st iteration
    for i in range(len(arr)):
        for j in range(i+1, len(arr)): # increasing starting index by 1 each time
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                print(f"i {i}, j {j}. swapped {arr[i]} and {arr[j]} >> {arr}")
                break
    print("*****SECOND PASS*****")
    for i in reversed(range(len(arr))):
        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                print(f"i {i}, j {j}. swapped {arr[i]} and {arr[j]} >> {arr}")
                break

    return arr
arr = [0,1,2,-3,5,2,1,7,5,9,10,1]
pivot_index = 4

print(dutch_flag(arr, pivot_index))

# Approach 1 - O(n) space >> have 3 lists those sum of len is = len of input arr
# less, equal and greater
# iterate over input and append elements to 3 lists if they are less, equal and greater

# def dutch_flag(arr, pivot_index):
#     # base cases
#     if not arr:
#         return arr
    
#     if pivot_index > len(arr) - 1:
#         raise ValueError("Invalid Index")

#     pivot = arr[pivot_index]
#     less = []
#     equal = []
#     greater = []
#     print(less, equal, greater)
#     for num in arr:
#         if num < pivot:
#             less.append(num)
#         elif num == pivot:
#             equal.append(num)
#         else:
#             greater.append(num)
    
#     arr = less + equal + greater

#     return arr
