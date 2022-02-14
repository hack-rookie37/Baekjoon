import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline()) # 연산의 개수 n
abs_h = []

for i in range(n):
    x = int(sys.stdin.readline()) # 연산의 정보 x
    
    if x != 0:
        heappush(abs_h, (abs(x), x))
    else:
        if abs_h:
            print(abs_h[0][1])
            heappop(abs_h)
        else:
            print(0)