'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
'''
from itertools import accumulate


def max_sub_array(nums):
    # dynamic programming
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        y = nums[i]
        x=nums[i] + dp[i - 1]
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)

    # # divide an conquer
    # def helper(beg, end):
    #     if beg + 1 == end: return nums[beg]
    #     mid = (beg + end) // 2
    #     sum_1 = helper(beg, mid)
    #     sum_2 = helper(mid, end)
    #     right = max(accumulate(nums[beg:mid][::-1]))
    #     left = max(accumulate(nums[mid:end]))
    #     return max(sum_1, sum_2, left + right)
    #
    # return helper(0, len(nums))

    # # kadane Algo
    cur_max, max_till_now = 0, -inf
    for c in nums:
        # cur_max = maximum of cur no and cur_max+cur_no
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)  # which is the max(max_till_now) amoung the cur maxs
    return max_till_now

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(nums))
