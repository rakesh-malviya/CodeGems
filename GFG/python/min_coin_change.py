def coin_change(A,c):
    A = sorted(A)
    dp = [0 for _ in range(c+1)]
    minC = c+99
    mindp = [minC for _ in range(c+1)]

    dp[0] = 1
    mindp[0] = 0
    for coin in A:
        for i in range(coin,c+1):
            dp[i] += dp[i - coin]
            mindp[i] = min(mindp[i],mindp[i-coin]+1)

    if mindp[c]==minC:
        return 0

    return mindp[c]#dp[c]

A = [9, 6, 5, 1]
print(coin_change(A,19))


