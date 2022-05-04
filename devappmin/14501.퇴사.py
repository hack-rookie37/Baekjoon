import sys
input = sys.stdin.readline

n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for idx in range(n):
    pos = idx
    m = 0
    for i in range(idx):
        if i + li[i][0] <= idx and dp[i] > m:
            m = dp[i]
            pos = i

    if li[idx][0] + idx > n:
        continue

    dp[idx] = dp[pos] + li[idx][1]

print(max(dp))