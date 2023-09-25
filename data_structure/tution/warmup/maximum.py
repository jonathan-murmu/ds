"""Get maximum in an array"""
def get_max(arr):
    max = float('-inf')

    for i in arr:
        if i > max:
            max = i

    return max

print(get_max([20,2,45,60,60]))