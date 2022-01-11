from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

queue = deque([(0, 0, 1)])

# 0: r, 1: d, 2: l, 3: u
DX = (1, 0, -1, 0)
DY = (0, 1, 0, -1)

while queue and maze[N - 1][M - 1] != 0:
    i, j, count = queue.popleft()
    if maze[i][j] == 0:
        continue
    maze[i][j] = 0
    for k in range(4):
        x, y = j + DX[k], i + DY[k]
        if 0 <= x < M and 0 <= y < N:
            if maze[y][x] == 1:
                queue.append((y, x, count + 1))

print(count)
