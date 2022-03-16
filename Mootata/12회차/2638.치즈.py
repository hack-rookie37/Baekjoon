import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1] # 상 하 좌 우

n, m = map(int, input().split()) # 세로 길이 n, 가로 길이 m
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
air_inside = set() # 치즈 내부의 공기
cheese = set() # 치즈의 위치
cq = deque()
time = 0

for i in range(n): # 내부 공기만 남기기 위해 공기 부분 air_inside에 담기
    for j in range(m):
        if paper[i][j] == 0:
            air_inside.add((i, j))
        else:
            cheese.add((i, j))
            cq.append((i, j))

def air():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    air_inside.discard((0, 0)) # (0, 0)은 내부 공기가 될 수 없음
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if not visited[nx][ny] and paper[nx][ny] == 0: # 방문한 적 없고, 공기인 부분
                q.append((nx, ny))
                visited[nx][ny] = True
                
                if (nx, ny) in air_inside: # 외부 공기인 (0, 0)부터 탐색을 시작했는데, 위의 if문 안에 들어왔다는건 외부공기라는 뜻이므로 air_inside에서 지워줌
                    air_inside.discard((nx, ny)) # 외부 공기를 지워서 내부 공기만 남도록 함
                

def melting():
    while cq:
        count = 0
        x, y = cq.popleft()
        visited[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if paper[x][y] == 1 and not visited[nx][ny] and paper[nx][ny] == 0 and (nx, ny) not in air_inside: # paper[x][y]에 치즈가 있고, 외부 공기와 닿아있으며 그 공기가 현재의 BFS사이클에서 녹아서 생긴 것이 아닐 경우에
                count += 1
                if count == 2: # 닿아있는 외부 공기가 두 곳 이상이라면
                    paper[x][y] = 0
                    cheese.discard((x, y))

while True:
    if air_inside: # air_inside가 비어있다는 것은 내부 공기가 존재하지 않는다는 뜻이므로 내부 공기를 찾는 air() 실행할 필요 없음
        visited = [[False for _ in range(m)] for _ in range(n)]
        air()
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    melting()
    time += 1
    
    if not cheese:
        print(time)
        break
    
    for i in cheese:
        cq.append(i)


# 일단 모든 공기를 air_inside에 담고, air() 함수를 통해 외부 공기인 것들을 air_inside에서 삭제해서
# 내부 공기만 남도록 함.

# 치즈가 녹는 것을 구현할 때, 내부공기가 아닌 공기가 2개 이상 접촉했을 때만 녹도록 하고,
# 한번의 bfs 사이클 도중에 치즈가 녹아 공기가 된 부분이 다른 치즈에 영향을 주지 않도록 함

# 이 두 과정을 치즈가 모두 녹을 때까지 반복하는데 만약 공기 탐색과정에서 내부공기가 하나도 없다면
# 그 다음부터는 공기 탐색은 진행하지 않음.