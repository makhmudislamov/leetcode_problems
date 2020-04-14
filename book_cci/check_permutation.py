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

# approach 2 = time and space - o(n) and O(n)
# create hashmap - char and frequency with first string
# go throught the second string
# decrement the char value from the hashmap if char exists
# if the req value is zero remove the key altogether

# if hashmap is empty - return true

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    freq = {}
    # building dict with str1
    for char in str1:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    for char in str2:
        if char not in freq:
            return False
        else:
            freq[char] -= 1
        
        if freq[char] == 0:
            freq.pop(char)

    
    return not freq
    

print(is_permutation("doG", "God"))
