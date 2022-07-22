import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(x for _ in range(n) if (x := int(input())) <= 10000)

dp = [0] + [float("inf")] * k

for i in coins:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] = min(dp[j - i] + 1, dp[j])

print(dp[-1] if dp[-1] != float("inf") else -1)
