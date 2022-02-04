from collections import deque

m, n, h = map(int, input().split()) # 상자의 가로 칸의 수 m, 상자의 세로 칸의 수 n, 쌓인 상자의 수 h
storage = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1] # 앞 뒤 좌 우 위 아래
answer = 0
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if storage[i][j][k] == 1:
                queue.append((j, k, i))

def bfs():
    while queue:
        x, y, z = queue.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and storage[nz][nx][ny] == 0:
                storage[nz][nx][ny] = storage[z][x][y] + 1
                queue.append((nx, ny, nz))

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if storage[i][j][k] == 0:
                print(-1)
                exit(0)
            
            answer = max(answer, storage[i][j][k])

print(answer - 1)