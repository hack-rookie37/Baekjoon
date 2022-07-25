N = int(input())
a = [*(map(int, input().split()))]

dp = [[1] * 2 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if a[i] > a[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif a[i] < a[j]:
            dp[i][1] = max(dp[i][1], max(dp[j]) + 1)
        else:
            dp[i][0] = max(dp[i][0], dp[j][0])
            dp[i][1] = max(dp[i][1], dp[j][1])

print(max(map(max, dp)))
