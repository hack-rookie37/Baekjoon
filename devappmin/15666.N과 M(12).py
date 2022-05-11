import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
items = sorted(list(set(map(int, sys.stdin.readline().split()))))

for item in combinations_with_replacement(items, m):
    print(*item)