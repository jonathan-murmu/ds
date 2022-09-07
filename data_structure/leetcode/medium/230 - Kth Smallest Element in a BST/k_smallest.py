"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
https://www.youtube.com/watch?v=5LUXSvjmGCw

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        i = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            i += 1
            if i == k:
                return cur.val

            cur = cur.right

#     def kthSmallest(self, root, k):
#         """
#         :type root: TreeNode
#         :type k: int
#         :rtype: int
#         """
#         self.i = 1
#         self.k_smallest = None
#         self.inorder(root,k)
#         return self.k_smallest

#     def inorder(self, root, k):
#         if not root:
#             return

#         self.inorder(root.left, k)

#         if self.i == k:
#             self.k_smallest = root.val

#         self.i += 1

#         self.inorder(root.right, k)
