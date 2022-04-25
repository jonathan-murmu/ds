"""
https://leetcode.com/problems/duplicate-zeros/

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""


class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # find number of zeros, to determine the displacement, i.e. how
        # many places to move (the last element)
        zero_count = 0
        for num in arr:
            if num == 0:
                zero_count += 1

        displacement = zero_count

        for i in range(len(arr) - 1, -1, -1):

            # Check if the array is long enough to make that displacement. In
            # cases where it is not, the element will be discarded
            # if satisfies the condition then simply make the replacement(even zeros, zeros will be checked later)
            if (i + displacement) < len(arr):
                arr[i + displacement] = arr[i]

            # Every time we reach a zero, reduce displacement by one, because
            # the number of zeros before that is current displacement - 1
            if arr[i] == 0:
                displacement -= 1  # if zero, reduce the displacement,

                # Zeroes need to be duplicated, so we do this once again for zeros
                if (i + displacement) < len(arr):
                    arr[i + displacement] = arr[i]


obj = Solution()
# arr = [1,0,2,3,0,4,5,0]
# obj.duplicateZeros(arr)
# print(arr)  # [1, 0, 0, 2, 3, 0, 0, 4]

arr = [8,4,5,0,0,0,0,7]
obj.duplicateZeros(arr)
print(arr)  # [8, 4, 5, 0, 0, 0, 0, 0]
