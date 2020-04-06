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

# ITERATIVE SOLUTION - O(n)
"""
from collections import deque
class Solution:
    def levelOrder(self, root):
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels
"""