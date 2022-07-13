import sys

n = int(sys.stdin.readline())
solutions = sorted(list(map(int, sys.stdin.readline().split())))


answer = 3000000001
position = [0, 1, n - 1]

for left_idx in range(n - 2):
    left, center, right = left_idx, left_idx + 1, n - 1

    while center < right:
        sum_value = solutions[left] + solutions[center] + solutions[right]

        if abs(sum_value) < answer:
            answer = abs(sum_value)
            position = [left, center, right]
        
        if sum_value < 0:
            center += 1
        else:
            right -= 1


print(solutions[position[0]], solutions[position[1]], solutions[position[2]])
