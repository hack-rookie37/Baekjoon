import sys

input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 동 서 북 남

n, m, x, y, k = map(int, input().split()) # 지도의 크기 N x M, 주사위의 위치 (X, Y), 명령의 수 K

maps = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 윗면 북 동 서 남 바닥면

for i in command:
    dir = i - 1 # dx, dy 인덱스가 0 ~ 3이라 1 뺴줌
    nx, ny  = x + dx[dir], y + dy[dir]
    
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    
    if dir == 0: # 주사위가 오른쪽으로 구를 때, 북, 남의 값은 변하지 않음
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: # 주사위가 왼쪽으로 구를 때, 북, 남의 값은 변하지 않음
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2: # 주사위가 위쪽으로 구를 때, 동, 서의 값은 변하지 않음
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else: # 주사위가 아래쪽으로 구를 때, 동, 서의 값은 변하지 않음
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if maps[nx][ny] == 0: # 주사위 아래 지도의 값이 0
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0
    
    x, y = nx, ny
    
    print(dice[0])