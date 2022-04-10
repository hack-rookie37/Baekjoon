import sys

input = sys.stdin.readline
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 남 동 북 서 

_ = int(input())
text = list(input().strip())
dir = 0

maze = [['#' for _ in range(100)]  for _ in range(100)]
x, y = 50, 50
maze[x][y] = '.'

ltx, lty = 50, 50
rbx, rby = 50, 50

for t in text:
    if t == 'R':
        dir = (dir + 3) % 4 # F가 나왔을 때 이동할 방향을 오른쪽으로 90도 변경
    elif t == 'L':
        dir = (dir + 1) % 4 # F가 나왔을 때 이동할 방향을 왼쪽쪽으로 90도 변경
    else:
        x += dx[dir]
        y += dy[dir]
        ltx, lty = min(ltx, x), min (lty, y) # 출력할 부분 설정하기 위해서 가장 왼쪽위의 x, y 좌표와
        rbx, rby= max(rbx, x), max(rby, y) # 가장 오른쪽 아래의 x, y 좌표를 구함
        maze[x][y] = '.'

for i in range(ltx, rbx + 1):
    for j in range(lty, rby + 1):
        print(maze[i][j], end='')
    print()