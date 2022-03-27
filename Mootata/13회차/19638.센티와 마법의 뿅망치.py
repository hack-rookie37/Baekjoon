import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, h, t = map(int, input().split()) # 인구수 n, 센티의 키 h, 뿅망치 횟수 제한 t
heights = []
count = 0

for i in range(n):
    heappush(heights, (-(int(input()))))

while True:
    if -heights[0] < h: # 가장 큰 키를 가진 거인보다 센티가 클 때
        print('YES')
        print(count)
        break
    elif t == 0: # 뿅망치 횟수 제한을 모두 소모했는데도, 위의 if문에 걸리지 않았으므로 실패
        print('NO')
        print(-heappop(heights))
        break
    elif -heights[0] == 1: # 가장 큰 거인의 키가 1인데도 맨 위의 if문에 걸리지 않았으므로, 센티의 키도 1이라는 뜻
        print('NO')
        print(-heappop(heights))
        break
    else:
        height = (-heappop(heights)) // 2
        heappush(heights, -height) # 거인의 키를 절반으로 낮추어 다시 우선순위 큐에 넣음
        t -= 1
        count += 1

