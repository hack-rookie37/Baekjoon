import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
b = sorted(list(map(int, sys.stdin.readline().split())))

print(sum([a[x] * b[x] for x in range(n)]))

