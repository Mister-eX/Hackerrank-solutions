def game_of_two_stack(x, A, B, n, m):
    temp = i = j = count = s =0
    while i < n and s+A[i] <= x:
        s += A[i]
        i += 1
    count = i
    
    while j < m and i >= 0:
        s += B[j]
        j += 1
        while s > x and i > 0:
            i -= 1
            s -= A[i]
        
        if s <= x and i + j > count:
            count = i + j

    return count



    '''other method'''

def game_of_two_stack2(x, A, B, n, m):
    sumA, sumB = [0], [0]
    cur = 0
    for i in range(n):
        cur += A[i]
        sumA.append(cur)

    cur = 0
    for j in range(m):
        cur += B[j]
        sumB.append(cur)

    j = m
    ans = 0
    for i in range(n+1):
        while j >= 0 and sumA[i] + sumB[j] > x:
            j -= 1
        if j >= 0 and i + j > ans:
            ans = i + j

    return ans