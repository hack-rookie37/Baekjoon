import sys
from collections import defaultdict
from heapq import heappush, heappop

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
matrix = defaultdict(list)

for _ in range(e):
    u, vv, w = map(int, sys.stdin.readline().split())
    matrix[u].append((vv, w))

def dijkstra(matrix, start):
    dists = {node : float('inf') for node in range(1, v + 1)}
    dists[start] = 0

    q = []

    heappush(q, (dists[start], start))

    while q:
        q_distance, q_destination = heappop(q)

        if dists[q_destination] < q_distance:
            continue

        for n_destination, n_distance in matrix[q_destination]:
            dist = dists[q_destination] + n_distance

            if dist < dists[n_destination]:
                dists[n_destination] = dist
                heappush(q, (dist, n_destination))
    
    for _, val in dists.items():
        print(val if val != float('inf') else 'INF')

dijkstra(matrix, k)
