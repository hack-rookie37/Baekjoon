from collections import deque

n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
answer = 1

def bfs(x, y, rain):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and location[nx][ny] > rain:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
for rain in range(max(map(max,location))):
    visited = [[False] * n for _ in range(n)]
    safe_area = 0
    for x in range(n):
        for y in range(n):
            if location[x][y] > rain and visited[x][y] == False:
                bfs(x, y, rain)
                safe_area += 1
    answer = max(answer, safe_area)
    
print(answer)