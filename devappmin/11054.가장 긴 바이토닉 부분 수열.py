import sys

n = int(sys.stdin.readline())
dp = [1] * (n + 1)
arr = [0] + list(map(int, sys.stdin.readline().split()))
answer = 0

for center in range(n):
    dp = [1] * (n + 1)
    for idx in range(1, center + 1):
        for inner in range(1, idx):
            if arr[idx] > arr[inner]:
                dp[idx] = max(dp[idx], dp[inner] + 1)
        
    for idx in range(center, n + 1):
        for inner in range(center, idx):
            if arr[idx] < arr[inner]:
                dp[idx] = max(dp[idx], dp[inner] + 1)
    
    answer = max(answer, max(dp))

print(answer)