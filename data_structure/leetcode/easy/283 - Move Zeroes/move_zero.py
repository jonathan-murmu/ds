"""
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers -> slow and fast
        slow = 0
        for fast in range(len(nums)):
            # fast is increment at every iteration
            # if fast != 0 and slow == 0 then swap
            if nums[fast] != 0 and nums[slow] == 0:
                # swap
                nums[fast], nums[slow] = nums[slow], nums[fast]

            # if slow != 0 then increment it
            if nums[slow] != 0:
                slow += 1



