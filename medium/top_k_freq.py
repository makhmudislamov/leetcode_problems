"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        frequency = {}
#         building hashmap
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
#                 using heap nlargest
        return heapq.nlargest(k, frequency.keys(), key=frequency.get)
