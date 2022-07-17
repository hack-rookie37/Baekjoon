import sys

# 북 남 동 서
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [0, 2], [1, 3], [1, 2]],
    [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cctvs = []
answer = float('inf')

for y in range(n):
    for x in range(m):
        if 0 < graph[y][x] <= 5:
            cctvs.append((graph[y][x], y, x))

def action(graph, mode, y, x):
    for md in mode:
        ny, nx = y, x

        while True:
            ny += dy[md]
            nx += dx[md]

            if not (0 <= ny < n and 0 <= nx < m):
                break

            if graph[ny][nx] == 6:
                break

            if not graph[ny][nx]:
                graph[ny][nx] = 7

def dfs(depth, graph):
    global answer

    if depth == len(cctvs):
        count = 0
        for idx in range(n):
            count += graph[idx].count(0)

        answer = min(answer, count)
        return
    
    temp = [row[:] for row in graph]

    cctv_value, y, x = cctvs[depth]

    for mode in modes[cctv_value]:
        action(temp, mode, y, x)
        dfs(depth + 1, temp)
        temp = [row[:] for row in graph]

dfs(0, graph)
print(answer)