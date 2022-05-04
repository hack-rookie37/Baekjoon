import sys
from heapq import heappush, heappop

n, h, t = map(int, sys.stdin.readline().split())
giants = []
count = 0
for _ in range(n):
    heappush(giants, -1 * int(sys.stdin.readline()))

for idx in range(1, t + 1):
    giant = -1 * heappop(giants)

    if h > giant or giant == 1: 
        heappush(giants, -1 * giant)
        break

    heappush(giants, -1 * (giant // 2))
    count += 1

giant = -1 * heappop(giants)
print(f"YES\n{count}" if h > giant else f"NO\n{giant}")