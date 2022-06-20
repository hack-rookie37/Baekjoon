import sys

input = sys.stdin.readline


def sol():
    n, m, b = map(int, input().split())
    data = [0] * 257
    for _ in range(n):
        for i in map(int, input().split()):
            data[i] += 1
    have = sum(i * data[i] for i in range(257))
    ans = (have * 2, 0)
    need = 0
    t = data[0]
    nm = n * m
    for i in range(1, 257):
        need += t
        have -= nm - t
        t += data[i]
        if have + b - need < 0:
            break
        else:
            ans = min((have * 2 + need, -i), ans)
    print(ans[0], -ans[1])


sol()
