"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        num1 = sorted(nums1)
        num2 = sorted(nums2)

        p1 = 0
        p2 = 0

        while p1 < len(num1) and p2 < len(num2):
            if num1[p1] < num2[p2]:
                p1 += 1
            elif num2[p2] < num1[p1]:
                p2 += 1
            else:
                result.append(num1[p1])
                p1 += 1
                p2 += 1
        return result

#         count = {}
#         result = []
#         # pick 1st list
#         # iterate and increment the count

#         for i in nums1:
#             count[i] = count.get(i, 0) + 1

#         # pick 2nd list
#         #iterate and check if exists in count dict
#         for i in nums2:
#             if i in count and count[i] > 0:
#                 count[i] -= 1
#                 result.append(i)
#         return result
