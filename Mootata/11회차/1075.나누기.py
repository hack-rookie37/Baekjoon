import sys

input = sys.stdin.readline

n = int(input())
f = int(input())
front = n // 100
answer = front * 100

while answer % f != 0:
    answer += 1
print(str(answer)[-2:])