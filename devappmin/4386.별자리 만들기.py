import sys
from math import sqrt
from itertools import combinations
from collections import defaultdict

n = int(sys.stdin.readline())
ranks = defaultdict(int)
parents = defaultdict(set)
positions = []
edges = []

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    positions.append((y, x))
    parents[(y, x)] = (y, x)
    ranks[(y, x)] = 0

for star1, star2 in combinations(positions, 2):
    s1y, s1x = star1
    s2y, s2x = star2

    weight = sqrt(abs(s2y - s1y) ** 2 + abs(s2x - s1x) ** 2)
    edges.append((weight, star1, star2))

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

    total = 0

    for edge in edges:
        if not edge:
            continue

        w, s1, s2 = edge
        
        if find(s1) != find(s2):
            union(s1, s2)
            total += w
    
    return total

print("{:.2f}".format(kruskal(edges)))