import sys
from collections import defaultdict
from heapq import heappush, heappop

n, m, x = map(int, sys.stdin.readline().split())
vt = defaultdict(list)

for _ in range(m):
    fr, to, ti = map(int, sys.stdin.readline().split())
    vt[fr].append((to, ti))

def dijkstra(graph, start, fin):

    # 시작점을 제외한 모든 거리를 무한대로 저장
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    q = []

    # heapq로 (거리, 노드)로 입력
    heappush(q, [dist[start], start])

    while q:
        c_dist, c_dest = heappop(q)

        if dist[c_dest] < c_dist:
            continue
            
        for n_dest, n_dist in graph[c_dest]:
            d = c_dist + n_dist
            if d < dist[n_dest]:
                dist[n_dest] = d
                heappush(q, [d, n_dest])
    
    return dist[fin]

ans = 0
for idx in range(1, n + 1):
    if idx == x:
        continue

    ans = max(dijkstra(vt, idx, x) + dijkstra(vt, x, idx), ans)

print(ans)