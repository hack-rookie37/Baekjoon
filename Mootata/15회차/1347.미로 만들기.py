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
        dir = (dir + 3) % 4
    elif t == 'L':
        dir = (dir + 1) % 4
    else:
        x += dx[dir]
        y += dy[dir]
        ltx, lty = min(ltx, x), min (lty, y)
        rbx, rby= max(rbx, x), max(rby, y)
        maze[x][y] = '.'

for i in range(ltx, rbx + 1):
    for j in range(lty, rby + 1):
        print(maze[i][j], end='')
    print()