"""
Chaoter 1, Page 90
given two strings, check if one is a permutation of another
"""

# questions to ask:
# acceptable and optimal time and space
# case sensetivity, whitespace, upper, lower cases. Assume case sensetive to whitespace

# base case
#  if lenghts are differetn then return false

# approach 1. Time and space - logn logn for sorting two strings >> Time: logn and space 1
# sort the strings and check if they are the same


# def is_permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     str1.sort()
#     str1.sort()

#     return str1 == str2


