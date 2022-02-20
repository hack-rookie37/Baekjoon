import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
know = list(map(int, sys.stdin.readline().split()))[1:]
party = {} 
matrix = defaultdict(list)

q = deque(know)

for idx in range(m):
    val = list(map(int, sys.stdin.readline().split()))
    party[idx] = val[1:]

    for i in party[idx]:
        matrix[i].extend(val[1:])

while q:
    person = q.pop()

    for pp in matrix[person]:
        if pp not in know:
            know.append(pp)
            q.append(pp)

ans = m
for _, v in party.items():
    for pp in know:
        if pp in v:
            ans -= 1
            break

print(ans)