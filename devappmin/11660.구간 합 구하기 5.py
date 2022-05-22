import sys

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (n + 1)] + [[0] * (n + 1) for _ in range(n)]

for y in range(1, n + 1):
    for x in range(1, n + 1):
        dp[y][x] = dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1] + graph[y - 1][x - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])