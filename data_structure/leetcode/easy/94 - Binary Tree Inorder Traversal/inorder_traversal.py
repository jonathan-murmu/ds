"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
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

    def inorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        self.inorderTraversal(root.left)
        self.list.append(root.val)
        self.inorderTraversal(root.right)

        return self.list

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initialize the stack and result_list with empty list
        stack = []
        self.list = []

        # iterate infinitely
        while True:
            # iterate untill root is None
            while root:
                # push all the left nodes
                stack.append(root)
                root = root.left

            # if stack is empty then return the result
            if not stack:
                return self.list

            # pop the stack into node
            node = stack.pop()
            # add into the result list as this will be the last node with no more left.
            self.list.append(node.val)
            # move to node's right
            root = node.right


