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
            
            output_arr = []
            stack = []
            # base case
            if root == None:
                return output_arr
            
            cur_node = root
            while cur_node != None or len(stack) > 0: # goes until reaches the farthest right node
                while cur_node != None: # goes until reaches the farthest left node
                    stack.append(cur_node)
                    cur_node = cur_node.left

                cur_node = stack.pop()
                output_arr.append(cur_node.val)
                cur_node = cur_node.right
            return output_arr

            # another solution
            # if root is None:
            #     return []
            # list = []
            # stack = []
            # ref = root
            # while ref is not None or len(stack) > 0:
            #     if ref is None:
            #         ref = stack.pop()
            #         list.append(ref.val)
            #         ref = ref.right
            #         continue
            #     stack.append(ref)
            #     ref = ref.left
            # return list

            
