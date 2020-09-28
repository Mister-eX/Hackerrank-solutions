def activityNotifications(arr, d):
    n = len(arr)
    count = 0
    if d >= n:
        return 0

    temp = [0] * 201
    for i in range(d):
        temp[arr[i]] += 1

    for i in range(d, n):
        mid= get_median(arr, temp, d, n)
        if arr[i] >= mid:
            count += 1
        temp[arr[i]] += 1
        temp[arr[i - d]] -= 1

    return count




def get_median(arr, count, d, n):
    temp = [0] * 201
    for i in range(201):
        temp[i] = count[i]

    for i in range(1, 201):
        temp[i] += temp[i -1]

    a = b = 0

    if d%2 != 0:
        first = d//2 + 1
        for i in range(201):
            if first <= temp[i]:
                a = 2*i
                break
    else:
        first = d//2
        second = first + 1
        i = 0
        while i < 201:
            if first <= temp[i]:
                break
            i += 1
        
        while i < 201:
            if second <= temp[i]:
                b = i
                break
            i += 1
        
    med = a + b
    return med

