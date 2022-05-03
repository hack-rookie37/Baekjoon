import sys
from heapq import heappush, heappop

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, ay, ax = map(int, sys.stdin.readline().split())

# Get virus infos from the graph
virus = []
temp_virus = []
for y in range(n):
    for x in range(n):
        if graph[y][x]:
            heappush(virus, (graph[y][x], y, x))

for day in range(s):
    while virus:
        name, y, x = heappop(virus)

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < n and 0 <= nx < n):
                continue

            if graph[ny][nx]:
                continue

            graph[ny][nx] = name
            heappush(temp_virus, (name, ny, nx))
    
    virus.extend(temp_virus)
    temp_virus = []

print(graph[ay - 1][ax - 1])