"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # calling recursive function with min and max values>>> -inf to +inf
        return self.recursive_check(root, float("-inf"), float("inf"))

    def recursive_check(self, root: TreeNode, min, max):
        if root is None:
            return True

        if root.val < min or root.val > max:
            return False

        # checking left children - max value is root value - 1
        is_valid_left = self.recursive_check(root.left, min, root.val - 1)
        # checking right children - min value is root value + 1
        is_valid_right = self.recursive_check(root.right, root.val + 1, max)
        return is_valid_left and is_valid_right
