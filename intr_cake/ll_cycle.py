"""
A singly-linked list is built with nodes, where each node has:

node.next—the next node in the list.
node.value—the data held in the node. For example, if our linked list stores people in line at the movies, 
node.value might be the person's name.
For example:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

A cycle occurs when a node’s next points back to a previous node in the list. 
The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked list and 
returns a boolean indicating whether the list contains a cycle.
"""

import unittest


def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    # Time and Space - O(n)
    # nodes_set = set()

    # while first_node != None:
    #     if first_node in nodes_set:
    #         return True
    #     else:
    #         nodes_set.add(first_node)
    #     first_node = first_node.next

    # return False
    
    # Time and Space - O(n) and O(1)
    fast = first_node
    slow = first_node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    
    
    return False



# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_two_node_cycle_at_end(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        result = contains_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        first = Test.LinkedListNode(1)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        first = Test.LinkedListNode(1)
        first.next = first
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)
