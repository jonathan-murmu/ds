"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # for Time=O(n) and space=O(n) => min(maxL, maxR) - heigh[i]

        # below algo will give Time=O(n) and Space=O(1)
        if not height:
            return 0

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0

        while l < r:  # untill they meet.
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])  # left max till now
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])  # right max till now
                water += r_max - height[r]

        return water