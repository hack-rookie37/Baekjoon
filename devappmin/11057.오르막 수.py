import sys

n = int(sys.stdin.readline())

dp = [[1] * 10 for _ in range(n)]

for i in range(1, n):
    for j in range(8, -1, -1):
        dp[i][j] = ( dp[i][j + 1] + dp[i - 1][j] ) % 10007

print(sum(dp[n - 1]) % 10007)

# 1     1 1 1 1 1 1 1 1 1 1     10
# 2     10 9 8 7 6 5 4 3 2 1    55
# 3     10 6 3 1 
#