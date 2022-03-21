import sys

n, m = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))

left, right = 0, 1
count = 0
while right <= n and left <= right:
    weight = sum(items[left:right])

    if weight == m:
        count += 1
        right += 1
    elif weight < m:
        right += 1
    else:
        left += 1

print(count)
