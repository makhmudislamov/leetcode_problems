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
        if len(lists) < 1:
            return None
        res = []
        for ll in lists:
            try:
                while ll is not None:
                    res.append(ll.val)
                    ll = ll.next
            except:
                if ll is None:
                    print('here')
                    continue
        if len(res) < 1:
            return None
        res.sort()
        print(res)
        head = ListNode(res[0])
        cur = head

        for i in range(1, len(res)):
            node_item = res[i]
            # print("node item is", str(node_item))
            cur.next = ListNode(node_item)
            cur = cur.next
        return head


