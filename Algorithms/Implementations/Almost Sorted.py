def check_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def almostSorted(arr):
    n = len(arr)
    if check_sorted(arr):
        print('yes')
        return 

    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            break

    for j in range(n-1, 0, -1):
        if arr[j] < arr[j -1]:
            break

    if check_sorted(swap(arr[:], i, j)):
        print('yes')
        print('swap {} {}'.format(i+1, j+1))
        return 

    for k in range(i, math.ceil((j + i)/2), 1):
        arr = swap(arr, k, i + j -k)

    if check_sorted(arr):
        print('yes')
        print('reverse {} {}'.format(i + 1, j + 1))
        return
    
    print('no')