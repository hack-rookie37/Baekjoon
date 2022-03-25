import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, h, t = map(int, input().split()) # 인구수 n, 센티의 키 h, 뿅망치 횟수 제한 t
heights = []
count = 0

for i in range(n):
    heappush(heights, (-(int(input()))))

while True:
    if -heights[0] < h:
        print('YES')
        print(count)
        break
    elif t == 0:
        print('NO')
        print(-heappop(heights))
        break
    elif -heights[0] == 1:
        print('NO')
        print(-heappop(heights))
        break
    else:
        height = (-heappop(heights)) // 2
        heappush(heights, -height)
        t -= 1
        count += 1

