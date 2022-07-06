import sys
from collections import defaultdict
from heapq import heappop, heappush

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(m):
    fr, to, weight = map(int, sys.stdin.readline().split())
    graph[fr].append((to, weight))

def dijkstra(graph, start, destination):
    dists = {node: float('inf') for node in range(1, n + 1)}
    dists[start] = 0

    path = {node: float('inf') for node in range(1, n + 1)}
    path[start] = 0

    q = []

    heappush(q, (dists[start], start))

    while q:
        c_distance, c_destination = heappop(q)

        if dists[c_destination] < c_distance:
            continue

        for n_destination, n_distance in graph[c_destination]:
            dist = c_distance + n_distance

            if dist < dists[n_destination]:
                dists[n_destination] = dist
                path[n_destination] = c_destination
                heappush(q, (dist, n_destination))
    
    path_list = [destination]
    p = path[destination]
    while p:
        path_list.append(p)
        p = path[p]

    return dists[destination], path_list

start, destination = map(int, sys.stdin.readline().split())
shortest, path = dijkstra(graph, start, destination)
print(shortest)
print(len(path))
print(*path[::-1])