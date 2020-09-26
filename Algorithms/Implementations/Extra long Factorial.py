def extra_long_factorial(n):
    result = [None] * 500
    size = 1
    result[0] = 1

    for i in range(2, n+1):
        carry = 0
        for j in range(size):
            ans = result[j] * i +carry
            result[j] = ans % 10
            carry = ans // 10

        while carry:
            result[size] = carry % 10
            carry = carry //10
            size += 1
        
    for i in range(size -1, -1, -1):
        print(result[i], end='')