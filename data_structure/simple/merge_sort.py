


def merge(A, l, mid, r):

    # create 2 arrary.
    # 1st l to mid
    # 2nd mid + 1 till r

    n1 = (mid - l) + 1  # size of 1st array
    n2 = r - mid  # size of 2nd array

    L = []
    for i in range(n1):
        L.append(A[l+i])

    R = []
    for i in range(n2):
        R.append(A[mid+1+i])  # +1 because mid is done in previour loop

    i = j = 0
    k = l

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

    print('A', A)


def merge_sort(A, l, r):
    if l < r:

        mid = (l+r)//2
        print(l,mid,r)

        merge_sort(A, l, mid)
        merge_sort(A, mid+1, r)

        merge(A, l, mid, r)

arr = [12,11,13,5,6,7]

merge_sort(arr, 0, len(arr)-1)

print(arr)