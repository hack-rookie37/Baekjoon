import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = [*map(int, input().split())]
    M = int(input())

    dp = [[1] + [0] * M for _ in range(N)]

    for m in range(1, M + 1):
        if m % coins[0] == 0:
            dp[0][m] = 1

    for n in range(1, N):
        for m in range(1, M + 1):
            dp[n][m] = dp[n - 1][m]
            if coins[n] <= m:
                dp[n][m] += dp[n][m - coins[n]]

    print(dp[-1][-1])
