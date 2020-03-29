"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}

        if len(s) == 0 or s is None:
            return -1
        
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = [1, i]
            else:
                chars.get(c)[0] += 1
        
        print(chars)
        for k in chars.keys():
            
            if chars.get(k)[0] == 1:
                return chars.get(k)[1]
        
        return -1
