import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

answer = []

for num in check:
    left = bisect_left(cards, num)
    right = bisect_right(cards, num)
    answer.append(right - left)

print(*answer)