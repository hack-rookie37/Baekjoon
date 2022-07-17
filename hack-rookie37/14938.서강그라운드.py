from sys import stdin

input = stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

maxItem = 0
for g in graph:
    tmp = 0
    for i in range(1, n + 1):
        if g[i] <= m:
            tmp += items[i - 1]
    maxItem = max(maxItem, tmp)

print(maxItem)
