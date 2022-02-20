import sys
from collections import deque

input = sys.stdin.readline

v = int(input()) # 트리의 정점의 개수 v
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    links = list(map(int, input().split()))
    links.pop()
    for j in range(1, len(links), 2):
        graph[links[0]].append((links[j + 1], links[j]))

def bfs(k):
    q = deque()
    q.append((0, k))
    visited = [False] * (v + 1)
    visited[k] = True
    fardest = [0, 0]
    
    while q:
        w, n = q.popleft() # 현재까지 이동한 거리와, 노드번호
        
        for dist, node in graph[n]: # 다음에 이동할 노드까지의 거리, 노드번호
            if not visited[node]:
                visited[node] = True
                q.append((dist + w, node))
                if fardest[0] < dist + w: # 현재 가장 먼 거리보다 다음 노드까지 이동한 거리가 더 멀다면
                    fardest = dist + w, node # 업데이트 해줌
    return fardest

fardest_dist, fardest_node = bfs(1)

print(bfs(fardest_node)[0])

# 아무 노드에서 가장 먼 노드를 찾고, 그 노드에서 가장 먼 노드를 한번 더 찾으면
# 그 거리가 트리의 지름임