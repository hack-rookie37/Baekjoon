from collections import deque
from itertools import permutations

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

n = int(input()) # 복도의 크기 N x N
corr = [list(input().split()) for _ in range(n)] # 복도
temp = []
teacher = []

for i in range(n):
    for j in range(n):
        if corr[i][j] == 'X':
            temp.append((i, j))
        elif corr[i][j] == 'T':
            teacher.append((i, j))

permu = list(permutations(temp, 3)) # 비어있는 공간들 중 3곳을 뽑아 장애물 배치

def bfs():
    for per in permu:
        t = deque(teacher)
        flag = True
        while t:
            x, y = t.popleft()
            for i in range(4):
                nx, ny = x, y
                while True: # 상 하 좌 우를 끝까지 탐색
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    
                    if corr[nx][ny] == 'S': # 학생과 마주치면 실패
                        flag = False
                    if (nx, ny) in per: # 장애물을 만나면 탐색 중지
                        break
        if flag:
            return 'YES'
    return 'NO'

print(bfs())


# 장애물이 위치한 곳과 동일한 x, y선상은 무시해도 됨 