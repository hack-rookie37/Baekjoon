from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

r, c, t = map(int, input().split()) # R x C 크기의 방, t초 후의 상황
room = [list(map(int, input().split())) for _ in range(r)]
s = deque()
p = []

for i in range(r):
    if room[i][0] == -1:
        p.append((i, 0))

def spread():
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                s.append((i, j))
    while s:
        x, y = s.popleft()
        if room[x][y] < 5: # 크기가 5보다 작으면 어차피 확산안됨
            continue
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c or room[nx][ny] == -1:
                continue
            
            temp[nx][ny] += room[x][y] // 5
            count += 1
        room[x][y] = room[x][y] - (count * (room[x][y] // 5))
    for i in range(r): # 확산된 먼지가 확산되기 전의 먼지와 더해져서 중복으로 확산되는 것을 방지
        room[i] = [x + y for x, y in zip(room[i], temp[i])]
    return room

def move():
    flag = True
    for px, py in p:
        x, y = px, 1
        temp = 0
        
        if flag: # 위쪽
            flag = False
            for i in [3, 0, 2, 1]:
                while True:
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        break
                    room[x][y], temp = temp, room[x][y]
                    x, y = nx, ny
                    if x == px and y == py: # 공기청정기의 위치
                        break
        else: # 아래쪽
            for i in [3, 1, 2, 0]:
                while True:
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        break
                    room[x][y], temp = temp, room[x][y]
                    x, y = nx, ny
                    if x == px and y == py: # 공기청정기의 위치
                        break

for _ in range(t):
    spread()
    move()

answer = 0
for i in range(r):
    answer += sum(room[i])
print(answer + 2)