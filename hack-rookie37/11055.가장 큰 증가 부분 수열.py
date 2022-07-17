N = int(input())
s = list(map(int, input().split()))
dp = [0] * 1001
for i in range(N):
    dp[s[i]] = max(dp[:s[i]]) + s[i]
print(max(dp))
