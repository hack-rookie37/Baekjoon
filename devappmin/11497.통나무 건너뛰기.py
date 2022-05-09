import sys
from heapq import heappop, heapify

def solution():
    n = int(sys.stdin.readline())
    l = [-x for x in list(map(int, sys.stdin.readline().split()))]
    length = len(l)
    greedy = []

    heapify(l)

    while l:
        greedy.append(-heappop(l))

        if l:
            greedy.insert(0, -heappop(l))

    ans = abs(greedy[0] - greedy[-1])

    for i in range(length - 1):
        ans = max(ans, abs(greedy[i] - greedy[i + 1]))

    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solution()