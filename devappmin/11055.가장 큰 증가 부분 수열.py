import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
dp[0] = arr[0]

for start_idx in range(1, n):
    for next_idx in range(start_idx):
        if arr[next_idx] < arr[start_idx]:
            dp[start_idx] = max(dp[next_idx] + arr[start_idx], dp[start_idx])
        else:
            dp[start_idx] = max(dp[start_idx], arr[start_idx])

print(max(dp))