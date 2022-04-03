import sys

n = int(sys.stdin.readline())

dp = [0] * 31
dp[2] = 3

for i in range(4, n + 1, 2):
    dp[i] = dp[2] * dp[i - 2]
    
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2

print(dp[n])

# n = 2, 3
# n = 4, dp[2] * dp[2] + 2
# n = 6, dp[2] * dp[4] + 2 * dp[2] + 2
# n = 8, dp[2] * dp[6] + 2 * 2 + 2 * 3 + 2