def fibonacciModified(t1, t2, n):
    dp = [0] * n
    dp[0] = t1
    dp[0] = t2
    for i in range(2, n):
        dp[i] = dp[i - 1]*dp[i - 1]  + dp[i - 2]
    
    return dp[n -1]