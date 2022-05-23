"""
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the actual rotation or slipting distance.
        length = len(nums)
        if k > length:
            k = k % length
        elif k == length:
            return

        # reverse the entire array
        self.reverse(nums, i=0, j=length - 1)

        # reverse the 1st half
        self.reverse(nums, i=0, j=k - 1)

        # reverse the 2n half
        self.reverse(nums, i=k, j=length - 1)

    def reverse(self, nums, i=None, j=None):
        while (i < j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

            i += 1
            j -= 1


#         temp = 0
#         length = len(nums)

#         if k != length:
#             for rounds in range(k):
#                 for i in range(length-2, -1, -1):
#                     if i == length-2:
#                         temp = nums[i+1]
#                     nums[i+1] = nums[i]

#                     if i == 0:
#                         nums[0] = temp
# n = len(nums)
# k = k % n
# nums[:] = nums[n-k:] + nums[:n-k]


obj = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
obj.rotate(nums, k)

print(nums)