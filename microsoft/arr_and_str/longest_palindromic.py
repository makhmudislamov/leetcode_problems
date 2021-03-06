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

# helper func
# base cases
# two pointers start expanding from the target char of the input
# keep going: and check if the chars are the same (palindrome)
# if not return the len of last palindromic substring - right - left - 1

def expand_pointers(s, left, right):
    if s is None or left > right:
        return 0
    
    while (left >= 0 and right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1
    return right - left - 1


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # expanding from center approach
    # base cases if s==None or len() < 1 = " "

    # declare start and end as 0 - these are boundries of the substring that will be adjusted
    # loop over the input
    # call helper function - initialize case1 ex: "racecar" - middle is one char (len is od)
    # call helper function - initialize other ususal cases: "dabbak" - bb is in the middle
    # keep the max len of two of the above
    # if the max len is greater than (end-start)
    # set new boundries for start and end
    # start = curren index - ((max len - 1) / 2)
    # end = cur index + (max len /2)

    # return the substring of start and end indexes of input

    if s is None or len(s) < 1:
        return ""
        
    start = end = 0

    for i in range(len(s)):
        odd_len = expand_pointers(s, i, i) # example case: "racecar" 
        even_len = expand_pointers(s, i, i + 1)
        max_len = max(odd_len, even_len)
        print(max_len)
        # print("Odd and Even", odd_len, even_len)

        if max_len > end - start:
            start = i - ((max_len - 1) // 2)
            end = i + (max_len // 2)

            # print("start and end", start, end)

        
    return s[start:end + 1]


s = "babad"
print(longestPalindrome(s))
# print(expand_pointers(s, 2, 2))
