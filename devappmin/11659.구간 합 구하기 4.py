import sys

n, m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
dp = [0, nl[0]]

for i in range(1, n):
    dp.append(dp[i] + nl[i])

for m_idx in range(m):
    i, j = map(int, sys.stdin.readline().split())    
    print(dp[j] - dp[i - 1])