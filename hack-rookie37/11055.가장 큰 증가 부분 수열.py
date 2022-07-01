import sys

input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
dp = s[:]

for i in range(N):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[i], dp[j] + s[i])

print(max(dp))
