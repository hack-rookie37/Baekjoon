import sys
from collections import deque
input = sys.stdin.readline

mx, my, mz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())

    if not l and not r and not c:
        break

    world = []
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    q = deque()

    for i in range(l):
        world.append([])

        for j in range(r):
            world[i].append(list(input().rstrip()))
            if 'S' in world[i][j]:
                k = world[i][j].index('S')
                q.append((i, j, k))
                visited[i][j][k] = 0
        input()
    
    ans = False
    
    while q and not ans:
        z, y, x = q.popleft()

        for idx in range(6):
            dz, dy, dx = z + mz[idx], y + my[idx], x + mx[idx]

            if dz < 0 or dy < 0 or dx < 0 or dz >= l or dy >= r or dx >= c:
                continue
            
            if world[dz][dy][dx] == '.' and visited[dz][dy][dx] == 0:
                visited[dz][dy][dx] = visited[z][y][x] + 1
                q.append((dz, dy, dx))
            
            if world[dz][dy][dx] == 'E':
                ans = True
                print('Escaped in', visited[z][y][x] + 1, "minute(s).")
                break

    if not ans:
        print('Trapped!')