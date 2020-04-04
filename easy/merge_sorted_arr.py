"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""



def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:

    # SOLUTION 3 -  O(m+n), Space (1)
    # two pointers from the end to fill nums1 since the end is empty
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
            # p -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p1 -= 1
        p -= 1


        
    

nums1 = [1, 2, 3, 0, 0, 0] 
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))


