# def binary_search(arr, x):
#     l = 0
#     r = len(arr) -1
#     mid = 0
#
#     while l <= r:
#         mid = (l + r ) // 2
#
#         if arr[mid] > x:
#             r = mid - 1
#         elif arr[mid] < x:
#             l = mid + 1
#
#         else:
#             return mid
#     return -1


def bs(arr, l, r, x):
    mid = (l + r) // 2

    if l <= r:
        if arr[mid] > x:
            return bs(arr, l, mid - 1, x)
        elif arr[mid] < x:
            return bs(arr, mid + 1, r, x)
        else:
            return mid
    else:
        return -1



def binary_search(arr, x):
    return bs(arr,0, len(arr)-1, x)


arr = [1,2,3,4,5,6,7,8]

print(binary_search(arr, 5))