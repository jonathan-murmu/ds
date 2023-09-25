"""find 2 max in a single pass"""

def two_max(arr):
    max1 = float('-inf')
    max2 = float('-inf')

    for i in arr:
        # if new max is found
        if i > max1:
            max2 = max1  # prev max become 2nd max. and then
            max1 = i  # update the new max
        # if new max is not found
        else:
            # compare with 2nd max
            if i > max2:  # if cur is larger
                max2 = i  # update 2nd max

    return max1, max2


print( two_max([2,4,5,2,1,55,52]) )