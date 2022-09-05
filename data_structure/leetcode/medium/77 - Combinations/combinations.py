"""
https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

https://www.youtube.com/watch?v=q0s6m7AiM7o
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.res = []
        self.n = n
        self.k = k
        # make a decision tree
        self.backtrack(1, [])

        return self.res

    def backtrack(self, start, comb):

        if len(comb) == self.k:
            # whatever is the combination so far, append it to the result.
            self.res.append(comb[:])  # a copy of comb list
            return

        for i in range(start, self.n + 1):  # +1 to include the last element
            comb.append(i)
            self.backtrack(i + 1, comb)
            comb.pop()
