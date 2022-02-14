from collections import deque

n = int(input()) # n x n 크기의 그리드
grid = [list(input()) for _ in range(n)]
color_weakness = [[] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
visited = [[False for _ in range(n)] for _ in range(n)]
sections1 = 0
sections2 = 0
index = 0

for i in grid:
    for j in i:
        green = j.replace('R', 'G')
        color_weakness[index].append(green)
    index += 1

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True
    
def bfs2(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and color_weakness[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True
                
for k in ('R', 'G', 'B'):
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == k:
                bfs(i, j, k)
                sections1 += 1

visited = [[False for _ in range(n)] for _ in range(n)]

for k in ('G', 'B'):
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and color_weakness[i][j] == k:
                bfs2(i, j, k)
                sections2 += 1

print(sections1, sections2)