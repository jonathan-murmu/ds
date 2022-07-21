"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # initialize the queue
        queue = collections.deque()

        # initialize level to 0
        level = 0
        if root:
            # initialize queue to (node, 1st level)
            queue.append((root, 1))  # (node, level)

        # until queue is empty
        while queue:
            # dequeue element from queue
            cur = queue.popleft()

            # extract the node and level
            cur_node = cur[0]
            cur_level = cur[1]  # level

            # if current level is more the max_level
            # update the max level
            if cur_level > level:
                level += 1

            # go to next level.
            if cur_node.left:
                queue.append((cur_node.left, level + 1))

            if cur_node.right:
                queue.append((cur_node.right, level + 1))

        return level

