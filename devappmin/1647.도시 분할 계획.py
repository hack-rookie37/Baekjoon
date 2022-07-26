import sys

n, m = map(int, sys.stdin.readline().split())
ranks = [0] * (n + 1)
parents = [x for x in range(n + 1)]
edges = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

def find(a):
    if parents[a] == a:
        return a
    
    t = find(parents[a])
    parents[a] = t

    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if ranks[a] > ranks[b]:
        parents[b] = a
        return
    
    parents[a] = b

    if ranks[a] == ranks[b]:
        ranks[b] += 1
    
def kruskal(edges):
    edges = sorted(edges)
    answer = 0
    max_value = 0
    for edge in edges:
        if not edge:
            continue

        weight, start, end = edge

        if find(start) != find(end):
            union(start, end)
            answer += weight
            max_value = max(max_value, weight)

    return answer - max_value

print(kruskal(edges))