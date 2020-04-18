"""
Write a program that takes as input an array of digits encoding a nonegative decimal integer D
and updates the array to represent the integer D+1.

Input: [1,2,9]
Ouput: [1,3,0]
explanation: 129 + 1 = 130
"""
def plus_one(arr):
    
    arr[-1] += 1 # base cases and requirement
    for i in reversed(range(1,len(arr))):
        print(arr)
        if arr[i] != 10:
            print("simple case")
            break
        # elif arr[i] == 10 
        print("here", arr, arr[i-1])
        arr[i] = 0
        arr[i-1] += 1
        print("now", arr, arr[i-1])

    if arr[0] == 10:
        print("changinh this", arr[0])
        arr[0] = 1
        arr.append(0)
    return arr


arr = [1,4,5]
print(plus_one(arr))
