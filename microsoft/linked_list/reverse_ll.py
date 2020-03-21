"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
Good explanation iterative: https://www.youtube.com/watch?v=XDO6I8jxHtA&t=502s

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # ITERATIVE - accepted
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        return prev

        #         RECURSIVE - accepted
        # if head is None or head.next is None:
        #     return head

        # reversed_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return reversed_head
