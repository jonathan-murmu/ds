"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: Optional[TreeNode], level=1) -> List[List[int]]:
        if root:
            if level < len(self.res):  # this means existing level,
                self.res[level].append(root.val)  # for left view comment this line
                pass
            else:  # if level is more that result array, that means a new level found
                self.res.append([root.val])
                pass

            self.levelOrder(root.left, level + 1)
            self.levelOrder(root.right, level + 1)

        return self.res
