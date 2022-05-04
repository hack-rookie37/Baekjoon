from itertools import combinations
from sys import stdin

n, m = map(int, stdin.readline().split())
for value in combinations([x for x in range(1, n + 1)], m):
    print(*value)
