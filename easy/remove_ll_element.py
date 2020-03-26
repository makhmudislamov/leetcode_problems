"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        # init empty node and link it no head
        temp = ListNode(0)
        temp.next = head

        # init two neighbot pointers for iteration 
        prev = temp
        current = head
        while current is not None:
            # value found
            if val == current.val:
                prev.next = current.next # skip the node and link the previous node to next node
            else:
                prev = current # move prev
            current = current.next # move current
        return temp.next 
