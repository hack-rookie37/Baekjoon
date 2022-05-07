import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

for items in permutations(nums, m):
    print(*items)