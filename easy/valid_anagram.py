"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Questions to ask >> space between the letters? is empty string valid?
"""
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basic solution
        # for char in s:
        #     if not char.isalpha() and char not in s:
        #         return False
        #     return True

        # better solution
        # base cases
        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True

        # dict method
        # documentation: https://docs.python.org/3/library/collections.html
        # return collections.Counter(s) == collections.Counter(t)

