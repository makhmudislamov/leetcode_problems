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

Questions to ask. space between the letters? 
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in s:
                return False
            return True

