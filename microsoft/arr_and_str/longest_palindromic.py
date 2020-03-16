"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # palindromes = {}

    # set two pointers
    # one stays at the start and another one starts moving toward the end
    # after each move to right check if the current string is pal
    # if so append to dictionary: pal, len
    # at the end loop over the dictionary and return the string with the longest len
    # if there is only on item in dict. return the item

   