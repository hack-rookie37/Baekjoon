import sys

n, m = map(int, sys.stdin.readline().split())

sites = {}

for i in range(n):
    site, pw = sys.stdin.readline().split()
    sites[site] = pw

for i in range(m):
    print(sites[sys.stdin.readline().rstrip()])