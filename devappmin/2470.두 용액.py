import sys

n = int(sys.stdin.readline())
solutions = sorted(list(map(int, sys.stdin.readline().split())))

answer = 2100000000
position = [0, n - 1]
left, right = 0, n - 1

while left < right:
    sum_value = solutions[left] + solutions[right]

    if abs(sum_value) < answer:
        answer = abs(sum_value)
        position = [left, right]
    
    if sum_value < 0:
        left += 1
    else:
        right -= 1

print(solutions[position[0]], solutions[position[1]])