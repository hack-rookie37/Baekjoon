import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [x for x in range(n + 1)]
rank = [0] * (n + 1)
edges = [[] for _ in range(m + 1)]

for idx in range(1, m + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[idx].extend([c, a, b])

def find(a):
    if parent[a] == a:
        return a

    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
        return

    parent[a] = b

    if rank[a] == rank[b]:
        rank[b] += 1

def kruskal(edges):
    edges = sorted(edges)
    total = 0
    minimum_spanning_tree = []

    for edge in edges:
        if not edge:
            continue

        cost, fr, to = edge

        if find(fr) != find(to):
            union(fr, to)
            total += cost
            minimum_spanning_tree.append((fr, to))
    
    return total, minimum_spanning_tree

total, minimum_spanning_tree = kruskal(edges)
print(total)