"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        dif = {}

        for index, num in enumerate(nums):
            if not num in dif:
                dif[target-num] = index             
            else:
                return [dif[num], index]


nums = [2, 7, 11, 15]
target = 9
s = Solution()
s.twoSum(nums, target)
