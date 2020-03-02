"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

questions to ask. is it sorted
"""


class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        # APROACH 1 - has bugs
        # empty dict

        # iterate over the list
        # add item to dict
        # if the item is already in the dict
        # return false
        
        # base case
        if len(nums) == 1 or len(nums) == 0:
            return False
        # dupl = {}
        # for num in nums:
        #     if not dupl.get(num):
        #         dupl[num] = 1
        #     else:
        #         return False
        # print(dupl)
        # return True

        # APPROACH 2 - has bugs
        # start = 0
        # end = len(nums) - 1

        # while start < end or end > start:
        #     if nums[start] == nums[end]:
        #         return True
        #     return False

        # another approach - best solution
        # if nums.count(0) > 1:
        #     return True
        # return sum(set(nums)) != sum(nums)

        # even better solution
        return len(set(nums)) != len(nums)




nums = [1, 2, 3, 0, 0]
s = Solution()
print(s.containsDuplicate(nums))
