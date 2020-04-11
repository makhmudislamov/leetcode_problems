"""
Given two strings check if they are one (or zero) edit away. Edits: insert, delete, replace a char
Example:
pale, ple -> True
pale, bake -> False
"""

# questions to ask:
# acceptable and optimal time and space reqs
# space, punctations - ASCII chars?
# lower case/upper case

# base case
# if two strings are equal -> True
# if difference of two string len are more than 1, use abs- > False

# approach 1 - O(n) space and time
# build frequency hashtable with one string
# loop over the second one and check
#  if at the end len of the dict is one or less and the item freq is one -> True

def one_away(s1, s2):
    # base cases
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    freq = {}
    # building a dict
    for char in s1:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    for char in s2:
        if char in freq:
            freq[char] -= 1
        else:
            freq[char] = 1
        
        if freq[char] == 0:
            freq.pop(char)

    return not freq or len(freq) == 1




        
s1 = "pale"
s2 = "ale"

print(one_away(s1, s2))
