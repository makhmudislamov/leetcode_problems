"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Questions to ask:
1. is array sorted?
2. can target exist in the array?
3. only positive nums?
"""


def twoSum(nums: [int], target: int):

    start = 0
    end = len(nums) - 1

    while start <= end:
        
        if nums[start] + nums[end] == target:
            return [nums[start], nums[end]]

        if nums[start] + nums[end] > target:
            end -= 1

        if nums[start] + nums[end] < target:
            start += 1
    



nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
