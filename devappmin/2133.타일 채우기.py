import sys

MIN = 4
MAX = 31

n = int(sys.stdin.readline())
dp = [0 for _ in range(MAX)]
dp[2] = 3

for i in range(MIN, MAX, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(MIN, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2

print(dp[n])