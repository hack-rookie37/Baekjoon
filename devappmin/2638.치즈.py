import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
air = []
q = deque()
remain = 0

for i_idx in range(n):
    row = list(map(int, input().split()))

    for j_idx in range(m):
        if row[j_idx]:
            q.append((i_idx, j_idx))
            remain += 1

    graph.append(row)


def spread_air():
    global air
    air = [[False] * m for _ in range(n)]

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if air[ny][nx]:
                continue

            if graph[ny][nx]:
                continue

            air[ny][nx] = True
            q.append((ny, nx))


def bfs():
    visited = [[0] * m for _ in range(n)]

    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if air[ny][nx]:
                visited[y][x] += 1
    q.clear()

    global remain

    for i_idx in range(n):
        for j_idx in range(m):
            if graph[i_idx][j_idx] == 1:
                if visited[i_idx][j_idx] >= 2:
                    graph[i_idx][j_idx] = 0
                    remain -= 1
                else:
                    q.append((i_idx, j_idx))


ans = 0
while remain:
    spread_air()
    bfs()
    ans += 1

print(ans)
