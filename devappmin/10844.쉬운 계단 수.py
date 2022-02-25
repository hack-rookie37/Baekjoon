import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for idx in range(1, n):
    for item in range(10):
        if item == 0:
            dp[idx][item] += dp[idx - 1][item + 1]
        elif item == 9:
            dp[idx][item] += dp[idx - 1][item - 1]
        else:
            dp[idx][item] += dp[idx - 1][item - 1] + dp[idx - 1][item + 1]

print(sum(dp[n - 1]) % 1000000000)


# 0 1 1 1 1 1 1 1 1 1
# 1 2 2 2 2 2 2 2 2 1