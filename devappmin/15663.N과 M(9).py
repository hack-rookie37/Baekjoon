import sys
from itertools import permutations 

n, m = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
item_set = set()

for item in permutations(items, m):
    item_set.add(item)

for item in sorted(list(item_set)):
    print(*item)