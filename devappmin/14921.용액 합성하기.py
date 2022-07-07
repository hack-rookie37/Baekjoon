import sys

n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
answer = float('inf')

left, right = 0, n - 1
while left < right:
    solution_sum = solutions[left] + solutions[right]
    answer = min(answer, solution_sum, key=lambda a: abs(a))

    if solution_sum < 0:
        left += 1
    else:
        right -= 1

print(answer)