import sys
from collections import defaultdict
from heapq import heappush, heappop

n, e = map(int, sys.stdin.readline().split())
matrix = defaultdict(list)

for _ in range(e):
    f, t, d = map(int, sys.stdin.readline().split())
    matrix[f].append((t, d))
    matrix[t].append((f, d))

ma, mb = map(int, sys.stdin.readline().split())

def dijkstra(matrix, start, end):
    dists = {node: float('inf') for node in range(1, n + 1)}
    dists[start] = 0

    q = []

    heappush(q, (dists[start], start))

    while q:
        c_distance, c_destination = heappop(q)

        if c_distance > dists[c_destination]:
            continue

        for n_destination, n_distance in matrix[c_destination]:
            dist = dists[c_destination] + n_distance

            if dist < dists[n_destination]:
                dists[n_destination] = dist
                heappush(q, (dist, n_destination))
    
    return dists[end]

to_a = dijkstra(matrix, 1, ma)
to_b = dijkstra(matrix, 1, mb)
a_to_b = dijkstra(matrix, ma, mb)
a_to_d = dijkstra(matrix, ma, n)
b_to_d = dijkstra(matrix, mb, n)

ans =min(to_a + a_to_b + b_to_d, to_b + a_to_b + a_to_d) 
print(ans if ans != float('inf') else -1)