import sys

v, e = map(int, sys.stdin.readline().split())
parent = [x for x in range(v + 1)]
rank = [0] * (v + 1)
edges = []

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

def find(a):
    if parent[a] == a:
        return a
    
    t = find(parent[a])
    parent[a] = t

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

    for edge in edges:
        if not edge:
            continue

        w, a, b = edge

        if find(a) != find(b):
            union(a, b)
            total += w
    
    return total

print(kruskal(edges))