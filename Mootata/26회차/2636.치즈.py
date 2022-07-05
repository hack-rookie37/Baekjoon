from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
air_inside = set() # 치즈 내부의 공기
cheese = set() # 치즈의 위치
q = deque()
answer = 0 # 치즈가 모두 녹는데 걸린 시간

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
            cheese.add((i, j))
        else:
            air_inside.add((i, j))

pc = len(cheese) # 1초 전 치즈의 개수

def air():
    aq = deque()
    aq.append((0, 0))
    visited[0][0] = True
    while aq:
        x, y = aq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            
            if board[nx][ny] == 0: # bfs를 통해 치즈 외부의 공기를 air_inside set에서 지움
                air_inside.discard((nx, ny))
                aq.append((nx, ny))
                visited[nx][ny] = True

def melting():
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]: # visited를 이용해 같은 BFS 턴에 녹은 치즈로 인해 인접한 치즈가 녹는 경우 방지 가능
                continue
            
            if board[nx][ny] == 0 and (nx, ny) not in air_inside: # 치즈 외부의 공기와 접하고 있다면 0으로 바꿈
                board[x][y] = 0
                cheese.discard((x, y))

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    if air_inside:
        air()
        visited = [[False for _ in range(m)] for _ in range(n)]
    
    melting()
    answer += 1
    
    if not cheese:
        print(answer, pc, sep='\n')
        break
    else:
        pc = len(cheese)
    
    for i in cheese:
        q.append(i)