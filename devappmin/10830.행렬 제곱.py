import sys

n, b = map(int, sys.stdin.readline().split())
a = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

def mul(u, v):
    n = len(u)
    z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += u[row][i] * v[i][col]
            z[row][col] = e % 1000

    return z

def square(a, b):
    if b == 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= 1000
        return a
    
    tmp = square(a, b//2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)

result = square(a, b)
for r in result:
    print(*r)