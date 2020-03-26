"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        
        temp = ListNode(0)
        current = temp
#         started iteration
        while l1 is not None and l2 is not None:
#             linking current to l1 or l2
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
#         if l1 or l2 ends early

        if l1 is not None:
            current.next = l1
            l1 = l1.next
        if l2 is not None:
            current.next = l2
            l2 = l2.next
            
        return temp.next
