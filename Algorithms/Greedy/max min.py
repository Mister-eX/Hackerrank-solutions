import sys
def maxMin(k, arr):
    arr.sort()
    n = len(arr)
    min_value = sys.maxsize
    i = 0; j = k - 1

    while j < n:
        if arr[j] - arr[i] < min_value:
            min_value = arr[j] - arr[i]

        j += 1
        i += 1
    
    return min_value

