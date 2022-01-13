from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

# for i in range(n):
#     maze.append(list(map(int, input())))
    
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
                
    return maze[n - 1][m - 1]
    
print(bfs(0, 0))