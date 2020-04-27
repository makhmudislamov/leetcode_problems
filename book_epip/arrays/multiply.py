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
    # num1 = ""
    # num2 = ""
    # res = []
    # for n in nums1:
    #     num1 += str(n)
    # for n in nums2:
    #     num2 += str(n)
    # m = int(num1) * int(num2)
    # i = 0
    # while i < len(str(m)):
    #     if str(m)[i] == "-":
    #         res.append(-int(str(m)[i+1]))
    #         i+=2
    #     res.append(int(str(m)[i]))
    #     i+=1
    # return res

    # book solution
    sign = -1 if (nums1[0] < 0) ^ (nums2[0] < 0) else 1
    nums1[0], nums2[0] = abs(nums1[0]), abs(nums2[0])

    # output arr
    result = [0] * (len(nums1) + len(nums2))
    print(result)
    for i in reversed(range(len(nums1))):
        for j in reversed(range(len(nums2))):
            result[i + j + 1] += nums1[i] * nums2[j]
            print(nums1[i], nums2[j], result)
            print(result[i + j + 1], result[i + j + 1] // 10)
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    
    result = result[next((i for i, x in enumerate(result) if x != 0),len(result)):] or [0]
    return [sign * result[0]] + result[1:]



nums1 = [1,2,3]
nums2 = [9,8,7]
# nums1 = [1,9,3,7,0,7,7,2,1]
# nums2 = [-7,6,1,8,3,8,2,5,7,2,8,7]

print(multiply(nums1, nums2))
