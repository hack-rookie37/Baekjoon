import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def fire_bfs(): # 불의 이동
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0:
                continue
            elif nx >= h or ny >= w:
                continue
            
            if building[nx][ny] == '.':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                building[nx][ny] = '*'

def bfs(): # 상근이의 이동
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w: # 빌딩의 범위를 벗어났다면, 탈출 성공
                return visited[x][y]
            
            if (visited[x][y] + 1 < visited[nx][ny] or visited[nx][ny] == 0) and building[nx][ny] !='#': # 불이 해당 위치까지 오는데 걸리는 시간보다 상근이가 먼저 도착 가능하다면 이동 가능, 불이 옮겨붙지 않는 곳 (visited가 0일 때)이라면 이동 가능
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 'IMPOSSIBLE'

for t in range(int(input())):
    w, h = map(int, input().split()) # 건물의 너비 w, 높이 h
    building = [list(input().rstrip()) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    q = deque()
    destinations = []
    
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*': # 불의 이동을 먼저 진행하기 위해 불만 큐에 담아줌
                q.append((i, j))
                visited[i][j] = 1
            elif building[i][j] == '@': # 상근이의 위치는 좌표만 기억
                sx, sy = i, j
                visited[i][j] = 1
    
    fire_bfs() # 불의 이동을 진행하고 각 위치로 불이 옮겨 붙는데 걸리는 시간을 visited에 기록
    
    q.append((sx, sy)) # 상근이의 위치 큐에 넣어줌
    print(bfs()) # 상근이의 이동 진행

# bfs를 이용해 불의 이동을 먼저 진행시킨 후, 각 위치 까지 불이 도달하는데 걸리는 시간을 구함.
# 상근이는 각 위치에 불이 도달하는데 걸리는 시간보다 먼저 도착할 수만 있다면 해당 위치로 이동 가능함
# 이런식으로 이동하면서 상근이가 빌딩의 테두리에 불보다 먼저 도착한다면, 탈출 성공