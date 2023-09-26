"""Given an array of N distinct elements, the task is to find all elements in array except two greatest
elements in sorted order.
Example 1:
Input :
a[] = {2, 8, 7, 1, 5}
Output :
1 2 5
Explanation :
The output three elements have two or
more greater elements.
Example 2:
Input :
a[] = {7, -2, 3, 4, 9, -1}
Output :
-2 -1 3 4"""

# def except2greats(arr):  # O(nlog(n))
#     arr = sorted(arr)
#
#     return arr[:-2]

def except2greats(arr):  # O(n)
    first = float('-inf')
    second = float('-inf')

    for i in arr:
        if i > first:
            second = first
            first = i
        else:
            if i > second:
                second = i

    result = []
    for i in arr:
        if i < second:
            result.append(i)

    return result

a = [2, 8, 7, 1, 5]  # [1,2,5]
b = [7, -2, 3, 4, 9, -1]  # [-2, -1, 3, 4]
result = except2greats(a)

print(result)