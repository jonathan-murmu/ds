"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list = []

    # recursion
    def preorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return

        self.list.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.list

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initialize stack with root
        stack = [root]
        # iterate till stack is empty
        while stack:
            # pop from stack and store in current
            current = stack.pop()
            # check if current is not null
            if current:
                # add in return list
                self.list.append(current.val)
                # push right in stack, right because its pre traversal backwards
                # As pretraveral is Root-L-R. Backwards will be Right then left
                stack.append(current.right)
                # push left in stack
                stack.append(current.left)

        return self.list



