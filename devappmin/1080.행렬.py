import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
b = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans = 0

def reverse(y, x):
    for y_idx in range(y, y + 3):
        for x_idx in range(x, x + 3):
            a[y_idx][x_idx] = (a[y_idx][x_idx] + 1) % 2

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            reverse(i, j)
            ans += 1

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit(0)

print(ans)