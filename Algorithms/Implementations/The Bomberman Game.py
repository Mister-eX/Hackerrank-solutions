def bomberMan(n, grid, r, c):
    three = [['O' for _ in range(c)] for i1 in range(r)]
    five = [['O' for _ in range(c)] for i1 in range(r)]
    even = [['O' for _ in range(c)] for i1 in range(r)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                three[i][j] = '.'
                for i1 in range(4):
                    if i + dr[i1] < 0 or i + dr[i1] >= r:
                        continue
                    if j + dc[i1] < 0 or j + dc[j1] >= c:
                        continue
                    three[i + dr[i1]][j + dc[i1]] = '.'

    for i in range(r):
        for j in range(c):
            if three[i][j] = 'O':
                five[i][j] = '.'
                for i1 in range(4):
                    if i +dr[i1] < 0 or i + dr[i1] >= r:
                        continue
                    if j + dc[i1] < 0 or j + dc[i1] >= c:
                        continue
                    five[i + dr[i1]][j + dc[i1]] = '.'

    Three = [''.join(a) for a in three]
    FIve = [''.join(a) for a in five]
    Even = [''.join(a) for a in even]
    if n == 1:
        return grid
    elif n % 2 == 0:
        return Even
    elif (n + 4) % 4 == 3:
        return Three
    else:
        return FIve