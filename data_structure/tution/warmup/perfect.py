"""
Given an array of size N and you have to tell whether the array is perfect or not. An array is said
to be perfect if it's reverse array matches the original array. If the array is perfect then print
"PERFECT" else print "NOT PERFECT".
Example 1:
Input : Arr[] = {1, 2, 3, 2, 1}
Output : PERFECT
Explanation:
Here we can see we have [1, 2, 3, 2, 1]
if we reverse it we can find [1, 2, 3, 2, 1]
which is the same as before.
So, the answer is PERFECT.
Example 2:
Input : Arr[] = {1, 2, 3, 4, 5}
Output : NOT PERFECT
"""
from copy import deepcopy


def reverse(num):
    """
    Reverse an array
    :param num: positive integer array
    :return: array of reversed number
    """
    n = len(num)
    for i in range((n+1)//2):  # +1 because range end in exclusive
        num[i], num[n-i-1] = num[n-i-1], num[i]

    print('reserver', num)
    return num

def perfect(num):
    original_num = deepcopy(num)
    if reverse(num) == original_num:
        print('perfect')
    else:
        print('not perfect')

perfect([1,2,3,2,1])