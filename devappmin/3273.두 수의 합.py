import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

left, right = 0, n - 1

ans = 0
while left < right:
    v = a[left] + a[right]
    if v == x:
        ans += 1
        left += 1
    elif v < x:
        left += 1
    elif v > x:
        right -= 1

print(ans)
