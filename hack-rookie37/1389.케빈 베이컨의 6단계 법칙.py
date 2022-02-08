from sys import stdin
from collections import deque, defaultdict

input = stdin.readline


def bfs(start):
    visited = [False] * (V + 1)
    visited[start] = True
    distance = [0] * (V + 1)
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for end in graph[vertex]:
            if not visited[end]:
                visited[end] = True
                queue.append(end)
                distance[end] = distance[vertex] + 1

    return sum(distance)


def bacon():
    bacons = [float("inf")] * (V + 1)

    for start in graph:
        bacons[start] = bfs(start)

    value = min(bacons)

    return bacons.index(value)


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(E):
        s, e = map(int, input().split())

        if e not in graph[s]:
            graph[s].append(e)
        if s not in graph[e]:
            graph[e].append(s)

    print(bacon())
