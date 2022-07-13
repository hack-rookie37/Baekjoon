import sys, heapq
from collections import defaultdict

input = sys.stdin.readline


def find(parent, v):
    if v != parent[v]:
        return find(parent, parent[v])
    return v


def union(parent, v1, v2):
    pv1 = find(parent, v1)
    pv2 = find(parent, v2)

    if pv1 < pv2:
        parent[pv2] = pv1
    else:
        parent[pv1] = pv2


def kruskal(graph):
    graph.sort(key=lambda x: x[2])
    parent = [p for p in range(N + 1)]
    edge_cnt = answer = 0

    for v1, v2, e in graph:
        if edge_cnt > N - 1:
            break

        if find(parent, v1) != find(parent, v2):
            union(parent, v1, v2)
            edge_cnt += 1
            answer += e
    print(answer)


def prim(graph, start=1):
    g = defaultdict(list)
    for v1, v2, e in graph:
        g[v1].append((e, v2))
        g[v2].append((e, v1))

    answer = 0
    node_cnt = 1
    pq = g[start]
    heapq.heapify(pq)
    visited = {start}

    while pq:
        if node_cnt > N:
            break

        e, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            answer += e
            node_cnt += 1

            for e, u in g[v]:
                if u not in visited:
                    heapq.heappush(pq, (e, u))
    print(answer)


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = [list(map(int, input().split())) for _ in range(M)]

    kruskal(graph.copy())
    prim(graph.copy())
