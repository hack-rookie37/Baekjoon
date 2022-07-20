import sys

input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        return find(parents[x])
    return x


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parents[b] = parents[pb] = pa
    else:
        parents[a] = parents[pa] = pb


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

parents = [i for i in range(N + 1)]
max_edge = edge_count = answer = 0

for a, b, edge in edges:

    if edge_count > N - 1:
        break

    if find(a) != find(b):
        union(a, b)
        answer += edge
        edge_count += 1
        max_edge = max(max_edge, edge)

print(answer - max_edge)
