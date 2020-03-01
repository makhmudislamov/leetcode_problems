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
        # ITERATIVE
        # declare a variable to point to previous Node
        # iterate over the LL until head reaches None(tail)
            # declare a variable that points to next Node
            # point head to previous Node
            # bring previous Node pointer to head
            # move the head pointer to next Node (to move the iteration)
        # return previous Node
        if not head:
            return None 
        previous_node = None
        while head != None:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node

        # RECURSIVE 
        # declare a helper function that takes two ars: previous (None) and current (head) Nodes
            # if current is None
            # return previous Node
            # declare a variable that points to next Node to current
            # point next to current Node to previous Node
            # bring previous Node to current Node
            # bring current node pointer to next Node

        # call the function recursively