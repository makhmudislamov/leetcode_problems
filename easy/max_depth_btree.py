"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3, 9, 20, null, null, 15, 7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3

Explanation in LeetCode : https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/ 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # TOP DOWN SOLUTION - pre-prder traversal
        # base case
        if root == None:
            return 0
        
        # call the function recursively
        # for left and right children
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # returning max of left and right children depth, +1 is adding the depth of the root
        return max(left, right) + 1

        # Runtime O(N) - since we are going throught the whole tree
        
