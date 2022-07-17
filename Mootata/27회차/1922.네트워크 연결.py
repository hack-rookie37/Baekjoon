from heapq import heappop, heappush

n = int(input())
m = int(input())
network = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split()) # 정점 a에서 b로 가는 비용이 c
    network[a - 1].append((c, b - 1))
    network[b - 1].append((c, a - 1))

def bfs():
    q = []
    heappush(q, (0, 0))
    answer = 0
    
    while q:
        weight, node = heappop(q)
        
        if not visited[node]:
            visited[node] = True
            answer += weight
            
            for next_node in network[node]:
                heappush(q, (next_node[0], next_node[1]))
    
    return answer

print(bfs())