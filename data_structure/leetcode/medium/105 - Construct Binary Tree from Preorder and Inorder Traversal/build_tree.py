"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

https://www.youtube.com/watch?v=ihj4IQGZ2zc
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        # The first element in preorder is the root of the tree. Let it be x
        root = TreeNode(preorder[0])

        # mid tell us how many node we want in left
        mid = inorder.index(preorder[0])

        # Elements left to x in inorder form the LEFT subtree.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Elements right to x in inorder forms the RIGHT subtree.
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
