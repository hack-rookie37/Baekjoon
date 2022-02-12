from collections import deque
from heapq import heappop, heappush

n = int(input()) # n x n 크기의 공간
space = [list(map(int, input().split())) for _ in range(n)]
index = [(i, j) for i in range(n) for j in range(n) if space[i][j] == 9]
x, y = index[0]
space[x][y] = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
count = 0
move = 0
size = 2

def bfs(bx, by):
    q = deque()
    q.append((bx, by))
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    visited[bx][by] = True
    target = [] # 우선순위별로 정렬된 물고기
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if space[nx][ny] <= size:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[x][y] + 1 # 아기 상어로부터 물고기 까지의 거리
                        if 0 < space[nx][ny] < size:
                            heappush(target, (distance[nx][ny], nx, ny))
    if target:
        return target[0] # 최소힙 특성상 거리가 가까운 것이 가장 앞쪽에 위치함 거리가 같다면 x좌표가 작은(위쪽에 위치한) 것이, x좌표가 같다면 y좌표가 작은(왼쪽에 위치한) 것이 맨 앞에 위치함
    else:
        return False

while True:
    result = bfs(x, y)
    
    if not result:
        print(move)
        break
    else:
        dist, nx, ny = result
    
    move += dist
    
    count += 1
    if size == count:
        size += 1
        count = 0
    
    space[nx][ny] = 0
    x, y = nx, ny