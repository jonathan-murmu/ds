

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        # find the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap ith element with the minimum
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

arr = [83,5,24,45,4,1,10]

selection_sort(arr)

print(arr)