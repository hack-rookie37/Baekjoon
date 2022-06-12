import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [0] * 100001
way = [0] * 100001
visited[n], way[n] = 1, 1

q = deque([n])

while q:
    pos = q.popleft()

    if visited[k] and visited[pos] > visited[k]:
        break

    for idx in (1, -1, pos):
        if not (0 <= pos + idx <= 100000):
            continue

        if not visited[pos + idx]:
            visited[pos + idx] = visited[pos] + 1
            way[pos + idx] = way[pos]
            q.append(pos + idx)
        elif visited[pos + idx] == visited[pos] + 1:
            way[pos + idx] += way[pos]

print(visited[k] - 1, way[k], sep='\n')