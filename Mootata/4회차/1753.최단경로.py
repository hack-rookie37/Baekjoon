from heapq import heappush, heappop

v, e = map(int, input().split()) # 정점의 개수, 간선의 개수
k = int(input()) # 시작 정점
INF = 11
graph = [[] for _ in range(v + 1)]
weights = [INF for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, input().split()) # 정점 u에서 v로 향하는 가중치 w의 간선 
    graph[u].append((v, w))
    
def dijkstra(k):
    queue = []
    weights[k] = 0 # 자기 자신으로 가는 값은 0
    heappush(queue, [0, k])
    
    while queue:
        weight, node = heappop(queue)
        
        if weights[node] < weight: # 가중치가 더 높다면 무시
            continue
        for i in graph[node]:
            next_w = weight + i[1]
            
            if next_w < weights[i[0]]: # 비용이 더 적다면
                weights[i[0]] = next_w
                heappush(queue, (next_w, i[0]))
                
dijkstra(k)

for i in weights[1:]:
    print(i if i != INF else "INF")
