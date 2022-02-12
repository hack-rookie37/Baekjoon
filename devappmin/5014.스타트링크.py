import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
q = deque()

building = [0] * (f + 1)
building[s] = 1
q.append(s)

while q:
    p = q.popleft()

    for i in (u, -1 * d):
        pos = p + i

        if pos < 1 or pos > f:
            continue
            
        if not building[pos]:
            q.append(pos)
            building[pos] = building[p] + 1
        
    
    if building[g]:
        print(building[g] - 1)
        break

if not building[g]:
    print("use the stairs")