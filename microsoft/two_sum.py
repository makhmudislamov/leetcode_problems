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
    # FOR SORTED ARRAY
    # start = 0
    # end = len(nums) - 1
    # while start <= end:
    #     print("start", nums[start])
    #     print("end", nums[end])
        
    #     if nums[start] + nums[end] == target:
    #         return [start, end]

    #     if nums[start] + nums[end] > target:
    #         end -= 1

    #     if nums[start] + nums[end] < target:
    #         start += 1

    # FOR UNSORTED ARRAY
    # index1 = 0
    # index2 = index1 + 1
    # while index1 < len(nums):
    #     while index2 < len(nums):
    #         if nums[index1] + nums[index2] == target:
    #             return [index1, index2]
    #         else:
    #             index2 += 1
    #     index1 += 1
    #     index2 = index1 + 1

    # DICTIONARY METHOD

    differences = {}
    for index, value in enumerate(nums):
        if not value in differences:
            differences[target-value] = index
        else:
            return [differences[value], index]




        
    
nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))
