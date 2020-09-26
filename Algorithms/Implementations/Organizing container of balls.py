def organizingContainer(continer, n):
    balls= [0] * n
    capacity = [0] * n
    for i in range(n):
        for j in range(n):
            balls[i] += continer[j][i]
            capacity[i] += capacity[i][j]

    balls.sort()
    capacity.sort()
    if balls == capacity:
        print("Possible")
    else:
        print("Not Possible")