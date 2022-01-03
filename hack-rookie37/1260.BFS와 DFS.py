from sys import stdin
from collections import deque, defaultdict

input = stdin.readline


def dfs(graph, s):
    stack = [s]
    visit = []

    while stack:
        p = stack.pop()
        if p not in visit:
            visit.append(p)
            stack.extend(reversed(graph[p]))

    for i in visit:
        print(i, end=' ')


def bfs(graph, s):
    queue = deque([s])
    visit = []
    while queue:
        p = queue.popleft()
        if p not in visit:
            visit.append(p)
            queue.extend(graph[p])

    for i in visit:
        print(i, end=' ')


def duplicate(t):
    return (t[1], t[0])


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # bidirectional edges
    edges = edges + list(map(duplicate, edges))
    edges = list(set(edges))
    edges.sort()

    graph = defaultdict(list)
    for e in edges:
        if e[0] not in graph:
            graph[e[0]]
        graph[e[0]].append(e[1])

    dfs(graph, V)
    print()
    bfs(graph, V)
