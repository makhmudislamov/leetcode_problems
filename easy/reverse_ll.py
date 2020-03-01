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
        # iterate over the ll until we reach NULL
        # from there start to change the pointer to previous node
        # no swapping here
        current_node = head
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next
        # pass