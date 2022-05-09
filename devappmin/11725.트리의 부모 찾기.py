import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
dicts = defaultdict(list)
visited = [0] * (n + 1)
q = deque()
q.append(1)

for _ in range(n - 1):
    node_a, node_b = map(int, sys.stdin.readline().split())
    dicts[node_a].append(node_b)
    dicts[node_b].append(node_a)

while q:
    idx = q.popleft()
    for i in dicts[idx]:
        if not visited[i]:
            visited[i] = idx
            q.append(i)

print(*visited[2:], sep="\n")