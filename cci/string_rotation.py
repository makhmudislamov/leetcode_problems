"""
Chapter 1, page 91

assume you have is_substring() method that checks if one string is a subs of another
using only one cal of is_substring() method check if s1 is a rotation of s2

example
waterbottle >> erbottlewat
"""

# questions to ask
# acceptable and optimal time and space reqs
# lowercase, uppercase? white space ASCII? - assuming lowercase and no whitespace


# s2 is always a substring of s1s1 so will use this fact
def is_substring(s1, s2):
    pass

def is_rotation(s1, s2):
    # base case
    if len(s1) > 0 and len(s1) == len(s2):
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    else:
        return False