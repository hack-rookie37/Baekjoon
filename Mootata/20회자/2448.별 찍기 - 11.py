n = int(input()) # N = (3 x 2^k)

star = [[' '] * 2 * n for _ in range(n)]

def recursive(x, y, N):
    if N == 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = star[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
    else:
        N //= 2
        recursive(x, y, N)
        recursive(x + N, y - N, N)
        recursive(x + N, y + N, N)

recursive(0, n - 1, n)

for i in star:
    print(''.join(i))