from sys import stdin
import heapq

input = stdin.readline
INF = float("inf")


def dijkstra(V, E, K):
    d = [INF] * (V + 1)
    d[K] = 0
    queue = []
    heapq.heappush(queue, (d[K], K))

    while queue:
        cur_distance, cur_destination = heapq.heappop(queue)

        if d[cur_destination] < cur_distance:
            continue

        for new_destination, new_distance in graph[cur_destination].items():
            distance = cur_distance + new_distance
            if distance < d[new_destination]:
                d[new_destination] = distance
                heapq.heappush(queue, (distance, new_destination))
    return d


# V <= 2*10^4, E <= 3*10^5
V, E = map(int, input().split())
K = int(input())  # start Vertex
graph = [dict() for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u] and graph[u][v] < w:
        continue
    graph[u][v] = w

# print(*dijkstra(V,E,K), sep='\n')
result = dijkstra(V, E, K)
for i in range(1, len(result)):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
