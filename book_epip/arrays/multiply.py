"""
input: [1,2,3] and [5,5]
output: [6,7,6,5] >> 123 x 55
"""

def multiply(nums1, nums2):
    # O(n) time and O(m) space
    # declare two empty string
    # iterate over both arrays and create fill each string with 
    # array elements
    # turn the strings into int
    # multiply them
    # iterate over the result
    # and add each element to output arr as int
    num1 = ""
    num2 = ""

    res = []

    for n in nums1:
        num1 += str(n)
    print(num1)
    for n in nums2:
        num2 += str(n)
    print(num2)
    m = int(num1) * int(num2)
    print(m)
    i = 0
    while i < len(str(m)):
        if str(m)[i] == "-":
            res.append(-int(str(m)[i+1]))
            i+=2
        res.append(int(str(m)[i]))
        i+=1

    return res


nums1 = [1,9,3,7,0,7,7,2,1]
nums2 = [-7,6,1,8,3,8,2,5,7,2,8,7]

print(multiply(nums1, nums2))
