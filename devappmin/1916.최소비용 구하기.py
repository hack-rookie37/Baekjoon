import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
matrix = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a].append((b, c))

def dijkstra(matrix, start, end):
    dists = {node: INF for node in range(1, n + 1)}
    dists[start] = 0

    pq = []

    heappush(pq, (dists[start], start))

    while pq:
        c_dist, c_next = heappop(pq)

        if dists[c_next] < c_dist:
            continue

        for n_node, n_dist in matrix[c_next]:
            dist = c_dist + n_dist

            if dist < dists[n_node]:
                dists[n_node] = dist
                heappush(pq, (dist, n_node))
    
    
    return dists[end]

print(dijkstra(matrix, *list(map(int, input().split()))))