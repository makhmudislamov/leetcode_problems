"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        # traverse until reach left child leaf
        # visit node
        #  traverse until you reach the rightest child leaf
        if root is None:
            return None
        res = []
        self.recursive(root, res)

        return res

    def recursive(self, root: TreeNode, res: []):
        if root.left != None:
            self.recursive(root.left, res)
        res.append(root.val)
        if root.right != None:
            self.recursive(root.right, res)
        
    def iterative(self, root: TreeNode, res:[]):
        current = root
        stack = []
        while current != None or len(stack) != 0:
            while current != None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        
