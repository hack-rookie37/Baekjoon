import sys

n, m, b = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, world))
min_height = min(map(min, world))
total_dirt = sum(map(sum, world)) + b
answer = [float('inf'), float('inf')]

for height in range(min_height, max_height + 1):
    if total_dirt < n * m * height:
        break

    temp = 0

    for y in range(n):
        for x in range(m):
            if world[y][x] < height:
                temp += height - world[y][x]
                continue

            temp += (world[y][x] - height) * 2

    answer = min(answer, [temp, height], key=lambda a: [a[0], -a[1]])

print(*answer)