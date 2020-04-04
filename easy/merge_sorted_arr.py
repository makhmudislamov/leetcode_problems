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
    pass
    # SOLUTION 1 - O((n1 + n2)log(n+m)), Space O(1)
    # nums1 extends nums2 and sorting

    # SOLUTION 2 - O(m+n), Space (m) - using copy of nums1
    # loop over nums2 and add it to nums1 in proper order

    # SOLUTION 3 -  O(m+n), Space (1)
    # two pointers from the end to fill nums1 since the end is empty
    # 
    

nums1 = [1, 2, 3, 0, 0, 0] 
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))


