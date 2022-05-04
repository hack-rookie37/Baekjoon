import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
d = {v: k for k, v in enumerate(sorted(set(x)))}

for i in range(n):
    print(d[x[i]], end=' ')