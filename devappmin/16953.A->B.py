import sys
from collections import deque, defaultdict

a, b = map(int, sys.stdin.readline().split())
visited = defaultdict(int)
q = deque()

visited[a] = 1
q.append(a)

for idx in range(b):
    if not q:
        break

    if visited[b]:
        break

    n = q.popleft()

    for next in (n * 2, n * 10 + 1):
        if not visited[next]:
            visited[next] = visited[n] + 1
            if next <= b:
                q.append(next)

print(-1 if not visited[b] else visited[b])
