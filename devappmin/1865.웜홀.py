from collections import defaultdict
import sys
input = sys.stdin.readline

test_case = int(input())

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

def solution():
    n, m, w = map(int, input().split())
    world = defaultdict(list)
    dist = {node: 10001 for node in range(1, n + 1)}

    # Append matrix values into world dictionary
    for _ in range(m):
        s, e, t = map(int, input().split())
        world[s].append((e, t))
        world[e].append((s, t))
    
    # Append wormhole values into world dictionary
    for _ in range(w):
        s, e, t = map(int, input().split())
        world[s].append((e, -t))
    
    print("NO" if not bellman_ford(world, dist, 1, n) else "YES")


for _ in range(test_case):
    solution()