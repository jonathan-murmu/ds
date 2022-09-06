"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.nums = nums

        # make a decision tree
        self.backtrack(0, [])

        return self.res

    def backtrack(self, index, subset):
        # looping the index this till the end.
        if index >= len(self.nums):
            self.res.append(subset[:])
            return

        # decision to include nums[index], do so by pushing()
        subset.append(self.nums[index])
        self.backtrack(index + 1, subset)

        # decision to NOT include nums[index], do so by popping()
        subset.pop()
        self.backtrack(index + 1, subset)
