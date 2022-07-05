import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [[0, n] for _ in range(100001)]
visited[n] = [1, -1]
q = deque([n])

while q:
    cur = q.popleft()

    if visited[k][0]:
        break
    
    for pos in (1, -1, cur):
        n_cur = cur + pos

        if not (0 <= n_cur < 100001):
            continue

        if visited[n_cur][0]:
            continue

        visited[n_cur][0] = visited[cur][0] + 1
        visited[n_cur][1] = cur
        q.append(n_cur)


arr = [k]
pos = k
while visited[pos][1] != -1:
    arr.append(visited[pos][1])
    pos = visited[pos][1]

print(visited[k][0] - 1)
print(*arr[::-1])