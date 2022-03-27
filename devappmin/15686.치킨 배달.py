import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chickens = []
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

dist = float("inf")
dists = [[0] * n for _ in range(n)]

for pos in combinations(chickens, m):
    dists = [[0] * n for _ in range(n)]
    for cy, cx in pos:
        for hy, hx in house:
            if dists[hy][hx] == 0:
                dists[hy][hx] = abs(hy - cy) + abs(hx - cx)
                continue
            dists[hy][hx] = min(dists[hy][hx], abs(hy - cy) + abs(hx - cx))
    
    dist = min(dist, sum(map(sum, dists)))

print(dist)