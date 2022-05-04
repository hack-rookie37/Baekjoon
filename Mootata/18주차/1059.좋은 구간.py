import sys

input = sys.stdin.readline

l = int(input())
numbers = list(map(int, input().split())) + [0]
n = int(input()) # == n

numbers.sort()

answer = 0
for i in range(len(numbers) - 1) :
    if numbers[i] == n or numbers[i + 1] == n:
        answer = 0
        break
    elif numbers[i] < n and n < numbers[i + 1]:
        answer = (n - numbers[i]) * (numbers[i + 1] - n) - 1
        break

print(answer)