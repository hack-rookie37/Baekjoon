import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
erase = int(sys.stdin.readline())

tree = defaultdict(list)
for idx, value in enumerate(nodes):
    if value == -1:
        root = idx
        continue

    if value == erase or idx == erase:
        continue

    tree[value].append(idx)

q = deque([root])
answer = 0

if erase == root:
    print(0)
    exit()

while q:
    node = q.popleft()
    
    if not tree[node]:
        answer += 1
        continue

    q.extend(tree[node])

print(answer)