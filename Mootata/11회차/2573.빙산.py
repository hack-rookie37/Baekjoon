import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
n, m = map(int, input().split()) # 행의 개수 n, 열의 개수 m
sea = [list(map(int, input().split())) for _ in range(n)]
time = 0

def melting(): # 바다와 인접한 빙산이 녹는 bfs
    while q:
        x, y, = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0:
                continue
            elif nx >= n or ny >= m:
                continue
            
            # visited를 체크하는 이유는 이번 bfs를 돌면서 녹아 0이 된 부분이 존재할 때, 그 부분과 인접한 빙산이 녹지 않게 하기 위해서임
            if not visited[nx][ny] and sea[nx][ny] == 0 and sea[x][y] > 0:
                sea[x][y] -= 1

def bfs(i, j): # 바다에 빙산이 몇 덩어리나 있는지 확인하는 bfs
    q2 = deque()
    q2.append((i, j))
    visited[i][j] = True
    
    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0:
                continue
            elif nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and sea[nx][ny] != 0:
                q2.append((nx, ny))
                visited[nx][ny] = True

while True:
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0 # 빙산의 수
    
    for i in range(n): # 바다에 빙산이 몇 덩어리나 있는지 체크
        for j in range(m):
            if not visited[i][j] and sea[i][j] != 0:
                bfs(i, j)
                count += 1
    if count >= 2: # 두 덩어리 이상이라면 종료
        print(time)
        break
    elif count == 0: # 빙산이 존재하지 않으면 종료
        print(0)
        break
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n): # 빙산의 위치 queue에 넣음
        for j in range(m):
            if sea[i][j] != 0:
                q.append((i, j))
                visited[i][j] = True # 방문처리 해서 빙산이 녹아 0이 된 부분이 다른 빙산에 영향을 주지 않도록 함
    melting()
    time += 1

# 0 1 2
# 0 0 3
# 0 0 0 
# 위와 같은 상황에서 melting 함수가 실행됐을 때 queue에는 (0, 1), (0, 2), (1, 2) 가 들어있고
# 큐에 있는 순서대로 빙산이 녹을텐데 가장 처음 녹을 (0,1) 는 1이기 때문에 0이 되어버려서 따로 체크해두지않으면 (0, 2)가 녹는 것에 영향을 줌.
# 따라서 큐에 넣을 때 해당 위치는 visited를 이용해 방문처리(True) 해두고, melting 함수에서 빙하가 녹기 위한 조건은 (인접한 곳의 값이 0이면서, visited가 False인 부분과 인접했을 때)만 녹도록 함.