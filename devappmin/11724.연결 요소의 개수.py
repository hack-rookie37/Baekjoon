import sys
from collections import defaultdict
from collections import deque

n, m = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
matrix = defaultdict(list)

q = deque([x for x in range(1, n + 1)])
qq = deque()

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u].append(v)
    matrix[v].append(u)

ans = 0

while(q):
    if(not qq):
        front = q.popleft()
        
        if visited[front]:
            continue
        qq.append(front)
        ans += 1
        visited[front] = True
        
    for item in matrix[qq.popleft()]:
        if not visited[item]:
            qq.append(item)
            visited[item] = True

print(ans)