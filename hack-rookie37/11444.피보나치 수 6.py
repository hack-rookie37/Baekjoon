Q = 1000000007
m = [[1, 1], [1, 0]]


def power(a, b):
    cal = []
    for i in range(2):
        row = []
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k] * b[k][j]
            row.append(num % Q)
        cal.append(row)
    return cal


def fibo(n, s=m):
    if n <= 1:
        return m

    x = fibo(n // 2, s)

    cal = power(x, x)

    if n % 2:
        return power(cal, m)
    else:
        return cal


n = int(input())

print(fibo(n)[0][1])
