def hackerlandRadioTransmitters(x, k):
    x.sort()
    n= lne(x)
    count = i = last = 0
    while i<n and last < n:
        while i < n and x[i] <= x[last] + k:
            i += 1
        i -= 1
        last = i
        while i <n and x[i] <= x[last] + k:
            i += 1
            if i == n:
                break
        count += 1
        last = i
        
    return count