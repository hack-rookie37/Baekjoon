import sys

n = int(sys.stdin.readline())
dp = [1]*(n+1)
arr = [0, *list(map(int, sys.stdin.readline().split()))]

for i in range(1, n + 1):
    for j in range(1, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))