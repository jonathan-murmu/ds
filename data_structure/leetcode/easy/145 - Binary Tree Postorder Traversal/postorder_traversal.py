"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
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

    def postorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.list.append(root.val)

        return self.list

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initialize stack with root
        stack = [root]

        # iterate till stack is empty
        while stack:
            # pop one element
            temp = stack.pop()
            if temp:
                # if temp is a tree node
                if isinstance(temp, TreeNode):
                    # postorder is LeftRightNode. So push backwards i.e. NodeRightLeft
                    # push everything backwards i.e. NodeRightLef
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                # if temp is a node data
                else:
                    self.list.append(temp)

        return self.list

