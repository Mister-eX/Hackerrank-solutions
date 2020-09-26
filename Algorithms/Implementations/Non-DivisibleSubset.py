from collections import defaultdict
def nonDivisibleSubset(k, arr):
    Array = defaultdict(int)
    for i in arr:
        Array[i % k] += 1

    count = min(Array[0], 1)
    if k % 2 == 0:
        count = min(Array[k//2], 1)
        n = k//2
    else:
        n = k//2 + 1

    for i in range(1, n):
        count += max(Array[i], Array[k - i])

    return count


