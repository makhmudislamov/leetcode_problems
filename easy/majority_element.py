"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

Question to ask - is there only one element that appears more than n/2?
"""


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        # find n/2 to compare
        # iterate over the array
        # if count of the item is greater than n/2
        # return the item
        # APPOACH1
        # half_of_len = len(nums) // 2        
        # for num in nums:
        #     if nums.count(num) > half_of_len:
        #         return num
        # APPROACH 2
        # empty dictionary
        # iterate over the nums
        # fill the dict key: num, value: appearances
        # iterate over the dict
        # return the key with max value

        pass
        