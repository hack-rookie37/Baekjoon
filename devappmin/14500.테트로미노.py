import sys

blocks = [
    [
        [1, 1, 1, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1],
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1],
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1],
    ],
    [
        [1, 1],
        [0, 1],
        [0, 1],
    ],
    [
        [1, 1],
        [1, 0],
        [1, 0]
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1],
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
    ],
    [
        [0, 0, 1],
        [1, 1, 1],
    ],
    [
        [1, 0, 0],
        [1, 1, 1],
    ],
    [
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
    ],
    [
        [0, 1],
        [1, 1],
        [0, 1],
    ],
    [
        [1, 0],
        [1, 1],
        [1, 0],
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1],
    ],
    [
        [0, 1],
        [1, 1],
        [1, 0],
    ],
    [
        [0, 1, 1],
        [1, 1, 0],
    ],
    [
        [1, 1, 0],
        [0, 1, 1],
    ],
]

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max = 0

for y in range(n):
    for x in range(m):
        for li in blocks:
            if len(li) > n - y or len(li[0]) > m - x:
                continue
            temp = 0

            for by in range(len(li)):
                for bx in range(len(li[0])):
                    temp += li[by][bx] * matrix[y + by][x + bx]

            if temp > max:
                max = temp

print(max)
