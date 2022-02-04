from collections import deque

m, n = map(int, input().split()) # 상자의 가로 칸의 수 m, 상자의 세로 칸의 수 n
storage = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
queue = deque()

for i in range(n):
    for j in range(m):
        if storage[i][j] == 1: # 이미 익은 토마토부터 탐색을 시작하기 위해서 미리 큐에 담아줌
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and storage[nx][ny] == 0: # 범위 안에 있고, 익지 않은 토마토 일 때
                storage[nx][ny] = storage[x][y] + 1
                queue.append((nx, ny))
    return max(map(max, storage)) # 가장 큰 값을 찾아서 리턴

answer = bfs()

for i in range(n):
    for j in range(m):
        if storage[i][j] == 0: # 아직 익지 않은 토마토가 있다면
            print(-1)
            exit(0)
            
print(answer - 1) # 익은 토마토가 1부터 시작하므로 1을 빼줘야 함