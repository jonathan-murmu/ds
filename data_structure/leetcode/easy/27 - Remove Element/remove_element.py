"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = 0  # last position where val is found
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
            elif nums[i] != val:
                nums[i], nums[last] = nums[last], nums[i]  #swap
                last += 1
                count +=1
            else:
                last += 1
                count += 1
        return count


# Removing unwanted lines, same algo though
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = 0  # last position where val is found
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last] = nums[i]  #replace
                last += 1
        return last


# different algo: simple replace the last element of the array with the found element, reduce the array size.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while (i<n):
            if nums[i] == val:
                # simply replace with last element of array, as order does not matter.
                nums[i] = nums[n-1]
                n -=1
            else:
                i += 1
        return n