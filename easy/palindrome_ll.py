"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head is not None: # O(n)
            arr.append(head.val)
            head = head.next
        
        return self.isPalArr(arr)
        
    def isPalArr(self, array):
        start, end = 0, len(array) - 1
        
        while start <= end: # O(n)
            if array[start] != array[end]:
                return False
            start += 1
            end -= 1
        return True
