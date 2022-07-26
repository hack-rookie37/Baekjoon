from heapq import heappop, heappush

n, m = map(int, input().split())
roads = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    roads[a - 1].append((w, b - 1))
    roads[b - 1].append((w, a - 1))

def bfs():
    q = []
    heappush(q, (0, 0))
    answer = 0
    m_road = 0
    
    while q:
        weight, node = heappop(q)
        
        if not visited[node]:
            visited[node] = True
            answer += weight
            m_road = max(m_road, weight)
            
            for next_node in roads[node]:
                heappush(q, (next_node[0], next_node[1]))
    return answer - m_road

print(bfs())

# MST알고리즘을 통해서 최단거리를 구하고, 그 중에서도 가장 큰 비용의 길을 하나 지우면
# 도시가 두개로 나뉘면서 최소 비용을 구할 수 있음.