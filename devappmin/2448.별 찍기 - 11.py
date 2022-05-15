import sys

n = int(sys.stdin.readline())

stars = [[' '] * n * 2 for _ in range(n)]

def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    else:
        new_size = size//2
        recursion(i, j, new_size)
        recursion(i + new_size, j - new_size, new_size)
        recursion(i + new_size, j + new_size, new_size)

recursion(0, n - 1, n)
for star in stars:
    print("".join(star))