import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
