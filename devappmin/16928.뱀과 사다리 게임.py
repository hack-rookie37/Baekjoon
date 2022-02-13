import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
world = [x for x in range(101)]
dices = [x for x in range(1, 7)]
visited = [0 for _ in range(101)]

for i in range(n + m):
    x, y = map(int, sys.stdin.readline().split())
    world[x] = y

q = deque()
q.append(1)

def colonize(pos):
    for dice in dices:
        if pos + dice > 100:
            continue

        if not visited[world[pos + dice]]:
            visited[pos + dice] = visited[world[pos]] + 1
            visited[world[pos + dice]] = visited[pos + dice]
            q.append(world[pos + dice])

while visited[100] == 0:
    p = q.popleft()
    
    colonize(p)

print(visited[100])