import sys

input = sys.stdin.readline

N, S = map(int, input().split())
series = list(map(int, input().split()))

answer = float("inf")
_sum = end = 0

for start in range(N):
    while end < N and _sum < S:
        _sum += series[end]
        end += 1

    if _sum >= S:
        answer = min(answer, end - start)
    _sum -= series[start]

if answer == float("inf"):
    print(0)
else:
    print(answer)
