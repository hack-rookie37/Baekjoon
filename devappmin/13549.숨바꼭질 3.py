import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100002
visited[n] = 0
q = deque([n])

while q:
    pos = q.popleft()

    if pos == k:
        print(visited[pos])
        break

    for idx in (pos * 2, pos + 1, pos - 1):
        if 0 <= idx < 100001 and visited[idx] == -1:
            visited[idx] = visited[pos] + (1 if idx != pos * 2 else 0)
            q.append(idx) if idx != pos * 2 else q.appendleft(idx)