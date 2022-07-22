import sys

input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]

for h in range(1, 31):
    dp[0][h] = 1

for w in range(1, 31):
    for h in range(30):
        if w + h > 30:
            break
        if h == 0:
            dp[w][h] = dp[w - 1][1]
        else:
            dp[w][h] = dp[w - 1][h + 1] + dp[w][h - 1]

while True:
    N = int(input())

    if N == 0:
        break

    print(dp[N][0])
