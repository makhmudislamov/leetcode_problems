"""
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity - O(n). 
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        # Time: O(n2); Space O(1) solution
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num

        # Time: O(n); Space O(n) - for using set
        # 2∗(a+b+c)−(a+a+b+b+c)=c

        # return 2 * sum(set(nums)) - sum(nums)

        # Time: O(n); Space O(1) - bit manipulation - meets the reqs
        a = 0
        for i in nums:
            a ^= i
        return a

            

nums = [4, 1, 2, 1, 2]
sol = Solution()
print(sol.singleNumber(nums))
