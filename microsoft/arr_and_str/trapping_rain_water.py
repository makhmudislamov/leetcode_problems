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

def calculate_depth(height, target_index):
    left = right = target_index
    if height is None or len(height) < 1: 
        return 0
    walls = set()
    while (left >= 0 and right < len(height)) and (height[left - 1] > height[left] and height[right] < height[right + 1]):
        walls.add(height[target_index])
        left -= 1
        right += 1
        walls.add(height[left])
        walls.add(height[right])
    print(walls)

    return max(walls) - min(walls)


def trap(height: [int]):
    # init value that represents output (int=0)
    # loop over the input
    # call helper func for each value
    # incerement the output value
    pass


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
print(calculate_depth(height, 5))
