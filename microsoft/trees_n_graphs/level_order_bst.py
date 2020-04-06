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
                # call helper function here
        levels = []

        if not root:
            return levels
        self.recurisve(root, 0, levels)
        return levels

    def recurisve(self, node, level, levels):

        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)

        if node.left:
            self.recurisve(node.left, level + 1, levels)
        if node.right:
            self.recurisve(node.right, level + 1, levels)

    # TIME and SPACE - O(n) >> travelling all node and appending all nodes

