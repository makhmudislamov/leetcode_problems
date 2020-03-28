"""
A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where 
random pointer points to, or null if it does not point to any node.


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""


# Definition for a Node.
class ListNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        current = head
        while current is not None:
            #             adding nodes with the same values after each node
            temp = ListNode(current.val)
            temp.next = current.next
            current.next = temp
            current = current.next.next


#             copying random pointers
        current = head
        while current is not None:
            if current.random == None:
                current.next.random = None
            else:
                current.next.random = current.random.next
            current = current.next.next
#         # not checking current.next.next == None, because interweaving creates even
# #         number of nodes

        # while head is not None:
        #     if head.random == None:
        #         print(f"val:{head.val}, rand:{head.random}")
        #     else:
        #         print(f"val:{head.val}, rand:{head.random.val}")
        #     head = head.next

        # val:7, rand:None
        # val:7, rand:None
        # val:13, rand:7
        # val:13, rand:7
        # val:11, rand:1
        # val:11, rand:1
        # val:10, rand:11
        # val:10, rand:11
        # val:1, rand:7
        # val:1, rand:7

# #       separating clone nodes to build whole copied ll
        copied = head.next
        current = head
        while current.next is not None and current.next.next is not None:

            temp = current.next
            current.next = current.next.next
            current = current.next
            temp.next = current.next

        return copied
