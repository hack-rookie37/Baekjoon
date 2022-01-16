from collections import deque

n, m = map(int, input().split())
field = [list(map(int, input())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 1

def bfs(x, y, b):
    queue = deque()
    queue.append((x, y, b))
    
    while queue:
        x, y, b = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][b]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if field[nx][ny] == 1 and b == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                if field[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    queue.append((nx, ny, b))
    return -1
        
print(bfs(0, 0, 1))