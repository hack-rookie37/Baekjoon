import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
duck_graph = [[False] * c for _ in range(r)]

dq, wq = deque(), deque()
tdq, twq = deque(), deque()

temp_duck = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            if temp_duck == 0:
                dq.append((i, j))
                duck_graph[i][j] = 'L'
                temp_duck += 1
            else:
                duck_graph[i][j] = 'P'
                dq.append((i, j))
            wq.append((i, j))
            graph[i][j] = 0

        elif graph[i][j] == '.':
            wq.append((i, j))
            graph[i][j] = 0

def water_spread():
    while wq:
        y, x = wq.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not(0 <= ny < r and 0 <= nx < c):
                continue

            if graph[ny][nx] != 'X':
                continue

            graph[ny][nx] = graph[y][x] + 1
            twq.append((ny, nx))

def duck_spread():
    while dq:
        y, x = dq.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not(0 <= ny < r and 0 <= nx < c):
                continue
            
            if  ((duck_graph[ny][nx] == 'L' and duck_graph[y][x] == 'P') or
                (duck_graph[ny][nx] == 'P' and duck_graph[y][x] == 'L')):
                return True

            if duck_graph[ny][nx] != False:
                continue

            if type(graph[ny][nx]) == int:
                duck_graph[ny][nx] = duck_graph[y][x]
                dq.append((ny, nx))

                if graph[y][x] != graph[ny][nx]:
                    tdq.append((ny, nx))
            
    


ans = 0
while True:
    ans += 1
    water_spread()
    if duck_spread():
        break
    
    dq, wq = tdq, twq
    tdq, twq = deque(), deque()

print(ans)