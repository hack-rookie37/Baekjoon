N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
# 0: 가로, 1: 대각, 2: 세로

for i in range(N):
    for j in range(1, N):
        if room[i][j]:
            continue
        if i > 0:
            dp[i][j][2] += sum(dp[i - 1][j][1:])
        if j > 0:
            dp[i][j][0] += sum(dp[i][j - 1][:2])
        if i * j > 0 and room[i - 1][j] + room[i][j - 1] == 0:
            dp[i][j][1] += sum(dp[i - 1][j - 1])

print(sum(dp[-1][-1]))
