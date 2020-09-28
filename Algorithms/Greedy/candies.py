def candies(n, arr):
    res = [1]*n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            res[i] = res[i -1] + 1

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i + 1] and res[i] <= res[i + 1]:
            res[i] = res[i + 1] +1
    
    count = 0
    for i in range(n):
        count += res[i]

    return count