'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def contains_duplicate(nums):
    # num_dict = {}
    #
    # for n in nums:
    #     if n in num_dict:
    #         return True
    #     else:
    #         num_dict[n] = 1
    # return False

    return len(nums) != len(set(nums))


nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))