import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

num_sum, length = nums[0], 1
answer = float('inf')
left, right = 0, 0

while left < n - 1:
    if right == n - 1:
        num_sum -= nums[left]
        left += 1
        length -= 1

        if num_sum >= s and length > 0:
            answer = min(answer, length)

        continue

    if num_sum >= s and left <= right:
        answer = min(answer, length)
        num_sum -= nums[left]
        left += 1
        length -= 1
    else:
        right += 1
        length += 1
        num_sum += nums[right]

        if right == n - 1 and num_sum >= s:
            answer = min(answer, length)
    

print(answer if answer != float('inf') else 0)