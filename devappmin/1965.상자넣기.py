import sys

n = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for idx in range(1, n):
    for i in range(idx):
        if boxes[idx] > boxes[i]:
            dp[idx] = max(dp[idx], dp[i] + 1)

print(max(dp))
