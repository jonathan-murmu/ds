"""
https://leetcode.com/problems/plus-one/
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's."""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # the above loop has exhausted, this means that digits contains all 9
        # Now we need to add digit 1 in the begining of the 0-array.

        # create a 0-array of n+1 size or use python extend()
        new_digits = [0] * (n + 1)
        # substitue 1 in 0th index
        new_digits[0] = 1
        return new_digits

#         first = True

#         carry = 0
#         result = []

#         # iterate in reverse
#         for i in digits[::-1]:
#             # check if 1st
#             if first:
#                 current_sum = i + 1 + carry
#             else:
#                 current_sum = i + carry

#             first = False

#             # check for carry
#             if current_sum > 9:
#                 carry = 1
#             else:
#                 carry = 0

#             result.append(current_sum % 10)

#         if carry:
#             result.append(carry)

#         # reverse the result array
#         return result[::-1]



