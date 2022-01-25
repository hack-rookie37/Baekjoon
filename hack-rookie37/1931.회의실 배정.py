from sys import stdin

input = stdin.readline

N = int(input())
q = [tuple(map(int, input().split())) for _ in range(N)]
q.sort(key=lambda a: (a[1], a[0]))

last = 0
count = 0

for i, j in q:
    if i >= last:
        count += 1
        last = j

print(count)
