import sys
from collections import defaultdict

dicts = defaultdict(int)

n = int(sys.stdin.readline())

for num in list(map(int, sys.stdin.readline().split())):
    dicts[num] += 1

m = int(sys.stdin.readline())

for num in list(map(int, sys.stdin.readline().split())):
    print(dicts[num], end=" ")