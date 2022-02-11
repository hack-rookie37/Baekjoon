import sys
import heapq

n = int(sys.stdin.readline()) # 연산의 개수 n
maxh = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(maxh, -1 * x)
    else:
        if maxh:
            print(-1 * heapq.heappop(maxh))
        else:
            print('0')