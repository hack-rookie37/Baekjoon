import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

n, m = map(int, input().split())
tmap = [list(input().rstrip()) for _ in range(n)]
land = []
answer = 0

for i in range(n):
    for j in range(m):
        if tmap[i][j] == 'L': # 육지인 부분 모두 찾기
            land.append((i, j))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    tmap[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            
            if tmap[nx][ny] != 'W': # 육지일 때
                visited[nx][ny] = True
                q.append((nx, ny))
                tmap[nx][ny] = tmap[x][y] + 1
    return tmap[x][y] # 마지막으로 체크한 육지가 시작 지점에서 가장 먼 육지임

for i, j in land:
        visited = [[False for _ in range(m)] for _ in range(n)]
        answer = max(answer, bfs(i, j))

print(answer)