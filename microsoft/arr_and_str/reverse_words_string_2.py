"""
Given an input string, reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

def reverse(arr, left, right):
    # left, right = 0, len(arr)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return arr

def reverse_each_word(arr):
    start = end = 0

    # looping over the array
    while start < len(arr):
        # looping over the array and each word
        while end < len(arr) and arr[end] != " ":
            end += 1
        reverse(arr, start, end - 1)
        # next word
        start = end + 1
        end += 1
    return arr

def reverseWords(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    print(reverse(s, 0, len(s)-1))
    print(reverse_each_word(s))


s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
print(reverseWords(s))
