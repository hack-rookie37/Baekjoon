import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input()) # 상자의 개수 n
boxes = list(map(int, input().split()))

answer = [float('inf')] * n

for i in range(n):
    index = bisect_left(answer, boxes[i])
    answer[index] = boxes[i]

print(bisect_left(answer, float('inf')))