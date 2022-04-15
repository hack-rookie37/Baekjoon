import sys

size_x, size_y = map(int, sys.stdin.readline().split())

sy, sx = [0, 0, size_y, 0, 0], [0, 0, 0, 0, size_x]
dy, dx = [0, 0, 0, 1, 1], [0, 1, 1, 0, 0]

shop_n = int(sys.stdin.readline())
shops = [(pos, sy[pos] + dy[pos] * mov, sx[pos] + dx[pos] * mov) for pos, mov in [tuple(map(int, sys.stdin.readline().split())) for _ in range(shop_n)]]
p = tuple(map(int, sys.stdin.readline().split()))
pos = (sy[p[0]] + dy[p[0]] * p[1], sx[p[0]] + dx[p[0]] * p[1])

answer = 0
for shop in shops:
    if  ((p[0] == 1 or p[0] == 4) and (shop[0] == 1 or shop[0] == 4)) or \
        ((p[0] == 2 or p[0] == 3) and (shop[0] == 2 or shop[0] == 3)):
        dist = abs(shop[1] + shop[2] - pos[0] - pos[1])
        answer += min(dist, ( size_x + size_y ) * 2 - dist)
    else:
        dist = shop[1] + shop[2] + pos[0] + pos[1]
        answer += min(dist, ( size_x + size_y ) * 2 - dist)

print(answer)