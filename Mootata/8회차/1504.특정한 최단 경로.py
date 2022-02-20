import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, e = map(int, input().split()) # 정점의 개수 n, 간선의 개수 e
INF = float('inf')
roads = [[] for _ in range(n + 1)]

for i in range(1, e + 1):
    v1, v2, dist = map(int, input().split())
    roads[v1].append((dist, v2))
    roads[v2].append((dist, v1))

v1, v2 = map(int, input().split()) # 중간에 거쳐야 하는 두개의 서로 다른 정점 v1, v2

def dijkstra(k):
    weights = [INF] * (n + 1) # 시작 정점에서 각 정점까지의 거리
    q = []
    heappush(q, (0, k))
    weights[k] = 0
    
    while q:
        weight, v = heappop(q)
        
        if weights[v] < weight: # 기록되어 있는 거리보다 멀다면 넘어감
            continue
        
        for w, node in roads[v]:
            next_weight = weight + w
            if weights[node] > next_weight:
                heappush(q, (next_weight, node))
                weights[node] = next_weight
    return weights # 시작 정점에서 n까지의 거리를 모두 구했다면 return

start_1 = dijkstra(1) # 1에서 n으로 가는 최단거리
start_v1 = dijkstra(v1) # v1에서 n으로 가는 최단거리
start_v2 = dijkstra(v2)# v2에서 n으로 가는 최단거리

answer = min(start_1[v1] + start_v1[v2] + start_v2[n], start_1[v2] + start_v2[v1] + start_v1[n]) # 1 -> v1 -> v2 -> n 과 1 -> v2 -> v1 -> n 둘중 더 작은 것을 answer에 넣음

if answer == INF:
    print(-1)
else:
    print(answer)

# 1에서 n으로 갈 때 중간에 두 정점 v1, v2를 거치는 경우는 다음 두가지 경우임
# 1 -> v1 -> v2 -> n 또는 1 -> v2 -> v1 -> n
# 두가지 경우의 거리를 구해야 하는데, 이는 (1 -> v1) + (v1 -> v2) + (v2 -> n) 이런식으로
# 1에서 출발해서 v1까지의 거리와 v1에서 출발해서 v2까지의 거리 마지막으로 v2에서 출발해서 n까지 가는 거리를 모두 더한 값임