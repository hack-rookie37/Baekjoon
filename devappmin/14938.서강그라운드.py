import sys

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for idx in range(n + 1):
    graph[idx][idx] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for path in graph:
    price = sum([items[x - 1] for x in range(1, n + 1) if path[x] <= m])
    answer = max(answer, price)

print(answer)