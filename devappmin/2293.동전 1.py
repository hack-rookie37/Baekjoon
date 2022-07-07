import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for idx in range(coin, k + 1):
        if idx >= coin:
            dp[idx] += dp[idx - coin]

print(dp[k])
