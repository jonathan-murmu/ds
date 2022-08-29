"""
Give an array of numbers, such that the difference between two adjacent elements are always +-1. Find the given number.
n=9
Arr =[1,2,3,2,3,4,5,3,2,3,4,5,6,7,8,9,10]
O/p - 16 # i.e. first occurrence of 9 (starting the count from 1)

"""

def l_search(arr, n):

    result = -1
    i = 0
    j = 0
    while i < len(arr):
        if arr[i] == n:
            return i + 1
        i += n - arr[i]

    return result


ar = [1,2,3,2,3,4,5,3,2,3,4,5,6,7,8,9,10]
print(l_search(ar, 9))