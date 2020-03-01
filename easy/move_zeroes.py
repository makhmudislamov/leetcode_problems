"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # end = len(nums) - 1
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
                # print(i)
        # return nums

        # another approach
        # int low = 0;
        # int high = 0;
        # while(high < nums.length){
        #     if(nums[high] == 0){
        #         high++;}else if(low == high){
        #         low++;
        #         high++; }else if(nums[high] > 0 | | nums[high]  < 0){
        #         nums[low++] = nums[high];
        #         nums[high++] = 0;


            


nums=[0, 1, 0, 3, 12]

s = Solution()
print(s.moveZeroes(nums))
