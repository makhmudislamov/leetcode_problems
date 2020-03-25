"""
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for ll in lists:
            while ll is not None:
                res.append(ll.val)
                ll = ll.next
        res.sort()
        print(res)

        for i in range(len(res)):
            node_item = res[i]
            # print("node item is", str(node_item))
            new_ln = ListNode(node_item)
            print("node is ", str(new_ln))
            new_ln.next = res[i+1]
            print("node.next ", str(new_ln.next))

            if res[i+1] == res[len(res) - 1]:
                print("LAST NODE", new_ln)
                new_ln.next = None

