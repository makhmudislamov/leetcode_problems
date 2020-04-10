"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        # init output set
        # set cases as False
        # sorting the arr
        # find the zeros and change the case boolean to True
        # cover each case and add al combos to output set
        # turn set into int int
        # return int int
        res = set()
        all_zero = False
        one_zero = False
        no_zero = False 

        sorted_nums = sorted(nums)
        print(sorted_nums)
        

nums = [-1, 0, 1, 2, -1, -4]
s=Solution()
s.threeSum(nums)
