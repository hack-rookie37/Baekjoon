import sys

n = int(sys.stdin.readline())
h = []
dp = []

for i in range(n):
    h.append(list(map(int, sys.stdin.readline().split())))

    if i == 0:
        dp.append(h[0])
    else:
        dp.append([ h[i][0] + min(dp[i - 1][1], dp[i - 1][2]),
                    h[i][1] + min(dp[i - 1][0], dp[i - 1][2]),
                    h[i][2] + min(dp[i - 1][0], dp[i - 1][1])])

print(min(dp[n - 1]))