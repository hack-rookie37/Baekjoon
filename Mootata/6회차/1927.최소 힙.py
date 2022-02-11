import heapq
import sys

n = int(sys.stdin.readline()) # 연산의 개수 n
minh = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if minh:
            print(heapq.heappop(minh))
        else:
            print('0')
    else:
        heapq.heappush(minh, x)