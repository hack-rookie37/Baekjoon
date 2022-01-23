n = int(input())
location = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
answer = 1

def dfs(x, y, rain):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and location[nx][ny] > rain:
            visited[nx][ny] = True
            dfs(nx, ny, rain)
            
for rain in range(max(map(max,location))):
    visited = [[False] * n for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if location[i][j] > rain and visited[i][j] == False:
                safe_area += 1
                visited[i][j] = True
                dfs(i, j, rain)
                
    answer = max(answer, safe_area) # 둘 중에 더 큰 값을 반환
    
print(answer)