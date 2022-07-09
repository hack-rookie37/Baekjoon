import sys

n = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
dp = [1] * (n + 1)

for pos in range(1, n + 1):
    for inner in range(1, pos):
        if nums[pos] < nums[inner]:
            dp[pos] = max(dp[inner] + 1, dp[pos])

print(max(dp))