def countSort(arr):
    count = [0] * 100
    output  = [None] * n

    for i in range( n//2):
        arr[i][1] = str(i +1)

    for i in range(n):
        index = int(arr[i][0]) % 100
        count[index] += 1
    
    for i in range(1, 100):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = int(arr[i][0]) % 100
        output[count[index] - 1] = arr[i][1]
        count[index] -= 1

    for i in range(n):
        if output[i].isdigit():
            print("-", end=" ")
        else:
            print(output[i], end=" ")
