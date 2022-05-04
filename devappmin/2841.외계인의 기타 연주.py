import sys
from collections import defaultdict, deque

n, p = map(int, sys.stdin.readline().split())
melodies = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dicts = defaultdict(deque)
ans = 0

for melody in melodies:
    if not dicts[melody[0]]:
        dicts[melody[0]].append(melody[1])
        ans += 1
        continue

    while dicts[melody[0]] and dicts[melody[0]][-1] > melody[1]:
        dicts[melody[0]].pop()
        ans += 1
    
    if dicts[melody[0]] and dicts[melody[0]][-1] == melody[1]:
        continue

    dicts[melody[0]].append(melody[1])
    ans += 1

print(ans)