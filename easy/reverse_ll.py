"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # declare a variable to point to previous Node
        # iterate over the LL until head reaches None(tail)
            # declare a variable that points to next Node
            # point head to previous Node
            # bring previous Node pointer to head
            # move the head pointer to next Node (to move the iteration)
        pass