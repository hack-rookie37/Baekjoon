import sys
from heapq import heappop, heappush
from tracemalloc import start

input = sys.stdin.readline
INF = float('inf')

n, m, x = map(int, input().split()) # 학생의 수 n, 단방향 도로의 수 m, 파티가 열리는 마을의 번호 x
roads = [[] for _ in range(m + 1)]
answer = [0] * (n + 1)

for i in range(1, m + 1):
    v1, v2, w = map(int, input().split()) # 마을 v1에서 마을 v2로 가는 거리 w
    roads[v1].append((w, v2))

def dijkstra(k, is_start):
    weights = [INF for _ in range(n + 1)]
    weights[k] = 0
    q = []
    heappush(q, (0, k))
    
    while q:
        weight, v = heappop(q)
        
        if weights[v] < weight: # 기존 최단거리보다 멀다면 continue
            continue
        
        for w, node in roads[v]:
            next_weight = weight + w
            if weights[node] > next_weight:
                weights[node] = next_weight
                heappush(q, (next_weight, node))
    if is_start: # 각 마을에서 파티가 열리는 마을로 가는 거리를 구할 때
        return weights[x] # 출발한 마을에서 파티가 열리는 마을까지의 거리만 return
    else: # 파티가 끝나고 자신의 마을로 돌아가는 거리를 구할 때
        return weights # 파티가 열리는 마을 x로부터 다른 모든 마을들까지의 최단거리를 모두 return

way_home = dijkstra(x, False) # 파티가 끝나고 마을 x에서 다른 마을로 가는 최단거리

for i in range(1, n + 1):
    answer[i] = dijkstra(i, True) # i마을에서 파티가 열리는 x마을까지가는 최단거리
    answer[i] += way_home[i] # x마을에서 i마을로 가는 최단 거리
print(max(answer))

# 다익스트라 알고리즘으로 각 마을에서 파티가 열리는 마을로 가는 거리를 구하고
# 반대로 파티가 열리는 마을에서 각 마을로 가는 거리도 구한 뒤 둘을 더해줌