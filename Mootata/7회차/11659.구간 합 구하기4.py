import sys

n, m = map(int, sys.stdin.readline().split()) # 수의 개수 n, 합을 구해야 하는 횟수 m
numbers = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
value = 0

for i in range(n):
    value += numbers[i]
    prefix_sum.append(value)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1])