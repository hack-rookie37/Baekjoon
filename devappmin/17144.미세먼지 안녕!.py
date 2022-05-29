import sys
from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

r, c, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
machine = []
dust = deque()

def air_purifier(pos, isTop):
    for y in range(pos + (-1 if isTop else 1), 0 if isTop else r - 1, -1 if isTop else 1):
        graph[y][0] = graph[y + (-1 if isTop else 1)][0]

    for x in range(c - 1):
        graph[0 if isTop else (r - 1)][x] = graph[0 if isTop else (r - 1)][x + 1]

    for y in range(0 if isTop else r - 1, pos, 1 if isTop else -1):
        graph[y][c - 1] = graph[y + (1 if isTop else -1)][c - 1]
    
    for x in range(c - 1, 0, -1):
        graph[pos][x] = graph[pos][x - 1]

    graph[pos][1] = 0

for y in range(r):
    for x in range(c):
        if graph[y][x] == -1:
            machine.append(y)
            continue

        if graph[y][x]:
            dust.append((y, x))

for i in range(t):
    spread = [[0] * c for _ in range(r)]

    while dust:
        y, x = dust.popleft()
        spread_value = graph[y][x] // 5

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < r and 0 <= nx < c):
                continue

            if graph[ny][nx] == -1:
                continue

            spread[ny][nx] += spread_value
            spread[y][x] -= spread_value

    for y in range(r):
        for x in range(c):
            graph[y][x] += spread[y][x]
    
    air_purifier(machine[0], True)
    air_purifier(machine[1], False)
    dust = deque([(y, x) for y in range(r) for x in range(c) if graph[y][x] > 0])

print(sum(map(sum, graph)) + 2)