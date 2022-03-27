import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range((n + 1))]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = graph[i - 1][j - 1] + \
            max(dp[i][j-1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[n][m])

# dy, dx = [1, 1, 0], [1, 0, 1]

# def sol1():
#     q = deque()
#     q.append((0, 0))

#     while q:
#         y, x = q.popleft()

#         for idx in range(3):
#             ny, nx = y + dy[idx], x + dx[idx]

#             if not (0 <= ny < n and 0 <= nx < m):
#                 continue

#             if dp[ny][nx] > dp[y][x] + graph[ny][nx]:
#                 continue

#             dp[ny][nx] = dp[y][x] + graph[ny][nx]
#             q.append((ny, nx))

#     print(dp[n - 1][m - 1])
