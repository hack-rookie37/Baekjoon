import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
aq = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            aq.append((i, j))

def bfs(oy, ox):
    q = deque()
    q.append((oy, ox))

    visited = [[0] * m for _ in range(n)]
    visited[oy][ox] = 1

    b_ans = 0

    while q:
        y, x = q.popleft()
        
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not(0 <= ny < n and 0 <= nx < m):
                continue
            
            if visited[ny][nx]:
                continue

            if graph[ny][nx] == 'W':
                continue

            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
            b_ans = max(visited[ny][nx], b_ans)

    return b_ans


ans = 0
while aq:
    y, x = aq.popleft()

    ans = max(ans, bfs(y, x))

print(ans - 1)