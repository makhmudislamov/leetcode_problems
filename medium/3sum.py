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
        

        zeros = 0
        # counting zeros
        for num in nums:
            if num == 0:
                zeros += 1
        # setting case boolean
        if zeros == 0:
            no_zero = True
        if zeros == 1:
            one_zero = True
        elif zeros >= 3:
            all_zero = True
        
        # kicking off sub algos
        if all_zero == True:
            res.add([0,0,0])
        
        if one_zero == True:
            # iterate over the array
            # binary search the opposite signed num,  num!=0 add this case
            # if found add to res as [-num, 0, num]

    def binary_search(self, nums, num, start=0, end=len(nums) - 1):

        # start = 0
        # end = len(nums) - 1

        mid = start + (start + end) // 2

        if nums[mid] == num:
            return nums[mid]

        

        

        

        


nums = [-1, 0, 1, 2, -1, -4]
s=Solution()
s.threeSum(nums)
