import sys
input = sys.stdin.readline

dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]

n = int(input())

dragons = [list(map(int, input().split())) for _ in range(n)]

worlds = [[0] * 101 for _ in range(101)]

def dragon_curve(x, y, d, g):
    global worlds

    directs = [d]
    worlds[y][x] += 1

    for gen in range(g):
        directs.extend([(x + 1) % 4 for x in directs][::-1])
    
    for direct in directs:
        y, x = y + dy[direct], x + dx[direct]

        if not (0 <= y <= 101 and 0 <= x <= 101):
            continue

        worlds[y][x] += 1

for x, y, d, g in dragons:
    dragon_curve(x, y, d, g)

ans = 0
for y_idx in range(100):
    for x_idx in range(100):
        if  worlds[y_idx][x_idx] and worlds[y_idx + 1][x_idx] and \
            worlds[y_idx][x_idx + 1] and worlds[y_idx + 1][x_idx + 1]:
                ans += 1

print(ans)

# 0 
# 0 1
# 0 1 2 1
# 0 1 2 1 2 3 2 1
# 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1