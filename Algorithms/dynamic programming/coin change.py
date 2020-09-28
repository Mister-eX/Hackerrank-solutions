def grtWays(n, c):
    m = len(c)
    dp = [[0 for i in range(m)] for j in range(n+1)]
    for i in range(m):
        dp[0][i]  = 1

    for i in range(1, n+1):
        for j in range(m):
            if i- c[j] >= 0:
                x = dp[i-c][j]
            else:
                x = 0

            if j >= 1:
                y = dp[i][j - 1]
            else:
                y = 0

            dp[i][j] = x+ y
    
    return dp[n][m - 1]
            