import sys

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]


def dfs(y, x):
    global ans
    if y == n - 1 and x == m - 1:
        return 1

    if visited[y][x] != -1:
        return visited[y][x]

    visited[y][x] = 0

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < n and 0 <= nx < m):
            continue

        if graph[ny][nx] >= graph[y][x]:
            continue

        visited[y][x] += dfs(ny, nx)

    return visited[y][x]


print(dfs(0, 0))

# 아래는 시간초과

# import sys

# dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
# input = sys.stdin.readline

# n, m = map(int, sys.stdin.readline().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]

# ans = 0


# def dfs(y, x):
#     global ans
#     if y == n - 1 and x == m - 1:
#         ans += 1
#         return
#     if visited[y][x]:
#         return

#     visited[y][x] = True

#     for idx in range(4):
#         ny, nx = y + dy[idx], x + dx[idx]

#         if not (0 <= ny < n and 0 <= nx < m):
#             continue

#         if graph[ny][nx] >= graph[y][x]:
#             continue

#         dfs(ny, nx)

#     visited[y][x] = False


# dfs(0, 0)
# print(ans)
