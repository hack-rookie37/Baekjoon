import sys

input = sys.stdin.readline

N, K = map(int, input().split())

lug = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
d = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = lug[i][0]
        v = lug[i][1]

        if j < w:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)

print(d[-1][-1])
