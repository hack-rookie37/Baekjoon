import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline())

visited = [0] * (n + 1)
dicts = defaultdict(list)

q = deque([n])
dicts[n] = [n]

while q:
    pos = q.popleft()

    if pos == 1:
        print(visited[pos])
        print(*dicts[pos])
        break

    if pos % 3 == 0 and not visited[pos // 3]:
        visited[pos // 3] = visited[pos] + 1
        q.append(pos // 3)
        dicts[pos // 3] = dicts[pos][:] + [pos // 3]
    
    if pos % 2 == 0 and not visited[pos // 2]:
        visited[pos // 2] = visited[pos] + 1
        q.append(pos // 2)
        dicts[pos // 2] = dicts[pos][:] + [pos // 2]
    
    if not visited[pos - 1]:
        visited[pos - 1] = visited[pos] + 1
        q.append(pos - 1)
        dicts[pos - 1] = dicts[pos][:] + [pos - 1]