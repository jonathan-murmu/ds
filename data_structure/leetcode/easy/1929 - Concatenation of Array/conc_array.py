'''
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
'''
from _ast import List


class Solution:
    def getConcatenation(self, nums) -> List:
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums
        # return nums + nums

#         ans = []
#         n = len(nums)
#         for i in range(n*2):
#             if i > (n - 1):
#                 ans.append(nums[i-n])
#             else:
#                 ans.append(nums[i])
#         return ans

nums = [1,2,1]
obj = Solution()
print(obj.getConcatenation(nums))