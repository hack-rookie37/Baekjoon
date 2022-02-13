import sys
from collections import deque

n, m = map(int, input().split()) # 정점의 개수 n, 간선의 개수 m
graph = [[0] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def bfs(k):
    queue = deque()
    queue.append(k)
    global count
    while queue:
        v = queue.popleft()
        if not visited[v]:
            for i in graph[v]:
                queue.append(i)
            visited[v] = True
    count += 1
            
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
    
print(count)