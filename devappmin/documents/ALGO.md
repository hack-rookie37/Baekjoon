# Algorithm

## LCS

문자열 크기의 2D Array를 선언한 후, 첫 행은 0으로 삽입.

    만약, 비교하는 위치의 문자가 서로 같으면
        현재 위치의 값 = 왼쪽 대각선 값 + 1  (배열 범위를 벗어났으면 0이라고 가정)
    다르다면
        현재 위치의 값 = MAX{왼쪽 값, 위쪽 값}

## LIS

LIS는 가장 긴 증가하는 부분 수열 길이를 구하는 방법이다.

주어진 값은 대부분 숫자로 이루어진 배열이고 해당 배열 내에서 증가하는 수열 중 가장 큰 수열의 길이를 구하는 문제이다.

### Case 1

```python
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[j] = max(dp[i], dp[j] + 1)

print(max(dp))
```

### Case 2

```python
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
```

> 중가하는 가장 큰 수열의 길이를 구하는 것이지, 모든 수열의 경우를 출력하는 것이 아님을 유의하자.

## 트리의 지름 구하기

트리의 지름을 구하기 위해서는 무작위 정점을 하나 고르고 그 정점에서 가장 먼 정점을 구한 뒤에 그 정점과 그 정점에서 가장 먼 정점의 거리를 구하면 된다.

    1. 임의의 정점으로 부터 가장 먼 정점을 구한다.
    2. 1에서 나온 정점으로 부터 가장 먼 정점을 구한다.
    3. 1과 2에서 나온 정점간의 거리가 트리의 지름!

    이 말은 즉슨,

    1. 트리에서 임의의 정점 x를 잡는다.
    2. 정점 x에서 가장 먼 정점 y를 찾는다.
    3. 정점 y에서 가장 먼 정점 z를 찾는다.

## Priority Queue Dijkstra

```python
def dijkstra(graph, start, fin):

    # 시작점을 제외한 모든 거리를 무한대로 저장
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    q = []

    # heapq로 (거리, 노드)로 입력
    heappush(q, [dist[start], start])

    while q:
        c_dist, c_dest = heappop(q)

        if dist[c_dest] < c_dist:
            continue

        for n_dest, n_dist in graph[c_dest]:
            d = c_dist + n_dist
            if d < dist[n_dest]:
                dist[n_dest] = d
                heappush(q, [d, n_dest])

    return dist[fin]
```

`dist`에는 start 노드에서 각 노드까지 최단경로가 저장이 되는 곳이다.

여기에는 자기 자신은 0으로 나머지는 전부 무한대로 생각을 하고 값을 저장한다.

그 이후에는 `priority_queue`를 생성하고 (출발 지점까지 거리(0), 출발 지점 노드)를 넣는다.

이후 큐에서 반복하여 값을 빼오면서 `dist[큐에서 뺀 노드]`의 값이 `큐에서 뺀 거리`의 값보다 클 경우에,

해당 지점까지의 최단경로를 찾고 존재하면 dist에 넣어준 뒤 큐에다가 삽입한다.

## Bellman-Ford

```python
def bellman_ford(world, dist, start, n):
    dist[start] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for next_node, weight in world[j]:
                if dist[next_node] > dist[j] + weight:
                    dist[next_node] = dist[j] + weight
                    if i == n:
                        return True
    return False
```

`graph`와 `dist`을 구하는 방식은 다익스트라와 동일.

하지만 전체를 돌면서 체크를 하는 부분이 다르다.

## Floyd-Warshall

모든 노드에서 모든 노드로 가는 정보를 저장하기 위해서는 플로이드를 써야한다. 다익스트라나 벨만처럼 dictionary + priority queue를 사용하는 것이 아니라 이차원 배열을 만든 뒤에 최단 경로를 탐색하면 된다.

> 관련 문제: 14938, 11404

```python
graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for idx in range(n + 1):
    graph[idx][idx] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

```

## Minimum Spanning Tree (Kruskal)

`union-find`을 활용하여 최단 거리를 탐색할 수 있다.

> 관련 문제: 1922

```python
import sys

n = int(sys.stdin.readline()) # 노드의 개수
m = int(sys.stdin.readline()) # 간선의 수

parent = [x for x in range(n + 1)] # 루트 노드 정보를 저장하기 위한 배열
rank = [0] * (n + 1) # 정점의 rank를 저장하기 위한 배열
edges = [[] for _ in range(m + 1)] # 간선 정보를 저장하기 위한 배열

# edge 배열(간선 정보)에 (간선 비용, 출발 노드, 도착 노드)로 값을 저장한다.
for idx in range(1, m + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[idx].extend([c, a, b])

# Union-find 알고리즘

# find 알고리즘
def find(a):
    if parent[a] == a:
        return a

    # 루트 노드를 찾고 루트 노드의 정보를 갱신
    p = find(parent[a])
    parent[a] = p
    return parent[a]

# union 알고리즘
def union(a, b):
    # 두 노드의 루트 노드를 탐색
    a = find(a)
    b = find(b)

    # 루트 노드가 같으면 이어져 있는 것이므로 알고리즘을 더 이상 실행하지 않음
    if a == b:
        return

    # a의 루트 노드의 rank가 높으면 a에 b를 병합
    if rank[a] > rank[b]:
        parent[b] = a
        return

    # b의 루트 노드의 rank가 높거나 둘이 rank가 같으면 b에 a를 병합
    parent[a] = b

    # 두 노드의 rank가 같으면 b의 rank를 1 올림
    if rank[a] == rank[b]:
        rank[b] += 1

# 크루스칼 알고리즘
def kruskal(edges):
    # edge 정보를 비용, from, to 순서대로 정렬
    edges = sorted(edges)

    # 총 비용
    total = 0

    # mst의 edge가 저장될 배열
    minimum_spanning_tree = []

    # 모든 edge 정보를 탐색하며
    for edge in edges:
        # 그 edge가 비어있으면 다음으로 넘어간다
        if not edge:
            continue

        cost, fr, to = edge

        # 두 노드의 부모가 같지 않으면
        if find(fr) != find(to):
            # 두 노드를 연결한다.
            union(fr, to)

            # 또한 총 비용을 cost만큼 추가하고
            total += cost

            # edge 정보 배열에 정보를 추가한다
            minimum_spanning_tree.append((fr, to))
    
    # 그 값을 리턴
    return total, minimum_spanning_tree

total, minimum_spanning_tree = kruskal(edges)
print(total)
```

## 다각형의 면적 구하기

다각형의 면적은 일명 [`신발끈 정리`](https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B)를 활용하면 된다.

> 관련 문제: 2166