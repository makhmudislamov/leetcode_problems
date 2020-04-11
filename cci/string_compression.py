"""
Chapter1, page 90
implement basic string compression method using counts of repeated chars.
example
input: aabcccccaaa
output: a2bc5a3
if non compressable, return the input
input has only uppercase and lowercase letters (a-z)
"""

# questions to ask:
# acceptable and optimal time and space reqs


# base cases
#  if input is empty return empty string

# approach 1 - O(n) time and space
# init empty dict
# init empty string
# build dict with char and frequency
# loop over the dict
# add key,value as string to output
