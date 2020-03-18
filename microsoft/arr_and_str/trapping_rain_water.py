"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

# helper func
# at the target index
# expand to two sides until on of the side values is less then previous value - should increase
# in that condition >> max value of one side - min value of another side
# return the value >> cubes of water in each section


def trap(height: [int]):
    if height is None or len(height) == 0:
        return 0

    total = 0
    level = 0
    left = 0
    right = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            lower = height[left]
            left += 1
        else:
            lower = height[right]
            right -= 1
        level = max(lower, level)
        total += level - lower
        print("lower", lower)
        print("total", total)
    return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
