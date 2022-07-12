from heapq import heappop, heappush

n = int(input())
m = int(input())
city = [[] for _ in range(n)]
weights = [float('inf') for _ in range(n)]

for i in range(m):
    c1, c2, w = map(int, input().split())
    city[c1 - 1].append((w, c2 - 1))

def bfs(s):
    q = []
    heappush(q, (0, s))
    weights[s] = 0
    
    while q:
        w, n = heappop(q)
        
        if weights[n] < w:
            continue
        
        for weight, node in city[n]:
            next_w = w + weight
            if next_w < weights[node]:
                weights[node] = next_w
                heappush(q, (next_w, node))

s, e = map(int, input().split())
bfs(s - 1)
print(weights[e - 1])