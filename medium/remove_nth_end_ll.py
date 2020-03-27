"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:
Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
# TWO POINTER METHOD
        p1 = head
        p2 = head
        for _ in range(n+1):

            if p1 is None:
                p2 = p2.next
                return p2

            p1 = p1.next

        while p1 != None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return head
