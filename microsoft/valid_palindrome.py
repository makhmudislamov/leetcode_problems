"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import string

def isPalindrome(s: str):
    s = s.lower()
    s = s.translate(s.maketrans('', '', string.punctuation))
    s=s.replace(" ", "")
    
    if s == s[::-1]:
        return True
    return False


# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))
