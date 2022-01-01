from collections import deque

N, M, V = map(int, input().split()) # 정점의 개수 N, 간선의 개수 M, 시작할 정점 V
graph = [[] for _ in range(N + 1)]

for i in range(M): #연결할 간선 입력
    m1, m2 = map(int, input().split())
    graph[m1].append(m2) # 각각의 자리에 연결된 정점을 입력
    graph[m2].append(m1)
    graph[m1].sort()
    graph[m2].sort()


visited = [False] * (N + 1) # 방문 유무

def dfs(graph, V, visited):
    visited[V] = True # 시작하는 정점은 방문했다고 표시
    print(V, end=' ')
    for i in graph[V]: # 시작하는 정점과 연결된 정점들을 하나씩 방문
        if not visited[i]: # 방문한 적이 없다면
            dfs(graph, i, visited) # 해당 정점으로 이동

def bfs(graph, V, visited):
    visited = [False] * (N + 1) # DFS에서 넣었던 값을 다시 False로 초기화 
    queue = deque([V]) # 정점 V를 큐에 넣음
    visited[V] = True # 시작하는 정점 방문 표시
    while queue: # queue에 값이 남아 있다면 반복
        pop = queue.popleft() # 큐의 가장 앞쪽 값을 꺼냄
        print(pop, end=' ')
        for i in graph[pop]: # 시작하는 정점 V와 연결된 정점들을 차례로 i에 넣음
            if not visited[i]: # 방문한 적이 없다면
                queue.append(i) # 큐에 해당 정점을 넣고
                visited[i] = True # 방문했다고 표시

dfs(graph, V, visited)
print()
bfs(graph, V, visited)