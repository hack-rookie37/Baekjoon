import sys

n = int(sys.stdin.readline())
ropes = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)
ans = [ropes[x] * (x + 1) for x in range(n)]

print(max(ans))