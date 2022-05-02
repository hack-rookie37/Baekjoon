import sys

def check_last(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        return False

    return True

def solution(s):
    left, right = 0, len(s) - 1
    answer = 0

    if s == s[::-1]:
        return 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        check_left = check_last(s, left + 1, right)
        check_right = check_last(s, left, right - 1)

        answer = 1 if check_left or check_right else 2
        break

    return answer

t = int(sys.stdin.readline())

for _ in range(t):
    print(solution(input()))