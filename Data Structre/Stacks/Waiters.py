from collections import deque

# Seive Algorithm for finding primes
def generate_primes():
    test = [True] * 10001
    primes = deque()
    i = 2

    while(i*i <= 10000):
        if test[i] == True:
            for j in range(2 * i, 10001, i):
                test[j] = False
        i += 1

    for i in range(2, 10001):
        if test[i]:
            primes.append(i)

    return primes



def waiter(numbers, q):
    primes = generate_primes()
    stack = deque()
    result = deque()

    if num in numbers:
        if num % primes[0] != 0:
            stack.append(num)
        else:
            result.append(num)

    for i in range(1, q):
        temp = deque()
        while stack:
            num = stack.pop()
            if num % primes[i] != 0:
                temp.append(num)
            else:
                result.append(num)
        stack = temp
    
    while stack:
        result.append(stack.popleft())
    
    return result