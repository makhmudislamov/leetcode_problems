"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
            # TODO: Create queue to store nodes not yet traversed in level-order
        queue = []
        # TODO: Enqueue given starting node
        queue.append(root)
        # TODO: Loop until queue is empty
        while:
            # TODO: Dequeue node at front of queue
            node = ...
            # TODO: Visit this node's data with given function
            ...
            # TODO: Enqueue this node's left child, if it exists
            ...
            # TODO: Enqueue this node's right child, if it exists
            ...
        pass
