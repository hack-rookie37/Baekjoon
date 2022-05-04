import sys

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
dice = [0] * 7

n, m, y, x, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmds = list(map(int, sys.stdin.readline().split()))

for cmd in cmds:
    if not (0 <= y + dy[cmd] < n and 0 <= x + dx[cmd] < m):
        continue

    y, x = y + dy[cmd], x + dx[cmd]

    if cmd == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif cmd == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif cmd == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif cmd == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    
    if graph[y][x] != 0:
        dice[6] = graph[y][x]
        graph[y][x] = 0
    else:
        graph[y][x] = dice[6]
    
    print(dice[1])