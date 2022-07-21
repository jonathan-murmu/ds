"""
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        queue = collections.deque()
        # initialize queue with root node
        if root:
            queue.append(root)

        # loop until queue is empty
        while queue:
            # dequeue from queue
            cur = queue.popleft()

            # swap
            temp = cur.left
            cur.left = cur.right
            cur.right = temp

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root

#         if root == None:
#             return

#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         # swap
#         temp = root.left
#         root.left = root.right
#         root.right = temp

#         return root