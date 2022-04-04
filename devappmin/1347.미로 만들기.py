import sys

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

n = int(sys.stdin.readline())
commands = list(sys.stdin.readline().rstrip())
rotate = 0
position = [0, 0]

positions = []
positions.append(position)

for command in commands:
    if command == 'L':
        rotate = 0 if rotate == 3 else rotate + 1
    elif command == 'R':
        rotate = 3 if rotate == 0 else rotate - 1
    else:
        position = [position[0] + dy[rotate], position[1] + dx[rotate]]
        positions.append(position)

positions.sort()

ymin, xmin = 0, 0
ymax, xmax = 0, 0

for y, x in positions:
    ymin = min(y, ymin)
    xmin = min(x, xmin)

    ymax = max(y, ymax)
    xmax = max(x, xmax)

if ymin < 0:
    # due to the fact that ymin is always negative value
    ymax -= ymin
    
    temp = []

    for y, x in positions:
        temp.append([y - ymin, x])
    
    ymin = 0
    positions = temp

if xmin < 0:
    xmax -= xmin

    temp = []

    for y, x in positions:
        temp.append([y, x - xmin])
    
    xmin = 0
    positions = temp

maze = [['#'] * ( xmax + 1 ) for _ in range(ymax + 1)]
for y, x in positions:
    maze[y][x] = '.'

for row in maze:
    print(''.join(row))