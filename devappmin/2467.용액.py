import sys

n = int(sys.stdin.readline())
solutions = sorted(list(map(int, sys.stdin.readline().split())))

left, right = 0, n - 1
answer = float('inf')
answer_pos = [0, n - 1]

while left < right:
    sum_value = solutions[left] + solutions[right]

    if answer > abs(sum_value):
        answer = abs(sum_value)
        answer_pos = [left, right]
    
    if sum_value < 0:
        left += 1
    else:
        right -= 1

print(solutions[answer_pos[0]], solutions[answer_pos[1]])