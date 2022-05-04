import sys
from heapq import heappop, heappush

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

def bfs():
    pq = []
    heappush(pq, (-maps[0][0], (0, 0)))
    visited[0][0] = 1
    
    while pq:
        value, xy = heappop(pq)
        x, y = xy
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if maps[nx][ny] < maps[x][y]:
                if not visited[nx][ny]:
                    heappush(pq, (-maps[nx][ny], (nx, ny))) # 큰 값 먼저 방문
                visited[nx][ny] += visited[x][y]
    
    return visited[-1][-1]

print(bfs())

# 우선순위 큐를 사용해서 큰 값들부터 방문 하면서
# 차례대로 해당 좌표까지 도달할 수 있는 경로의 수를 계산함.