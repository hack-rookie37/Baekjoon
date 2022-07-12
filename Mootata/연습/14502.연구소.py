from collections import deque
from itertools import combinations

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
space = []
virus = []
vq = deque()
answer = 0
default = (n * m) - 3

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            space.append((i, j))
        elif lab[i][j] == 1:
            default -= 1
        else:
            virus.append((i, j))

default -= len(virus)

def spread(temp):
    count = 0
    while vq:
        x, y = vq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            
            if temp[nx][ny] == 0:
                visited[nx][ny] = True
                temp[nx][ny] = 2
                vq.append((nx, ny))
                count += 1
    return (default - count)

space_p = list(combinations(space, 3))

for i in space_p:
    w1, w2, w3 = i
    temp = []
    for j in lab[:]:
        temp.append(j[:])
    temp[w1[0]][w1[1]] = 1
    temp[w2[0]][w2[1]] = 1
    temp[w3[0]][w3[1]] = 1
    for j in virus:
        vq.append(j)
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = max(answer, spread(temp))

print(answer)