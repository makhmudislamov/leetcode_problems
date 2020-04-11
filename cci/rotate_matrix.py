"""
Chpater 1, page 90

Given an image rep by NxN matrix, where each pixel is 4 bytes. rotate the image by 90 degrees. in place
"""

# Questions to ask:
# acceptable and optimal time and space reqs
# rotate clockwise or counter clockwise? - assumption: clockwise

# no memory approach will take O(n**2) time since we have to touch all n**2 elements
# swapping diagoanlly and then using two pointers to swap elemets in each row


