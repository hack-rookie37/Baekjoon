import sys

MAX = 1000000009

dp = [[0] * 4 for _ in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for idx in range(4, 100001):
    dp[idx][1] = dp[idx - 1][2] % MAX + dp[idx - 1][3] % MAX
    dp[idx][2] = dp[idx - 2][1] % MAX + dp[idx - 2][3] % MAX
    dp[idx][3] = dp[idx - 3][1] % MAX + dp[idx - 3][2] % MAX


for _ in range(int(sys.stdin.readline())): print(sum(dp[int(sys.stdin.readline())]) % MAX)